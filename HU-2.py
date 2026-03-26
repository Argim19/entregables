# List to store products
inventory = []


# Function to add a product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    product = {"name": name, "price": price, "quantity": quantity}

    inventory.append(product)
    print("Product added successfully.")


# Function to show inventory
def show_inventory():
    if len(inventory) == 0:
        print("The inventory is empty.")
    else:
        for product in inventory:
            print(
                "Product:",
                product["name"],
                "| Price:",
                product["price"],
                "| Quantity:",
                product["quantity"],
            )


# Function to calculate statistics
def calculate_statistics():
    total_value = 0
    total_products = 0

    for product in inventory:
        total_value = total_value + (product["price"] * product["quantity"])
        total_products = total_products + product["quantity"]

    print("Total inventory value:", total_value)
    print("Total quantity of products:", total_products)


# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":
        add_product()
    elif option == "2":
        show_inventory()
    elif option == "3":
        calculate_statistics()
    elif option == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Try again.")

# This program allows the user to add products to an inventory,
# display them, and calculate basic statistics such as total value
# and total quantity of products.
