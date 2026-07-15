# 🚀 Enterprise AI IT Helpdesk Chatbot

An AI-powered Enterprise IT Helpdesk Chatbot developed as an internship assignment for **Nexoraa Technosolve**.

The application provides intelligent IT support using **Google Gemini AI**, **Retrieval-Augmented Generation (RAG)**, **MongoDB Atlas**, and **Flask REST APIs**. It also includes ticket management, asset management, conversation history, authentication, and an admin dashboard.

---

# 📌 Features

## 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- Role-Based Access (Foundation)

---

## 🤖 AI Helpdesk Chatbot
- Google Gemini AI Integration
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Enterprise Knowledge Base
- Context-Aware Responses

---

## 🎫 Ticket Management
- Create Support Tickets
- Automatic Ticket Creation from Chatbot
- Ticket Priority Detection
- Update Ticket Status
- View All Tickets

---

## 💻 Asset Management
- Add Assets
- View Assets
- Asset Inventory using MongoDB Atlas

---

## 💬 Conversation History
- Save User Conversations
- Retrieve Previous Chats

---

## 📊 Dashboard
- Total Users
- Total Tickets
- Open Tickets
- Resolved Tickets
- Total Assets
- Total Conversations

---

## 📄 API Documentation
- Swagger UI
- RESTful APIs

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask
- Flask-JWT-Extended
- Flasgger (Swagger)

## Database
- MongoDB Atlas

## AI
- Google Gemini API

## RAG
- ChromaDB
- Sentence Transformers

## Authentication
- JWT

---

# 📁 Project Structure

```
enterprise-ai-it-helpdesk-chatbot
│
├── app
│   ├── ai
│   ├── assets
│   ├── auth
│   ├── chatbot
│   ├── conversations
│   ├── dashboard
│   ├── database
│   ├── rag
│   ├── tickets
│   └── config.py
│
├── knowledge_base
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/DHANA-TEJA/enterprise-ai-it-helpdesk-chatbot.git
```

```bash
cd enterprise-ai-it-helpdesk-chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret_key

MONGO_URI=your_mongodb_atlas_uri

GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Run Application

```bash
python app.py
```

Server runs at

```
http://127.0.0.1:5000
```

---

# 📘 Swagger API Documentation

Open

```
http://127.0.0.1:5000/apidocs
```

---

# 🗄️ MongoDB Collections

- users
- tickets
- assets
- conversations

---

# 🔄 System Workflow

```
Employee
     │
     ▼
AI Chatbot
     │
     ▼
Knowledge Retrieval (RAG)
     │
     ▼
Gemini AI
     │
     ▼
Resolved?
   │        │
 Yes       No
  │         │
  ▼         ▼
Answer   Create Ticket
             │
             ▼
MongoDB Atlas
```

---

# 📌 Main APIs

## Authentication
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/profile`

---

## Chatbot
- POST `/chat`

---

## Tickets
- POST `/tickets`
- GET `/tickets`
- PUT `/tickets/{ticket_id}`

---

## Assets
- POST `/assets`
- GET `/assets`

---

## Conversations
- GET `/conversations`

---

## Dashboard
- GET `/dashboard`

---

# 🚀 Future Enhancements

- Email Notifications
- Ticket Assignment Engine
- Asset-aware AI Responses
- Advanced Role-Based Access Control
- Analytics Dashboard
- Multi-Agent AI Support

---

# 👨‍💻 Developed By

**Dhana Teja Naga Varma Gadiraju**

Internship Assignment – **Nexoraa Technosolve**

---

# 📄 License

This project is developed for educational and internship evaluation purposes.
