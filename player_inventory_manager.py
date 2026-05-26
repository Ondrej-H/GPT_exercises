# PLAYER INVENTORY MANAGER
# ------------------------

"""
1 - Add item
2 - Remove item
3 - Show inventory
4 - Search item
5 - Show statistics
6 - Clear duplicates
7 - Exit
Choose:
"""

# func add_item()
def add_item(inventory):
    item = input("Enter item: ")
    if item == "":
        print("Invalid item!")
    elif item.lower() in inventory:
        print("Item already exists!")
    else:
        inventory.append(item.lower())
    

#test add_item():
"""inventory = ["shield"]
add_item(inventory)
print(inventory)"""



# func remove_item ()
def remove_item(inventory: list) -> None:
    item_to_remove = input("Enter item to remove: ")
    inventory.remove(item_to_remove)

# test remove_item():
lst1 = ["1", "2"]
remove_item(lst1)
print(lst1)

# func show_inventory()

# func search_item()

# func show_statistics()

# func clear_duplicates()