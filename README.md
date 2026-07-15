# 🚀 Enterprise AI IT Helpdesk Chatbot

An AI-powered Enterprise IT Helpdesk Chatbot developed as an internship assignment for **Nexoraa Technosolve**.

The system assists employees in resolving IT issues using **Google Gemini AI** with **Retrieval-Augmented Generation (RAG)**. If an issue cannot be resolved, it automatically creates an IT support ticket. The application also provides authentication, asset management, conversation history, dashboard analytics, and REST APIs documented with Swagger.

---

# 📌 Features

## 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- Role-based user information

---

## 🤖 AI Helpdesk Chatbot
- Google Gemini AI Integration
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Enterprise Knowledge Base
- Intelligent troubleshooting
- Automatic ticket creation for unresolved issues

---

## 🎫 Ticket Management
- Create IT support tickets
- View all tickets
- Update ticket status
- Automatic priority detection
- Automatic ticket generation from chatbot

---

## 💻 Asset Management
- Add enterprise assets
- View assets
- Store asset inventory in MongoDB Atlas

---

## 💬 Conversation History
- Store chatbot conversations
- Retrieve previous conversations
- Track whether a ticket was created

---

## 📊 Admin Dashboard
- Total Users
- Total Tickets
- Open Tickets
- Resolved Tickets
- Total Assets
- Total Conversations

---

## 📄 API Documentation
- Swagger UI Documentation
- RESTful API Design

---

# 🛠️ Technology Stack

## Backend
- Python
- Flask
- Flask-JWT-Extended
- Flasgger (Swagger)

## Database
- MongoDB Atlas

## Artificial Intelligence
- Google Gemini API

## Retrieval-Augmented Generation
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
├── screenshots
├── README.md
├── DATABASE_SCHEMA.md
├── SAMPLE_CONVERSATIONS.md
├── Dockerfile
├── requirements.txt
├── .env.example
└── app.py
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

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
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

MONGO_URI=your_mongodb_atlas_connection_string

GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Run Application

```bash
python app.py
```

Application runs at:

```
http://127.0.0.1:5000
```

---

# 📘 API Documentation

Swagger UI:

```
http://127.0.0.1:5000/apidocs
```

---

# 🗄️ MongoDB Collections

The project uses the following collections:

- users
- tickets
- assets
- conversations

---

# 🔄 Application Workflow

```
Employee
     │
     ▼
Login
     │
     ▼
AI Chatbot
     │
     ▼
Knowledge Retrieval (RAG)
     │
     ▼
Google Gemini AI
     │
     ▼
Issue Resolved?
     │
 ┌───┴─────────┐
 │             │
Yes           No
 │             │
 ▼             ▼
Answer     Create Ticket
               │
               ▼
          MongoDB Atlas
               │
               ▼
        Dashboard & History
```

---

# 📌 REST APIs

## Authentication

| Method | Endpoint |
|----------|-----------|
| POST | `/auth/register` |
| POST | `/auth/login` |
| GET | `/auth/profile` |

---

## Chatbot

| Method | Endpoint |
|----------|-----------|
| POST | `/chat` |

---

## Tickets

| Method | Endpoint |
|----------|-----------|
| POST | `/tickets` |
| GET | `/tickets` |
| PUT | `/tickets/{ticket_id}` |

---

## Assets

| Method | Endpoint |
|----------|-----------|
| POST | `/assets` |
| GET | `/assets` |

---

## Conversations

| Method | Endpoint |
|----------|-----------|
| GET | `/conversations` |

---

## Dashboard

| Method | Endpoint |
|----------|-----------|
| GET | `/dashboard` |

---

# 📚 Additional Documents

The repository also includes:

- `DATABASE_SCHEMA.md`
- `SAMPLE_CONVERSATIONS.md`
- `.env.example`
- `Dockerfile`
- `knowledge_base/`
- Swagger API Documentation

---

# 🚀 Future Improvements

- Advanced RBAC
- Email Notifications
- Ticket Assignment Workflow
- Asset-aware AI Responses
- Analytics Dashboard
- Multi-Agent AI Support

---

# 👨‍💻 Author

**Dhana Teja Naga Varma Gadiraju**

Internship Assignment Submission

**Nexoraa Technosolve**

---

# 📄 License

This project was developed for educational and internship evaluation purposes.
