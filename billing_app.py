

from database import database
from barcode_reader import read_barcode

def calculate_total_price(cart):
    total_price = sum(database[item]["price"] for item in cart)
    return total_price

def main():
    # Initialize an empty cart
    cart = []

    # Read 5 items
    for _ in range(5):
        barcode_data = read_barcode()

        # Check if the item is in the database
        if barcode_data in database:
            item_name = database[barcode_data]["name"]
            item_price = database[barcode_data]["price"]
            print(f"Item: {item_name}, Price: ${item_price}")
            cart.append(barcode_data)
        else:
            print("Item not found in the database. Try again.")

    # Calculate and display the total price
    total_price = calculate_total_price(cart)
    print(f"\nTotal Price for 5 items: ${total_price}")

if __name__ == "__main__":
    main()
