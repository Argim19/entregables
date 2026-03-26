# Request product name and text-only verification

while True:
    name = input("enter the name:")
    if name.replace(" ", "").isalpha():
        break
    else:
        print("Please enter a valid name")

# Request the price and  verify that only numbers are entered

while True:
    try:
        price = float(input("enter the price:"))
        if price <= 0:
            print("Value must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Request the quantity and  verify that only numbers are entered

while True:
    try:
        quantity = int(input("enter the quantity:"))
        if quantity <= 0:
            print("Value must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Calculate total cost

total_cost = price * quantity

# Display the results in a readable format

print("Product Name:", name)
print("Unit Price: $", price)
print("Quantity:", quantity)
print("Total Cost: $", total_cost)


# This program collects information about a product from the user, including its name,
# price, and quantity. It validates each input to ensure correct data types and positive values.
# Once valid data is entered, it calculates the total cost and displays a summary of the product.
