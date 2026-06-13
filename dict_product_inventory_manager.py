# PRODUCT INVENTORY MANAGER
#  -----------------------

# product inventory for testing
inventory = {
    "apple": {
        "price": 25,
        "quantity": 10
    },
    "banana": {
        "price": 30,
        "quantity": 5
    }
}

def show_menu():
    print("""
1 - Add product
2 - View product
3 - Update quantity
4 - Delete product
5 - Show statistics
6 - Show all products
7 - Exit
""")
    

def add_product(product_inventory: dict) -> None:
    product = input("Name of the product: ")
    if product in product_inventory:
        print("Product already exists!")
        return

    price = float(input("Price of the product: "))
    quantity = int(input("Quantity of product: "))

    product_inventory[product] = {
        "price": price,
        "quantity" : quantity
    }

    print(f"Succesfully added product {product} of price {price} and quantity {quantity}.")


# test add_product
"""product_inventory = {}
add_product(product_inventory)
print(product_inventory)"""


def view_product(product_inventory: dict) -> None:
    product_to_view = input("Name of the product to view: ")

    product_info = product_inventory.get(product_to_view)

    if product_info is None:
        print("Product not found.")
        return
    
    print(f"Name of the product: {product_to_view}")
    print(f"Price: {product_info['price']}")
    print(f"Quantity: {product_info['quantity']}")


# test view_product()
"""view_product(inventory)"""

