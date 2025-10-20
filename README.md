Project Zenith: Intelligent Enterprise Assistant for the Public Sector (SIH 1706)

Overview: AI-Driven Efficiency for the Public Sector

Project Zenith is an Intelligent Enterprise Assistant I developed to directly address the challenge of slow information access and inefficient internal processes within public sector organizations.

The solution is a scalable, secure chatbot that functions as an internal helpdesk. It utilizes advanced AI and Machine Learning techniques, specifically Retrieval-Augmented Generation (RAG), to efficiently handle complex tasks such as retrieving obscure HR policies, processing document content, and resolving repetitive IT and administrative queries. This capability aims to significantly enhance organizational efficiency and redirect human capital to more strategic responsibilities.

This project addresses the Smart India Hackathon (SIH) Problem Statement SIH 1706: Intelligent Enterprise Assistant: Enhancing Organizational Efficiency through AI-driven Chatbot Integration.

Core Capabilities and Features

I engineered Zenith to meet all critical requirements of the problem statement, ensuring a robust and production-ready system:

Feature

SIH 1706 Requirement

Implementation Strategy

Intelligent Q&A

Accurately understand and respond to queries (HR, IT, Admin, Events).

A Retrieval-Augmented Generation (RAG) architecture leveraging a pre-indexed vector database of public sector documents (policies, manuals).

Document Processing

Analyze and extract information from uploaded documents (summarization, keyword extraction).

Integration with a large language model (LLM) and Optical Character Recognition (OCR) service to process document uploads (PDF/DOCX), perform chunking, and generate on-the-fly summaries and insights.

Scalable Architecture

Handle a minimum of 5 users parallelly; Response Time < 5 seconds.

Asynchronous web framework (FastAPI/Node.js) utilizing concurrent LLM API calls and efficient caching mechanisms for high performance.

Multi-Factor Auth (2FA)

Enable 2FA (email ID type) for enhanced security.

Custom two-step verification implemented using a secure token delivered to the registered email address upon login.

Bad Language Filtering

Chatbot should filter bad language as per a system-maintained dictionary.

A dedicated pre-processing layer employing a toxicity classifier (e.g., Hugging Face model or custom filter) before the query is processed by the LLM.

Multilingual Support

Best Practice: Support for multiple regional languages (e.g., Hindi, English).

Integration with a translation service or a pre-trained multilingual LLM to facilitate user interaction in diverse languages.

Audit Logging

Best Practice: Traceability of all user interactions and responses.

Firestore/PostgreSQL database utilized for immutable logging of all user queries, model responses, and session metadata for compliance and improvement.

Technology Stack

The technology stack utilizes modern, scalable components optimized for high performance and maintainability:

Category

Technology

Purpose

Backend/Core Logic

Python, FastAPI

High-performance, asynchronous API server.

NLP/LLM

Gemini API (or fine-tuned Open Source LLM), LangChain/LlamaIndex

Core engine for conversational understanding, RAG pipeline, and summarization.

Vector Database

ChromaDB or Pinecone

Storage and retrieval of vectorized public sector documentation for the RAG system.

Authentication

Firebase Auth / OAuth 2.0 (for 2FA)

Secure user management and custom email-based 2FA implementation.

Frontend

React or Next.js

Modern, responsive UI for the chatbot interface and administrative dashboards.

Deployment

Docker (Optional)

Containerization for consistent, scalable deployment across environments.

Installation and Setup

Follow these steps to deploy Project Zenith locally for demonstration and development.

Prerequisites

Python 3.10+

Node.js (for the frontend)

Git

Docker (Recommended)

1. Backend Setup

# Clone the repository
git clone [https://github.com/your-username/An-Intelligent-Enterprise-Assistant-for-public-sector](https://github.com/your-username/An-Intelligent-Enterprise-Assistant-for-public-sector)
cd An-Intelligent-Enterprise-Assistant-for-public-sector/backend

# Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment Variables
# Create a .env file and add your API keys and configuration:
cp .env.example .env

# Example .env content:
# GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
# FIREBASE_API_KEY="YOUR_FIREBASE_WEB_API_KEY"
# EMAIL_SECRET="A_STRONG_SECRET_FOR_2FA"

# Run the backend server
uvicorn main:app --reload


2. Document Ingestion (RAG Setup)

The RAG system requires the knowledge base to be indexed.

Place the sample public sector documents (HR manuals, IT guides, etc.) into the /data/source_documents folder.

Run the ingestion script:

python ingest_documents.py
# This script processes documents, generates embeddings, and stores them 
# in the Vector Database (e.g., ChromaDB).


3. Frontend Setup

cd ../frontend

# Install dependencies
npm install

# Start the React/Next.js development server
npm run dev


The application should now be accessible at http://localhost:3000.

License

This project is licensed under the MIT License—see the LICENSE file for details.
