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
    product_name = input("Name of the product: ")
    if product_name in product_inventory:
        print("Product already exists!")
        return

    price = float(input("Price of the product: "))
    quantity = int(input("Quantity of product: "))

    product_inventory[product_name] = {
        "price": price,
        "quantity" : quantity
    }

    print(f"Succesfully added product {product_name} of price {price} and quantity {quantity}.")


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


def update_quantity(product_inventory: dict) -> None:
    product_to_update = input("Product to update: ")

    if product_to_update not in product_inventory:
        print(f"Product {product_to_update} not found.")
        return

    new_quantity = int(input("New quantity: "))

    product_inventory[product_to_update]["quantity"] = new_quantity


# test update_quantity()
"""update_quantity(inventory)
print(inventory)"""


def delete_product(product_inventory: dict) -> None:
    product_to_delete = input("Product to delete: ")
    
    if product_to_delete not in product_inventory:
        print("Product not found.")
        return
    
    verification = input(f"Are you sure you want to permanently delete product {product_to_delete}? y/n: ")
    
    if verification.lower() in ["y", "yes"]: #same as if verification.lower() == "y" or verification.lower() == "yes":
        del product_inventory[product_to_delete]
        print(f"Product {product_to_delete} successfuly deleted.")
        return

    print(f"Product {product_to_delete} was NOT deleted.")


# test delete_product
"""delete_product(inventory)
print(inventory)"""


def show_statistics(product_inventory: dict) -> None:
    if not product_inventory:
        print("Inventory is empty.")
        return

    total_quantity = 0
    most_expensive_price = 0
    most_expensive_name = ""
    
    for product_info in product_inventory.values():
        total_quantity += product_info["quantity"]

    for product_name, product_info in product_inventory.items():
        if most_expensive_price < product_info["price"]:
            most_expensive_price = product_info["price"]
            most_expensive_name = product_name

    print(f"Total products: {len(product_inventory)}")
    print(f"Total quantity: {total_quantity}")
    print(f"Most expensive product: {most_expensive_name} with price of {most_expensive_price}.")
        

"""# test show_statistics()
show_statistics(inventory)"""


def show_all_products(product_inventory: dict) -> None:
    if not product_inventory:
        print("Product inventory is empty.")
        return

    for product_name, product_info in product_inventory.items():
        print()
        print(product_name)
        print(f"Price: {product_info['price']}")
        print(f"Quantity: {product_info['quantity']}")

# test show_all_products()
"""show_all_products(inventory)"""

