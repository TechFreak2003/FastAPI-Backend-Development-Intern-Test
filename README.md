# FastAPI Backend Development Intern Test

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A robust backend application built with FastAPI that demonstrates authentication, prompt handling, and user session management. The system features secure token-based authentication, real-time prompt processing with AI-style responses, and persistent history tracking for each user session.

The application showcases professional API design principles, proper error handling, and modular architecture suitable for scalable backend development. It's optimized for development environments and demonstrates industry-standard practices for authentication and data management.

## 📦 Repository Structure

| Component | Description |
|-----------|-------------|
| 🔗 **Backend API** | Core FastAPI application with authentication |
| 🔗 **Authentication** | Token-based security system |
| 🔗 **Data Models** | Pydantic models for request/response validation |
| 🔗 **Route Handlers** | Modular endpoint organization |
| 📁 **history.json** | Stores persistent user prompt history |
| 📁 **response_*.json** | Stores Swagger UI auth tokens (temporary/debugging) |

## 📂 Project Structure

```
backend_app/
├── auth.py                   # Authentication logic and token handling
├── history.json              # JSON file for persistent user history
├── main.py                   # FastAPI application entry point
├── models.py                 # Pydantic request/response models
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py        # Authentication routes
│   ├── history_routes.py     # History retrieval routes
│   └── prompt_routes.py      # Prompt processing routes
├── response_*.json           # Token responses from Swagger UI (for debugging)
├── requirements.txt          # Dependency list
├── README.md                 # Project documentation
└── .gitignore                # Ignored files and folders
```

## 🧠 Key Purpose

This FastAPI backend application demonstrates modern backend practices, showcasing secure login, user prompt handling, and response generation with persistent history stored in `history.json`.

## 🛠 Tech Stack

- **FastAPI** — Web framework for building APIs  
- **Pydantic** — Data validation and serialization  
- **Uvicorn** — ASGI server for running the app  
- **Python 3.8+** — Programming language  
- **JWT-style Auth** — Secure token-based system  
- **File-based Storage** — History stored in `history.json`

## 🔧 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Suvrodeep2002/fastapi-backend-intern-test
cd backend_app

# Create and activate virtual environment
python -m venv venv
.env\Scripts\Activate.ps1   # On Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🔐 API Endpoints

### Authentication
- `POST /login` — User authentication & token generation

### Prompts
- `POST /prompt` — Submit prompt for AI-like response (requires token)

### History
- `GET /history` — Retrieve your prompt history (stored in `history.json`)

### System
- `GET /` — Root API info  
- `GET /health` — Health check

## 💻 Sample Requests

### Login
```bash
curl -X POST "http://localhost:8000/login" -H "Content-Type: application/json" -d '{"username": "alice", "password": "password123"}'
```

### Prompt Submit
```bash
curl -X POST "http://localhost:8000/prompt" -H "Authorization: Bearer <your-token>" -H "Content-Type: application/json" -d '{"prompt": "What is the capital of France?"}'
```

### View History
```bash
curl -X GET "http://localhost:8000/history" -H "Authorization: Bearer <your-token>"
```

## 📄 History Storage

- All user interactions are saved persistently in `history.json`  
- The structure supports per-user prompt tracking  
- Helps simulate database behavior in a lightweight format

## 👨‍💻 Developer Info

| Name           | Branch           | Degree                     | Year       | University                                                 | Role               |
|----------------|------------------|-----------------------------|------------|------------------------------------------------------------|--------------------|
| Suvrodeep Das  | Computer Science | B.Tech in Computer Science | 3rd Year   | Maulana Abul Kalam Azad University of Technology (MAKAUT) | Backend Developer  |


## 🚀 Features

- Token-based Auth  
- File-based Persistent History  
- Swagger UI & ReDoc  
- Modular Routing  
- Proper Exception Handling

## 🔮 Future Scope

- [ ] DB Integration (PostgreSQL/MongoDB)  
- [ ] OAuth or token expiry features  
- [ ] Dockerization  
- [ ] Logging system  
- [ ] Rate Limiting  
- [ ] Unit Tests

## 📫 Contact

Feel free to reach out on GitHub or via email for queries, feedback, or collaboration!

---

**Built with ❤️ using FastAPI. Feel free to fork, contribute, and star!** 🚀
