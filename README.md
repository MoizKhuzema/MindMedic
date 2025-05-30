# MindMedic - AI Mental Health Assistant 🧠

MindMedic is an AI-powered mental health diagnostic assistant built using FLAN-T5 and LangChain. It helps users understand potential mental health concerns by providing evidence-based information and preliminary insights based on trusted mental health resources.

![image](https://github.com/user-attachments/assets/d718b1a8-8936-4996-b8aa-d86b44ad49af)


## Table of Contents

- [MindMedic - AI Mental Health Assistant 🧠](#mindmedic---ai-mental-health-assistant-)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Important Note](#important-note)
    - [Emergency Resources:](#emergency-resources)
  - [Contributing](#contributing)

## Introduction

MindMedic leverages advanced language models and vector stores to provide informative responses to mental health-related queries. It processes and understands a curated collection of mental health resources to offer reliable, evidence-based information about various mental health conditions, symptoms, and general mental wellness topics.

## Features

- 🤖 Powered by Google's FLAN-T5 language model
- 📚 Knowledge base built from trusted mental health resources
- 💡 Provides evidence-based responses with sources
- 🔍 Semantic search capabilities for accurate information retrieval
- 💻 User-friendly chat interface powered by Chainlit
- 🔒 Runs locally for privacy

## Prerequisites

Before setting up MindMedic, ensure you have:

- Python 3.6 or higher
- pip (Python package manager)
- 4GB+ RAM recommended
- CPU with x86_64 architecture

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/MindMedic.git
   cd MindMedic
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Prepare the knowledge base:
   ```bash
   python ingest.py
   ```

## Usage

1. Start the MindMedic chatbot:
   ```bash
   chainlit run model.py -w
   ```

2. Open your web browser and navigate to `http://localhost:8000`

3. Start interacting with MindMedic by asking mental health-related questions

Example queries:
- "What are the common symptoms of anxiety?"
- "How can I tell if I'm experiencing depression?"
- "What are some coping strategies for stress?"
- "Can you explain what panic attacks feel like?"

## Important Note

⚠️ **Disclaimer**: MindMedic is an AI assistant designed to provide information and general guidance about mental health topics. It is NOT a replacement for professional mental health care. Always consult with qualified mental health professionals for diagnosis and treatment. In case of emergency, contact your local emergency services or mental health crisis hotline immediately.

### Emergency Resources:
- National Suicide Prevention Lifeline (US): 988
- Crisis Text Line: Text HOME to 741741
- Find local mental health resources: [NAMI HelpLine](https://www.nami.org/help)

## Contributing

Contributions to improve MindMedic are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure your contributions align with mental health best practices and maintain the focus on providing accurate, helpful information.

---

Built with ❤️ for mental health awareness and support. Remember, it's okay to not be okay, and seeking help is a sign of strength.
