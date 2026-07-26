# 🔐 Week 4 – Authentication with Supabase

A FastAPI authentication service that integrates **Supabase Auth** to provide secure user registration, login, JWT authentication, and protected routes.

---

## 📌 Assignment Objective

Build a backend authentication API using **FastAPI** and **Supabase Authentication** that allows users to:

- Register with email and password
- Login securely
- Receive JWT access tokens
- Access protected endpoints
- Handle authentication errors gracefully

---

# 🚀 Features

- ✅ User Signup
- ✅ User Login
- ✅ JWT Authentication
- ✅ Protected `/me` Endpoint
- ✅ Bearer Token Authentication
- ✅ Secure Password Management (Supabase)
- ✅ Environment Variables
- ✅ Swagger API Documentation
- ✅ Professional Error Handling

---

# 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Supabase
- JWT Authentication
- Pydantic
- Uvicorn
- Python Dotenv

---

# 📂 Project Structure

```
task-api-auth/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── repository.py
│   ├── routes.py
│   ├── schemas.py
│   └── services.py
│
├── images/
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd task-api-auth
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
SUPABASE_URL=YOUR_SUPABASE_PROJECT_URL
SUPABASE_KEY=YOUR_SUPABASE_ANON_KEY
```

---

# ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📖 API Endpoints

## Root

```
GET /
```

Returns application status.

---

## Signup

```
POST /signup
```

Example Request

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

---

## Login

```
POST /login
```

Example Request

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Example Response

```json
{
  "message": "Login successful",
  "access_token": "JWT_TOKEN",
  "token_type": "Bearer"
}
```

---

## Protected Route

```
GET /me
```

Authorization Header

```
Bearer <ACCESS_TOKEN>
```

Example Response

```json
{
  "id": "...",
  "email": "user@example.com",
  "role": "authenticated"
}
```

---

# 📷 Screenshots

## Swagger UI

_Add screenshot_

---

## Successful Signup

_Add screenshot_

---

## Successful Login

_Add screenshot_

---

## Protected Endpoint (/me)

_Add screenshot_

---

# 🧪 Testing

The API was tested using the built-in Swagger UI.

### Successful Tests

- ✅ Signup
- ✅ Login
- ✅ JWT Token Generation
- ✅ Protected Route Access
- ✅ Invalid Login Handling
- ✅ Invalid Signup Handling

---

# 📚 Learning Outcomes

During this assignment I learned:

- FastAPI project architecture
- Authentication using Supabase
- JWT-based authentication
- Protected routes with dependencies
- Bearer Token authorization
- Environment variable management
- Exception handling
- API documentation using Swagger

---

# 👨‍💻 Author

**Devanshu Dasgupta**

Backend AI Engineering Intern — FlyRank AI

GitHub:
https://github.com/Devanshu07R