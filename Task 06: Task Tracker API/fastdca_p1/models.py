from pydantic import BaseModel, EmailStr, constr, validator
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, EmailStr, constr
from typing import Annotated

# User Models
# class UserCreate(BaseModel):
#     username: constr(min_length=3, max_length=20)
#     email: EmailStr
class UserCreate(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20)]
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # This helps FastAPI to parse ORM models into Pydantic models


# Task Models
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: date
    status: str  # status will be validated

    class Config:
        orm_mode = True

    @validator('due_date')
    def check_due_date(cls, value):
        if value < date.today():
            raise ValueError('due_date must be today or in the future')
        return value


# Task Creation Model (without id, to use during task creation)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
