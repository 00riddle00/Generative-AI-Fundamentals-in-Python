# =============================================================================
# Food Ordering Application
# =============================================================================

# Global variables and constants
app_name = "Gourmet Express"

menu = {
    "sku1": {"name": "Hamburger", "price": 6.51},
    "sku2": {"name": "Cheeseburger", "price": 7.75},
    "sku3": {"name": "Milkshake", "price": 5.99},
    "sku4": {"name": "Fries", "price": 2.39},
    "sku5": {"name": "Sub", "price": 5.87},
    "sku6": {"name": "Ice Cream", "price": 1.55},
    "sku7": {"name": "Fountain Drink", "price": 3.45},
    "sku8": {"name": "Cookie", "price": 3.15},
    "sku9": {"name": "Brownie", "price": 2.46},
    "sku10": {"name": "Sauce", "price": 0.75},
}

actions = {
    1: "Add a new menu item to cart",
    2: "Remove an item from the cart",
    3: "Modify a cart item's quantity",
    4: "View cart",
    5: "Checkout",
    6: "Exit",
}

sales_tax_rate = 0.07  # 7% sales tax

cart = {}


# Display the menu
def display_menu():
    print("\n**** Menu ****\n")
    for sku in menu:
        sku_number = sku[3:]
        item_name = menu[sku]["name"]
        item_price = menu[sku]["price"]
        print(f"({sku_number}) {item_name}: ${item_price:.2f}")


# Add an SKU and quantity to the cart
def add_to_cart(sku, quantity):
    if sku in menu:
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
        print(f"\nAdded {quantity} of {menu[sku]['name']} to the cart.\n")
    else:
        print("\nError: Invalid menu item SKU.\n")


# Remove an SKU from the cart
def remove_from_cart(sku):
    if sku in cart:
        removed_item = cart.pop(sku)
        print(f"\nRemoved {menu[sku]['name']} from the cart.\n")
    else:
        print("\nError: Item not found in the cart.\n")


# Modify the quantity of an SKU in the cart
def modify_cart(sku, quantity):
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print(
                f"\nModified {menu[sku]['name']} quantity to {quantity} in the cart.\n"
            )
        else:
            remove_from_cart(sku)
    else:
        print("\nError: Item not found in the cart.\n")


# Display the cart contents
def view_cart():
    print("\n**** Cart Contents ****\n")
    subtotal = 0.0
    for sku in cart:
        if sku in menu:
            quantity = cart[sku]
            item_total = menu[sku]["price"] * quantity
            subtotal += item_total
            print(f"{quantity} x {menu[sku]['name']}")
    tax = subtotal * sales_tax_rate
    total = subtotal + tax
    print(f"\nTotal: ${total:.2f}\n")


# Perform the checkout
def checkout():
    print("\n**** Checkout ****\n")
    view_cart()
    print("Thank you! Your order has been received and is being processed.")


# Get SKU and quantity
def get_sku_and_quantity(sku_prompt, quantity_prompt=None):
    sku_input = input(sku_prompt)
    sku = "sku" + sku_input

    if quantity_prompt is not None:
        quantity_input = input(quantity_prompt)
        if quantity_input.isdigit():
            quantity = int(quantity_input)
        else:
            quantity = 1  # Default value if not a valid digit

        return sku, quantity

    return sku


# Run the app loop
def run_ordering_app():
    print(f"Welcome to {app_name}!")

    app_running = True

    while app_running:
        print("\n**** Ordering Actions ****\n")
        for action_number, action_description in actions.items():
            print(f"({action_number}) {action_description}")

        user_input = input("\nPlease enter the number of the action you want to take: ")

        if user_input == "1":
            display_menu()
            sku, quantity = get_sku_and_quantity(
                "Please enter the SKU number for the menu item you want to order: ",
                "Please enter the quantity: ",
            )
            add_to_cart(sku, quantity)

        elif user_input == "2":
            display_menu()
            sku = get_sku_and_quantity(
                "Please enter the SKU number for the menu item you want to remove: "
            )
            remove_from_cart(sku)

        elif user_input == "3":
            display_menu()
            sku, quantity = get_sku_and_quantity(
                "Please enter the SKU number for the menu item you want to modify: ",
                "Please enter the new quantity: ",
            )
            modify_cart(sku, quantity)

        elif user_input == "4":
            view_cart()

        elif user_input == "5":
            checkout()
            app_running = False

        elif user_input == "6":
            app_running = False

        else:
            print("\nError: Invalid action. Please enter a number from 1 to 6.")


# Start the application
run_ordering_app()
