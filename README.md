# Multilingual AI Email Reply Demo

This is a simplified demo of a multilingual AI-powered email agent, built with **FastAPI** and designed for deployment on **Vercel** using serverless functions.

It simulates the key workflow of handling customer service emails in multiple languages by:
- Translating incoming customer emails into German (internal language)
- Generating a simulated AI response in German
- Translating the response back to the original language of the customer

---

## ✨ Features

- Language detection via input
- Mock translation logic (can be extended with real APIs like DeepL or Google Translate)
- Simulated AI response generator (extendable with OpenAI, Gemini, etc.)
- FastAPI-based serverless function
- Ready to deploy on [Vercel](https://vercel.com)

---

## 🔧 Technologies Used

- Python 3.10+
- FastAPI
- Mangum (for Vercel compatibility)
- Pydantic (for request/response models)

---
---

## 🚀 Running Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/email-agent-demo.git
   cd email-agent-demo

   pip install -r requirements.txt

   uvicorn api.simulate-email-reply:app --reload

   http://localhost:8000/docs

Notes
	•	Translations and responses are mocked for demo purposes
	•	This project is structured to allow easy integration with:
	•	Real translation APIs (e.g. DeepL, Google Translate)
	•	LLMs (e.g. OpenAI GPT-4, Gemini Pro, or local models)   
