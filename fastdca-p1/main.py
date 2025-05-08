from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Item route with optional query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
