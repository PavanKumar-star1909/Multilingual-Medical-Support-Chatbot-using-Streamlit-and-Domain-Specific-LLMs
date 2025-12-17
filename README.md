
# Multilingual Medical Support Chatbot

## Overview
A Streamlit-based multilingual medical chatbot that translates user queries,
generates medical guidance using a domain-specific LLM, and translates responses back.

⚠️ Disclaimer: This chatbot is NOT a replacement for professional medical advice.

## Tech Stack
- Streamlit
- Hugging Face Transformers
- NLP / LLM
- Translation Models

## Project Structure
app.py
src/
  ├── translator.py
  ├── medical_llm.py
  ├── utils.py

## How to Run
```bash
git clone <your-github-repo>
cd Multilingual_Medical_Chatbot
pip install -r requirements.txt
streamlit run app.py
```

## Dataset (Recommended)
- MedQuAD (HuggingFace)
- PubMedQA
- HealthcareMagicQA

## Deployment
- Hugging Face Spaces
- Streamlit Cloud
