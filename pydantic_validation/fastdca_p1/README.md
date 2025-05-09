
# **Pydantic Integration for FastAPI**

## **Step 1: Getting Started with Pydantic 🚀**

### **What is Pydantic? 🤔**

Pydantic is a data validation and settings management library that leverages Python type annotations for data schema validation. It's widely used with **FastAPI** for request/response validation, ensuring type safety and automatic error handling.

### **Key Features of Pydantic 🔑**

* **Type-Safe Validation**: Ensures that data matches Python type hints (e.g., `str`, `int`, `List[str]`).
* **Automatic Type Conversion**: Converts strings to integers, booleans to `True/False`, etc.
* **Error Handling**: Provides detailed errors when validation fails.
* **Nested Models**: Supports complex data structures.
* **Serialization**: Converts models to JSON format for API responses.
* **Custom Validators**: Write custom validation logic.

### **Step 2: Set up Pydantic in Your Project ⚙️**

Run the following commands to get started with Pydantic:

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
```

### **1. Basic Pydantic Model Example 🧑‍💻**

Create a file named `pydantic_example_1.py`:

```python
from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field

# Valid data
user_data = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25}
user = User(**user_data)
print(user)  # id=1 name='Alice' email='alice@example.com' age=25
print(user.model_dump())  # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25}

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)
```

#### **Run the Script 🚀:**

```bash
uv run python pydantic_example_1.py
```

#### **Output for Invalid Data ❌:**

```
1 validation error for User
id
  value is not a valid integer (type=type_error.integer)
```

---

### **2. Nested Models 🏠**

Create `pydantic_example_2.py` for a model with nested structures:

```python
from pydantic import BaseModel, EmailStr

# Define Address model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr  # Built-in email validator
    addresses: list[Address]  # List of nested models

# Valid data with nested structure
user_data = {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "addresses": [
        {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
        {"street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001"},
    ],
}
user = UserWithAddress.model_validate(user_data)
print(user.model_dump())
```

#### **Expected Output 📦:**

```json
{
  "id": 2,
  "name": "Bob",
  "email": "bob@example.com",
  "addresses": [
    { "street": "123 Main St", "city": "New York", "zip_code": "10001" },
    { "street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001" }
  ]
}
```

---

### **3. Custom Validators 🛠️**

Create `pydantic_example_3.py` with a custom validator to enforce name length:

```python
from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# Test with invalid data
try:
    invalid_user = UserWithAddress(
        id=3,
        name="A",  # Too short
        email="charlie@example.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    print(e)
```

#### **Validation Error for Short Name ❌:**

```
1 validation error for UserWithAddress
name
  ValueError: Name must be at least 2 characters long
```

---

## **Step 3: Why Use Pydantic in DACA? 🤖**

Pydantic is critical for DACA workflows because:

* **Data Integrity 🛡️**: Validates incoming data and ensures agents send correctly formatted responses.
* **Complex Workflows 🔄**: Handles nested models (e.g., user data with metadata).
* **Serialization 🌐**: Easily converts data to JSON for API responses.
* **Error Handling 🚨**: Provides clear validation errors, aiding debugging in distributed systems.

---

## **Step 4: Build a FastAPI Application for Chatbot 🤖💬**

Create the main FastAPI app with complex Pydantic models:

1. **Create `main.py`:**

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

# Initialize FastAPI app
app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-based API for a chatbot in DACA",
    version="0.1.0",
)

# Define complex Pydantic models
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))

class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata
    tags: list[str] | None = None  # Optional tags

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for API documentation."}

# GET endpoint
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info

# POST endpoint for chat
@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(
            status_code=400, detail="Message text cannot be empty")
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata()  # Auto-generate timestamp and session_id
    )
```

2. **Run the FastAPI server**:

```bash
fastapi dev main.py
```

---

## **Conclusion 🎉**

By following these steps, you can implement Pydantic validation in your FastAPI application for DACA’s agentic AI workflows. This approach ensures that your data is type-safe and error-free, making the system robust and reliable.
