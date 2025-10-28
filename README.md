


# Intelligent Enterprise Assistant (SIH1706)

An AI-powered virtual assistant designed to help the public sector work smarter. It automates tasks like document search, policy answering, leave requests, and helpdesk support — all through natural conversation.

## Overview

The Intelligent Enterprise Assistant acts as a smart chatbot that integrates with internal data, automating enterprise workflows for public sector organizations.
It can:

* Understand and answer employee or citizen queries
* Fetch information from official documents
* Automate internal tasks (leave/expense/helpdesk)
* Provide a dashboard for administrators

## Problem Statement

Government and public organizations face difficulty managing large amounts of internal documents and repetitive queries. Existing systems are slow and manual.
**Goal:** Build a system that improves efficiency by combining AI + NLP + automation to create a self-learning digital assistant.

## Features

* Conversational chatbot interface (text-based)
* Policy and SOP document search with context answers
* Workflow automation (leave, travel, expenses)
* Ticket creation for support issues
* Dashboard for admin tracking
* Role-based secure access

## Tech Stack

| Layer         | Technology                             |
| ------------- | -------------------------------------- |
| Frontend      | HTML, CSS, JavaScript (React optional) |
| Backend       | FastAPI (Python)                       |
| AI / NLP      | Sentence Transformers, HuggingFace     |
| Database      | PostgreSQL / SQLite                    |
| Vector Search | FAISS                                  |
| Deployment    | Docker / Render / Railway              |

## Installation & Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/intelligent-enterprise-assistant.git
cd intelligent-enterprise-assistant
```

### 2. Backend setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend setup

Open `frontend/index.html` in your browser.

## Example Query

> What is the travel allowance for Grade A officers?
> How many casual leaves can I apply for?
> The assistant responds instantly from stored policies and returns the relevant section with citation.

## Project Structure

```
intelligent-enterprise-assistant/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── data/
│   └── sample_policies.json
│
└── README.md
```
## How to Run Everything
```
Step 1: Open Terminal in your project folder
cd intelligent-enterprise-assistant/backend

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Start backend server
uvicorn main:app --reload


You’ll see:
Running on http://127.0.0.1:8000

Step 4: Open frontend

Open frontend/index.html in your browser.
Ask something like:

What is the travel allowance?
How many leave days are allowed?


✅ It’ll reply using your sample policy data!
```



## Hackathon Info

**Hackathon:** Smart India Hackathon 2025
**Problem Statement:** SIH1706 – Intelligent Enterprise Assistant for Public Sector
**Theme:** Artificial Intelligence / Smart Automation

## Future Enhancements

* Integrate voice-based chat using Speech-to-Text
* Add multilingual support (English, Hindi, Tamil, etc.)
* Connect with real HRMS or ERP systems via APIs
* Add admin analytics dashboard

## OUTPUT:
<img width="906" height="669" alt="Employees are entitled to 20 days of annual leave per year, in addition to public holidays  Casual and sick leaves can also be availed as per HR policy" src="https://github.com/user-attachments/assets/8cbcaa7e-dd6f-4b2c-a9b1-b2d809416046" />


## License

This project is open-source under the MIT License.


