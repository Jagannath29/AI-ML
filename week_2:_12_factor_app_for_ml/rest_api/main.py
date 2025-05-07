# Import required modules from FastAPI framework
from fastapi import FastAPI, HTTPException, status
# Import Pydantic for data validation
from pydantic import BaseModel, Field
# Import typing modules for type hints
from typing import List, Optional
# Import asyncio for handling asynchronous operations
import asyncio

# Create FastAPI application instance with metadata
app = FastAPI(
    title="Simple FastAPI Demo",  # Set API title
    description="A simple API to demonstrate FastAPI basics",  # API description
    version="1.0.0"  # API version number
)

# Define Item model for data validation and serialization
class Item(BaseModel):
    """Data model for items"""
    name: str = Field(..., min_length=1)  # Name field with minimum length validation
    description: Optional[str] = None  # Optional description field
    price: float = Field(..., gt=0)  # Price field with positive number validation

# Initialize empty list to store items (simulating database)
items_db = []

# Define async function to simulate database operations
async def simulate_db_operation(delay: float = 1.0):
    """Simulate a database operation that takes time"""
    await asyncio.sleep(delay)  # Add artificial delay to simulate DB latency
    return items_db  # Return the items list

# Root endpoint definition
@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    """Root endpoint that returns API information"""
    return {
        "message": "Welcome to FastAPI Demo!",  # Welcome message
        "version": "1.0.0",  # API version
        "status": "healthy"  # API health status
    }

# Get all items endpoint
@app.get("/items", response_model=List[Item], status_code=status.HTTP_200_OK)
async def get_items():
    """Retrieve all items from the database"""
    items = await simulate_db_operation()  # Simulate DB read operation
    return items  # Return all items

# Get single item endpoint
@app.get("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def get_item(item_id: int):
    """Retrieve a specific item by its ID"""
    try:
        await simulate_db_operation(0.5)  # Simulate DB read operation
        if item_id < 0:  # Validate item_id is not negative
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Item ID cannot be negative"
            )
        return items_db[item_id]  # Return the requested item
    except IndexError:  # Handle case when item doesn't exist
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

# Create new item endpoint
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """Create a new item in the database"""
    await simulate_db_operation(0.3)  # Simulate DB write operation
    items_db.append(item)  # Add new item to database
    return item  # Return created item

# Update existing item endpoint
@app.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_item(item_id: int, item: Item):
    """Update an existing item by its ID"""
    try:
        if item_id < 0:  # Validate item_id is not negative
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Item ID cannot be negative"
            )
        items_db[item_id] = item  # Update item in database
        return item  # Return updated item
    except IndexError:  # Handle case when item doesn't exist
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

# Delete item endpoint
@app.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
async def delete_item(item_id: int):
    """Delete an item from the database by its ID"""
    try:
        if item_id < 0:  # Validate item_id is not negative
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Item ID cannot be negative"
            )
        deleted_item = items_db.pop(item_id)  # Remove and get deleted item
        return {"message": f"Item {deleted_item.name} deleted", "status": "success"}  # Return success message
    except IndexError:  # Handle case when item doesn't exist
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

# Shutdown endpoint
@app.get("/shutdown")
async def shutdown():
    """Endpoint to gracefully shutdown the application"""
    import sys  # Import sys module for system operations
    sys.exit(0)  # Exit the application with success status