# PRODUCT INVENTORY MANAGER
#  -----------------------

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