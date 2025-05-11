
# **Step 4: Dependency Injection in FastAPI 🚀**

In this step, we explore **Dependency Injection (DI)** in FastAPI, which is a powerful tool to improve your code's reusability, testability, and organization. DI allows you to share reusable logic across your endpoints, like checking user permissions or connecting to a database.

### **Why Use Dependency Injection? 🤔**

* **Code Reusability:** Reuse common logic across multiple endpoints (e.g., fetching the current user).
* **Separation of Concerns:** Keep endpoint logic focused on specific tasks, delegating common tasks to dependencies (e.g., authentication).
* **Testability:** Easily mock dependencies for unit testing.
* **Organization:** Keep your codebase clean and structured.

### **How Dependency Injection Works in FastAPI 🔍**

1. **Define a Dependency:**
   Create a function (or class) that handles the necessary setup or provides a shared resource. Dependencies can also have parameters, which FastAPI will automatically resolve, including other dependencies.

2. **"Depend" on It:**
   Add a parameter to your endpoint function, type-hinted with the return type of the dependency. Use `Depends(your_dependency_function)` to inject the dependency. For cleaner syntax, you can use `typing.Annotated`.

3. **FastAPI Execution:**
   FastAPI will execute the dependency for each request that needs it and pass the result to the endpoint function. FastAPI also caches the dependency result within the same request, so it's only executed once per request.

---

## **Setup: 🚀**

If you're continuing from Step 3, make sure you're in the **03\_api\_parameters** directory. If you're starting fresh, follow these steps:

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
```

---

## **Learning Plan: 📚**

We’ll learn **Dependency Injection** through four simple examples:

1. **Check a Secret Key 🔑**
2. **Common Query Parameters 🔍**
3. **Simulate a Database 🗄️**
4. **Sub-Dependencies 🔗**

---

### **1. Hello Dependency 🌟**

First, let’s define a simple dependency that returns a goal.

```python
from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response
```

* This example demonstrates how to inject a simple goal using a dependency.

---

### **2. Dependency with Parameter 🧩**

Now, let’s pass a parameter to our dependency function.

```python
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response
```

* This shows how to pass parameters to the dependency function (like the `username`).

---

### **3. Dependency with Query Parameters 🔐**

Let’s use a dependency to check for a secret key in the query parameters.

```python
from fastapi import FastAPI, Depends, Query

app = FastAPI()

def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user
```

* This example demonstrates using query parameters for user authentication.

---

### **4. Multiple Dependencies 🔄**

Here, we demonstrate how to use multiple dependencies together.

```python
def depfunc1(num: int):
    num += 1
    return num

def depfunc2(num: int):
    num += 2
    return num

@app.get("/main/{num}")
def get_main(num: int, num1: Annotated[int, Depends(depfunc1)], num2: Annotated[int, Depends(depfunc2)]):
    total = num + num1 + num2
    return f"Pakistan {total}"
```

* This shows how multiple dependencies can be used in a single endpoint to perform different actions.

---

### **5. Using Classes as Dependencies 🏷️**

We can also use classes to manage dependencies. Here’s an example of checking for objects in a mock database.

```python
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

class GetObjectOr404():
    def __init__(self, model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name
```

* This shows how to use a class as a dependency to manage resource retrieval.

---

### **Conclusion: 🚀**

Dependency Injection in FastAPI helps you manage complexity in your application by enabling you to reuse code, organize your logic, and write cleaner, testable, and maintainable code.

Now that you understand the basics, you can apply DI in your own FastAPI projects to handle things like authentication, data access, and more!

---

# **Ready to start building your FastAPI application?**

Explore more examples and enhance your API with advanced features. Stay tuned for the next steps in the FastAPI journey! 🌍
