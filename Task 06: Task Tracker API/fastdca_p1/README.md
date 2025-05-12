
# ✅ Task Tracker API with FastAPI 🚀

A beginner-friendly, in-memory **Task Tracker API** using `FastAPI`, where you can create users, manage tasks, and update their status.

![Screenshot](https://github.com/HadiqaGohar/Q4-Exploring-Generative-AI/raw/main/Task%2006%3A%20Task%20Tracker%20API/fastdca_p1/Screenshot%20from%202025-05-12%2020-55-11.png)

---

## 📦 Features

- 👤 Create, get, and list users  
- 📋 Add, get, and update tasks  
- ✅ Filter tasks by user  
- 🧪 Validations with Pydantic  
- 🌐 Interactive Swagger Docs at `/docs`

---

## 🛠️ Installation Guide

Make sure you have [uv](https://github.com/astral-sh/uv) and Python 3.9+ installed.

```bash
# Clone the repo
git clone https://github.com/HadiqaGohar/Q4-Exploring-Generative-AI.git
cd "Task 06: Task Tracker API"/fastdca_p1

# Create virtual environment using uv
uv venv
source .venv/bin/activate

# Install required packages
uv add "fastapi[standard]"
````

---

## ▶️ Run the server

```bash
uvicorn main:app --reload --port 8001
```

Open in browser: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

---

## 🚀 API Endpoints

### 📍 Root

```http
GET /
```

**Response:**

```json
{ "message": "Welcome to the Task Tracker API" }
```

---

### 👤 Users

#### ➕ Create User

```http
POST /users/
```

**Request:**

```json
{
  "username": "hadiqa",
  "email": "hadiqa@example.com"
}
```
![Screenshot](https://github.com/HadiqaGohar/Q4-Exploring-Generative-AI/raw/main/Task%2006%3A%20Task%20Tracker%20API/fastdca_p1/Screenshot%20from%202025-05-12%2020-54-02.png)

#### 🔎 Get User by ID

```http
GET /users/{user_id}
```

#### 📋 List All Users

```http
GET /users/
```

---

### ✅ Tasks

#### ➕ Create Task

```http
POST /tasks/
```

**Request:**

```json
{
  "title": "Study FastAPI",
  "description": "Learn routing and models",
  "due_date": "2025-05-15",
  "status": "pending"
}
```

#### 🔍 Get Task by ID

```http
GET /tasks/{task_id}
```

#### 🔁 Update Task Status

```http
PUT /tasks/{task_id}?status=completed
```

#### 📑 List Tasks for a User

```http
GET /users/{user_id}/tasks
```

---

## 🧠 Tech Stack

* FastAPI
* Pydantic
* Uvicorn
* Python 3.9+
* uv (for fast dependency management)

---

## ✍️ Author

**Hadiqa Gohar**
📎 [GitHub](https://github.com/HadiqaGohar)

---

## ⭐ Like this project?

Give it a ⭐ on GitHub to show support!
