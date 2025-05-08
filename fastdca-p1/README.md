
# FastAPI Project

This is a simple FastAPI application that demonstrates how to create and run an API with path parameters and query parameters. The app contains basic routes to showcase FastAPI's ease of use for web development.

## Features

- **GET /**: A simple route that returns a "Hello World" message.
- **GET /items/{item_id}**: A dynamic route that accepts an `item_id` as a path parameter and an optional query parameter `q`.

## Prerequisites

Ensure that you have the following installed on your system:

- **Python 3.9+**
- **FastAPI** for building the API.
- **Uvicorn** to run the server.

## Setup & Installation

1. **Clone the repository** or download the code:
   ```bash
   git clone <repository-url>
   cd <project-directory>
````

2. **Create a virtual environment** and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   If you have a `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Or manually install FastAPI and Uvicorn:

   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

After the setup, you can run the application using Uvicorn. From the project root, execute:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

![Revolutionizing Generative AI](https://jktech.com/wp-content/uploads/2024/11/Revolutionizing-Generative-AI.png)

* **main**: Refers to the Python file where your FastAPI app instance (`app`) is defined.
* **--reload**: Enables automatic reloading of the application during development.
* **--host 0.0.0.0**: Makes the app accessible to any IP address (useful for deployment).
* **--port 8000**: Runs the application on port 8000.

## Endpoints

### 1. **GET /**

* **Description**: A simple route that returns a "Hello World" message.
* **Response**:

  ```json
  {
    "Hello": "World"
  }
  ```


![Revolutionizing Generative AI](https://jktech.com/wp-content/uploads/2024/11/Revolutionizing-Generative-AI.png)

### 2. **GET /items/{item\_id}**

* **Description**: This endpoint accepts a path parameter `item_id` and an optional query parameter `q`.
* **Example**: Requesting `http://localhost:8000/items/5?q=somequery`
* **Response**:

  ```json
  {
    "item_id": 5,
    "q": "somequery"
  }
  ```

![Revolutionizing Generative AI](https://jktech.com/wp-content/uploads/2024/11/Revolutionizing-Generative-AI.png)

## Testing the API

* Open your browser or API testing tool (like Postman).
* Visit `http://localhost:8000/` to get a "Hello World" response.
* Visit `http://localhost:8000/items/{item_id}?q=somequery` (replace `{item_id}` with any number) to get item details.
