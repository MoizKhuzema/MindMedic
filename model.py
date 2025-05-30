from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.chains import RetrievalQA
import chainlit as cl
from dotenv import load_dotenv
import torch
import os

load_dotenv()  

DB_FAISS_PATH = 'vectorstore/db_faiss'

# Prompt Template
custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

# Create RetrievalQA chain
def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    return qa_chain

# Load Hugging Face LLM
def load_llm():
    # Load model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained(
        "google/flan-t5-base",
        device_map="cpu",
        torch_dtype=torch.float32
    )

    # Create text-generation pipeline without invalid parameters
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        repetition_penalty=1.15
    )

    # Create LangChain wrapper for the pipeline
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm

# Build full chatbot pipeline
def qa_bot():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    db = FAISS.load_local(
        DB_FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)
    return qa

# Run for one query (used internally)
def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

# Chainlit UI - Start
@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to MindMate. What is your query?"
    await msg.update()
    cl.user_session.set("chain", chain)

# Chainlit UI - Handle messages
@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True
    
    # Use invoke with proper query format
    res = await cl.make_async(chain.invoke)(
        {"query": message.content}, 
        callbacks=[cb]
    )
    
    # Extract result and sources from the response
    answer = res.get("result", "No result found")
    sources = res.get("source_documents", [])

    # Format sources to show only the content
    if sources:
        formatted_sources = []
        for source in sources:
            if hasattr(source, 'page_content'):
                formatted_sources.append(source.page_content.strip())
        
        if formatted_sources:
            answer = f"{answer}\n\nBased on the following information:\n" + "\n\n".join(formatted_sources)

    await cl.Message(content=answer).send()
