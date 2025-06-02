# Restaurant Management System

# empty menu
menu = []
# empty orders
orders = []

menu_id_counter = 1
order_id_counter = 1

def add_menu_item(name, price):
    """Add a new item to the menu."""
    global menu_id_counter
    item = {
        'id': menu_id_counter,
        'name': name,
        'price': price
    }
    menu.append(item)
    menu_id_counter += 1
    print(f"Added {name} to the menu with ID {item['id']}.")

def view_menu():
    """Display the current menu."""
    if not menu:
        print("The menu is currently empty.")
        return
    print("Current Menu:")
    for item in menu:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']:.2f}")

def place_order(item_id, quantity):
    """Place an order for a menu item."""
    global order_id_counter
    item = next((item for item in menu if item['id'] == item_id), None)
    if not item:
        print(f"Item with ID {item_id} not found in the menu.")
        return
    order = {
        'id': order_id_counter,
        'item': item,
        'quantity': quantity,
        'total_price': item['price'] * quantity
    }
    orders.append(order)
    order_id_counter += 1
    print(f"Order placed: {quantity} x {item['name']} (ID: {order['id']}) - Total: ${order['total_price']:.2f}")

def view_orders():
    """Display all current orders."""
    if not orders:
        print("No current orders.")
        return
    print("Current Orders:")
    for order in orders:
        print(f"Order ID: {order['id']}, Item: {order['item']['name']}, Quantity: {order['quantity']}, Total Price: ${order['total_price']:.2f}")


# main function to run the restaurant management system
def restaurant_management_system():
    """Run the restaurant management system."""
    print("Welcome to the Restaurant Management System!")
    
    while True:
        print("\nMenu:")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            add_menu_item(name, price)
        elif choice == '2':
            view_menu()
        elif choice == '3':
            item_id = int(input("Enter item ID to order: "))
            quantity = int(input("Enter quantity: "))
            place_order(item_id, quantity)
        elif choice == '4':
            view_orders()
        elif choice == '5':
            print("Exiting the Restaurant Management System. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    restaurant_management_system()