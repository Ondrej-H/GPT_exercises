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

# 1 func add_item()
def add_item(inventory: list) -> None:
    item = input("Enter item: ")
    if item == "":
        print("Invalid item!")
    elif item.lower() in inventory:
        print("Item already exists!")
    else:
        inventory.append(item.lower())
        print(f"Item {item} was added to inventory.")
    

#test add_item()
"""inventory = ["shield"]
add_item(inventory)
print(inventory)"""



# 2 func remove_item()
def remove_item(inventory: list) -> None:
    item_to_remove = input("Enter item to remove: ")
    if item_to_remove not in inventory:
        print("Item not found!")
    else:
        inventory.remove(item_to_remove)
        print(f"Item {item_to_remove} was removed from inventory.")


# test remove_item()
"""lst1 = ["1", "2"]
remove_item(lst1)
print(lst1)"""



# 3 func show_inventory()
def show_inventory(inventory: list) -> None:
    if not inventory:
        print("Inventory is empty!")
    else:
        print()
        print(f"All items: {inventory}")
        print(f"Total items: {len(inventory)}")
        print(f"First 3 items: {inventory[0:3]}")
        print(f"Last 3 items: {inventory[-3:]}")
        print(f"Reversed inventory: {inventory[::-1]}")
        print(f"Every second item: {inventory[::2]}")


# test show_inventory()
"""lst2 = ["1", "2", "3", "4", "5"]
lst3 = []
show_inventory(lst3)"""



# 4 func search_item()
def search_item(inventory: list) -> list:
    searched_text = input("Search: ")
    searched_items = []
    for item in inventory:
        if searched_text in item:
            searched_items.append(item)            #print(item)
    
    print(f"Searched items: {searched_items}")
    return searched_items


# test search_item()
"""lst4 = ["iron sword", "health potion", "magic sword"]
print(search_item(lst4))"""



# 5 func show_statistics() and its functions

# func find_longest()
def find_longest(inventory):
    longest = inventory[0]

    for item in inventory:
        if len(item) > len(longest):
            longest = item
    
    return longest


"""# test find_longest():
lst = ["iron sword", "health potion", "magic sword"]
print(find_longest(lst))"""


# func find_shortest()
def find_shortest(inventory):
    shortest = inventory[0]

    for item in inventory:
        if len(item) < len(shortest):
            shortest = item

    return shortest


# func find_average_length()
def find_average_length(inventory: list) -> float:
    total_length = 0

    for item in inventory:
        total_length += len(item)
    
    average_length = total_length / len(inventory)

    return average_length
        

# func find_items_starting_with_vowel(inventory)
def find_items_starting_with_vowel(inventory) -> list:
    vowels = "aeiou"
    vowels_starting_items = []
    
    for item in inventory:
        if item[0] in vowels:
            vowels_starting_items.append(item)
    
    return vowels_starting_items


# func find_items_containing_spaces(inventory)
def find_items_containing_spaces(inventory):
    containing_spaces = []

    for item in inventory:
        if " " in item:
            containing_spaces.append(item)

    return containing_spaces



# func show_statistics() itself
def show_statistics(inventory):
    if not inventory:
        print("Inventory is empty!")
    else:    
        print(f"Longest item: {find_longest(inventory)}")
        print(f"Shortest item: {find_shortest(inventory)}")
        print(f"Average item length: {find_average_length(inventory)}")
        print(f"Items starting with vowel: {find_items_starting_with_vowel(inventory)}")
        print(f"Items containing spaces: {find_items_containing_spaces(inventory)}")
    


# 6 func clear_duplicates()
def clear_duplicates(inventory):
    new_inventory = []

    for item in inventory:
        if item not in new_inventory:
            new_inventory.append(item)
    
    print("Duplicates removed.")
    return new_inventory


def ask_menu_choice() -> str:
    while True:
        print("""
1 - Add item
2 - Remove item
3 - Show inventory
4 - Search item
5 - Show statistics
6 - Clear duplicates
7 - Exit
""")
        users_choice = input("Choose: ")

        if users_choice in ("1234567"):
            return users_choice
        
        print("Invalid choice!")


# Player inventory manager itself
print()
print("Welcome to Inventory Manager!")

inventory = []

while True:
    users_choice = ask_menu_choice()

    if users_choice == "1":
        add_item(inventory)

    elif users_choice == "2":
        remove_item(inventory)

    elif users_choice == "3":
        show_inventory(inventory)

    elif users_choice == "4":
        search_item(inventory)

    elif users_choice == "5":
        show_statistics(inventory)

    elif users_choice == "6":
        inventory = clear_duplicates(inventory)

    elif users_choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

    

