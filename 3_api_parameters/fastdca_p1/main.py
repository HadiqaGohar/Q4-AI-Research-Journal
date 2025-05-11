from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ✅ Item model for request body validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# 🔹 1. Path Parameter with Validation
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  # Required field
        title="Item ID",
        description="A unique ID to identify the item",
        ge=1  # Must be >= 1
    )
):
    return {"message": "Item fetched successfully", "item_id": item_id}

# 🔹 2. Query Parameters with Validation
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Search Query",
        description="Keyword to search for items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, le=100, description="Maximum number of items to return")
):
    return {
        "message": "Items fetched successfully",
        "query": q,
        "skip": skip,
        "limit": limit
    }

# 🔹 3. Path + Query + Body together (with all validations)
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    item: Optional[Item] = Body(None, description="JSON body with updated item data")
):
    response = {"item_id": item_id}

    if q:
        response["query"] = q
    if item:
        response["item"] = item.model_dump()

    return {"message": "Item updated successfully", "data": response}