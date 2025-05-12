from fastapi import FastAPI, HTTPException
from typing import List
from datetime import date

from models import UserCreate, UserRead, Task, TaskCreate

app = FastAPI()

# Temporary in-memory storage
users_db = {}
tasks_db = {}

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task Tracker API"}

# Create user endpoint
@app.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    user_data = user.dict()
    user_data["id"] = user_id
    users_db[user_id] = user_data
    return user_data

# Get user endpoint
@app.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Get all users
@app.get("/users/", response_model=List[UserRead])
async def get_users():
    return list(users_db.values())

# Create task endpoint
@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate):
    task_id = len(tasks_db) + 1
    task_data = task.dict()
    task_data["id"] = task_id
    tasks_db[task_id] = task_data
    return task_data

# Get task endpoint
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update task status
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task_status(task_id: int, status: str):
    if status not in ["pending", "in_progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")
    
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task["status"] = status
    tasks_db[task_id] = task
    return task

# List tasks for a user
@app.get("/users/{user_id}/tasks", response_model=List[Task])
async def get_user_tasks(user_id: int):
    user_tasks = [task for task in tasks_db.values() if task["user_id"] == user_id]
    if not user_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user")
    return user_tasks
