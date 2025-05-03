from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import asyncio  # For simulating async operations



# Initialize FastAPI app
app = FastAPI(
    title="Simple FastAPI Demo",
    description="A simple API to demonstrate FastAPI basics",
    version="1.0.0"
)

# Define data model using Pydantic
class Item(BaseModel):
    """Data model for items"""
    name: str
    description: Optional[str] = None
    price: float

# In-memory storage for items
items_db = []

# Unlike regular functions, async functions can be awaited
# and can be used to perform non-blocking I/O operations

# Simulate a slow database operation
async def simulate_db_operation(delay: float = 1.0):
    """Simulate a database operation that takes time"""
    await asyncio.sleep(delay)  # Simulate DB latency
    return items_db

@app.get("/")
async def root():
    """Root endpoint - Welcome message"""
    return {"message": "Welcome to FastAPI Demo!"}

@app.get("/items", response_model=List[Item])
async def get_items():
    """Get all items with simulated DB delay"""
    # This could be a real database query
    items = await simulate_db_operation()
    return items

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID with simulated DB delay"""
    await simulate_db_operation(0.5)  # Shorter delay for single item
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """Create a new item with simulated DB delay"""
    await simulate_db_operation(0.3)  # Simulate write operation
    items_db.append(item)
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """Update an existing item"""
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": f"Item {deleted_item.name} deleted"}

@app.get("/shutdown")
async def shutdown():
    """Shutdown the application gracefully"""
    import sys
    sys.exit(0)