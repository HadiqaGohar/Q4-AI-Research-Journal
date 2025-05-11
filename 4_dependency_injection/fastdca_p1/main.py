from fastapi import FastAPI, Depends, Query, HTTPException, status 
from typing import Annotated

# Create a FastAPI instance
app: FastAPI = FastAPI()

# ===================== 1. SIMPLE DEPENDENCY =====================
# A basic dependency function returning a static dictionary
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

# This route uses the `get_simple_goal` dependency
@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response  # Returns the result of get_simple_goal


# ===================== 2. DEPENDENCY WITH PARAMETERS =====================
# This dependency expects a query parameter `username`
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

# This route provides `username` as a query param and injects the result
@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response


# ===================== 3. DEPENDENCY WITH QUERY PARAMETERS =====================
# A dependency function that takes `username` and `password` as query params
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

# This route depends on the login function and returns login status
@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user


# ===================== 4. MULTIPLE DEPENDENCIES =====================
# First dependency: increments the number by 1
def depfunc1(num: int): 
    num = int(num)
    num += 1
    return num

# Second dependency: increments the number by 2
def depfunc2(num): 
    num = int(num)
    num += 2
    return num

# Route takes a path parameter `num` and applies both dependencies
@app.get("/main/{num}")
def get_main(
    num: int,
    num1: Annotated[int, Depends(depfunc1)],  # returns num+1
    num2: Annotated[int, Depends(depfunc2)]   # returns num+2
):
    total = num + num1 + num2  # Sums the original and modified numbers
    return f"Pakistan {total}"


# ===================== 5. DEPENDENCY FOR OBJECT FETCHING (404 LOGIC) =====================

# Sample data stores
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

# Custom dependency class to simulate Django-like `get_object_or_404`
class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model  # The data dictionary (e.g., blogs or users)

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object ID {id} not found"
            )
        return obj  # Return the object if found

# Creating dependency instances for blogs and users
blog_dependency = GetObjectOr404(blogs)
user_dependency = GetObjectOr404(users)

# Route to get a blog by ID using dependency injection
@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

# Route to get a user by ID using dependency injection
@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name