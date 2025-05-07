import requests

# Base URL for the API
endpoint = "http://127.0.0.1:8000"

def test_can_call_endpoints():
    """Test if the base API endpoint is accessible"""
    response = requests.get(endpoint)
    assert response.status_code == 200

def test_can_add_items():
    """Test the creation of a new item and verify its data
    
    This test:
    1. Creates a new item via POST request
    2. Verifies the creation was successful
    3. Retrieves the created item
    4. Verifies the retrieved item matches the original data
    """
    # Get test data from helper function
    payload = new_item_payload()
    
    # Create new item
    create_item_response = create_item(payload)
    assert create_item_response.status_code == 201
    created_item = create_item_response.json()
    
    # Get all items to find the newly created item's ID
    get_items_response = requests.get(endpoint + "/items")
    items = get_items_response.json()
    item_id = len(items) - 1  # Get the last item's index
    
    # Get the specific item
    get_item_response = get_item(item_id)
    assert get_item_response.status_code == 200
    
    # Verify item data matches what we sent
    get_item_data = get_item_response.json()
    assert get_item_data["name"] == payload["name"]
    assert get_item_data["price"] == payload["price"]

def create_item(payload):
    """Helper function to create an item"""
    return requests.post(endpoint + "/items", json=payload)

def get_item(item_id):
    """Helper function to get an item by ID"""
    return requests.get(endpoint + f"/items/{item_id}")

def update_item(item_id, payload):
    """Helper function to update an item"""
    return requests.put(endpoint + f"/items/{item_id}", json=payload)

def new_item_payload():
    """Helper function that returns a valid item payload"""
    return {
        "name": "futball",
        "description": "game",
        "price": 100
    }