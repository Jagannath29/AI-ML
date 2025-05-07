import requests

def add_item():
    """Interactive function to get item details from user and add to the API"""
    print("\n=== Add New Item ===")
    
    # Get item details from user
    name = input("Enter item name: ").strip()
    while not name:
        print("Name cannot be empty!")
        name = input("Enter item name: ").strip()
    
    description = input("Enter item description (optional, press Enter to skip): ").strip()
    if not description:
        description = None
    
    while True:
        try:
            price = float(input("Enter item price: "))
            if price <= 0:
                print("Price must be greater than 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Prepare item data
    item_data = {
        "name": name,
        "description": description,
        "price": price
    }
    
    # Send request to API
    try:
        response = requests.post("http://localhost:8000/items", json=item_data)
        if response.status_code == 201:
            print("\nSuccess! Item added:")
            item = response.json()
            print(f"Name: {item['name']}")
            print(f"Description: {item['description']}")
            print(f"Price: ${item['price']:.2f}")
            return True
        else:
            print(f"\nError: Failed to add item. Status code: {response.status_code}")
            print(f"Details: {response.json()}")
            return False
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server. Make sure the FastAPI server is running!")
        return False

def main():
    print("Welcome to Item Manager!")
    print("Make sure the FastAPI server is running (uvicorn main:app --reload)")
    
    while True:
        try:
            add_item()
            
            choice = input("\nWould you like to add another item? (y/n): ").lower()
            if choice != 'y':
                break
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()