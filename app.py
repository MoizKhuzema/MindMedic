import gradio as gr
from model import final_result

def process_query(message):
    """Process the user's query and return the response"""
    response = final_result(message)
    answer = response.get("result", "I apologize, but I couldn't generate a response.")
    
    # Format sources if available
    sources = response.get("source_documents", [])
    if sources:
        formatted_sources = []
        for source in sources:
            if hasattr(source, 'page_content'):
                formatted_sources.append(source.page_content.strip())
        
        if formatted_sources:
            answer = f"{answer}\n\nBased on the following information:\n" + "\n\n".join(formatted_sources)
    
    return answer

# Create the Gradio interface
iface = gr.Interface(
    fn=process_query,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask me about mental health...",
        label="Your Question"
    ),
    outputs=gr.Textbox(
        label="MindMedic's Response",
        lines=10
    ),
    title="MindMedic - AI Mental Health Assistant",
    description="I'm here to provide information about mental health topics. Remember: I'm an AI assistant, not a replacement for professional mental health care.",
    examples=[
        ["What are common symptoms of anxiety?"],
        ["How can I tell if I'm experiencing depression?"],
        ["What are some effective stress management techniques?"],
        ["Can you explain what panic attacks feel like?"]
    ],
    theme=gr.themes.Soft()
)

# Add disclaimer
iface.add_markdown("""
### ⚠️ Important Disclaimer
This AI assistant provides information and general guidance about mental health topics. It is NOT a replacement for professional mental health care.
Always consult qualified mental health professionals for diagnosis and treatment.

### 🆘 Emergency Resources
- **National Suicide Prevention Lifeline (US)**: 988
- **Crisis Text Line**: Text HOME to 741741
- **Find local mental health resources**: [NAMI HelpLine](https://www.nami.org/help)
""")

# Launch the interface
iface.launch() 