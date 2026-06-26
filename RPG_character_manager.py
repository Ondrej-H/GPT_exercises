# RPG Character Manager
#  -------------------

# sample dict
party = {
    "Conan": {
        "class": "Barbarian",
        "level": 12,
        "hp": 48,
        "max_hp": 48,
        "inventory": ["Axe", "Potion"],
        "alive": True
    },

    "Merlin": {
        "class": "Wizard",
        "level": 12,
        "hp": 25,
        "max_hp": 30,
        "inventory": ["Staff", "Scroll"],
        "alive": True
    },

    "Cheddar the Wise": {
        "class": "Master of Cheese",
        "level": 12,
        "hp": 70,
        "max_hp": 99,
        "inventory": [
            "Legendary Gouda",
            "Cheese Wheel +2",
            "Potion of Lactose Resistance"
        ],
        "alive": True
    }
}

group = {}


# Core functions - Character management
"""
find_character()
add_character()
remove_character()
list_all_characters()
show_party()
"""

def find_character(party: dict, character_to_find: str) -> tuple[str, dict] | None:
    for character in party:

        if character.lower() == character_to_find.lower():

            return character, party[character]
    
    return None

# test find_character
"""print(find_character(party, "Merlin"))"""


def add_character(
        party: dict,
        name: str, 
        class_: str,
        level: int,
        hp: int,
        inventory: list[str] | None = None,
        ) -> str:
    
    if name in party:
        return "already_exists"
    
    if inventory is None:
        inventory = []

    party[name] = {
        "class": class_,
        "level": level,
        "hp": hp,
        "max_hp": hp,
        "inventory": inventory,
        "alive": True
    }

    return "success"


# test add_character
"""add_character(party, "Capitain Vegetable", "Brocoli Master", 8, 14)
print(party)"""


def remove_character(party: dict, character_to_remove: str) -> str:
    found_character = find_character(party, character_to_remove)

    if found_character is None:
        return "not_in_party"
    
    character_name, _ = found_character
    del party[character_name]
    return "success"
    

def list_all_characters(party: dict) -> list[str]:
    return list(party)


def show_party(party: dict) -> None:
    for character in party:
        character_data = party[character]
        
        if not character_data["inventory"]:
            inventory_contents = "Empty"
        
        else:
            inventory_contents = ", ".join(character_data["inventory"])
        
        print(f"""
{character}
Class: {character_data["class"]}
Level: {character_data["level"]}
Current HP: {character_data["hp"]}
Max HP: {character_data["max_hp"]}
Inventory: {inventory_contents}
Alive: {character_data["alive"]}
""")
        

# test show_party()
"""show_party(party)"""


# Statistics functions
"""
count_alive_characters()
count_dead_characters()
get_highest_level_characters()
get_lowest_level_characters()
show_statistics()
"""

def count_alive_characters(party: dict) -> int:
    alive_characters = 0
    for character in party:
        if party[character]["alive"]:
            alive_characters += 1

    return alive_characters


# test count_alive_characters()
"""print(count_alive_characters(group))"""


def count_dead_characters(party: dict) -> int:
    dead_characters = 0
    for character in party:
        if not party[character]["alive"]:
            dead_characters += 1

    return dead_characters


def get_highest_level_characters(party: dict) -> list[str]:
    if not party:
        return []

    highest_level = max(character["level"] for character in party.values())
    highest_level_characters = []
    
    for character in party:
        level = party[character]["level"]
        
        if level == highest_level:
            highest_level_characters.append(character)

    return highest_level_characters
    

# test get_highest_level_characters()
"""print(get_highest_level_characters(party))"""


def get_lowest_level_characters(party: dict) -> list[str]:
    if not party:
        return []

    lowest_level = min(character["level"] for character in party.values())
    lowest_level_characters = []
    
    for character in party:
        level = party[character]["level"]
        
        if level == lowest_level:
            lowest_level_characters.append(character)

    return lowest_level_characters


def show_statistics(party: dict):
    print()
    print("Party Statistics")
    print("----------------")
    print(f"Alive characters: {count_alive_characters(party)}")
    print(f"Dead characters: {count_dead_characters(party)}")
    # TODO: Improve UX of character list output.
    print(f"Highest level: {get_highest_level_characters(party)}")
    print(f"Lowest level: {get_lowest_level_characters(party)}")


# test show_statistics
"""show_statistics(party)"""

# HP management functions
"""
damage_character()
heal_character()
kill_character()
revive_character()
"""

def damage_character(party: dict, character: str, damage: int) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    if not character_data["alive"]:
        return "already_dead"
    
    character_data["hp"] -= damage
    
    if character_data["hp"] <= 0:
        character_data["hp"] = 0
        character_data["alive"] = False

    return "success"


def heal_character(party: dict, character: str, heal: int) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    if not character_data["alive"]:
        return "already_dead"
    
    if character_data["hp"] + heal <= character_data["max_hp"]:
        character_data["hp"] += heal

    else:
        character_data["hp"] = character_data["max_hp"]

    return "success"


def kill_character(party: dict, character: str) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    if not character_data["alive"]:
        return "already_dead"
    
    character_data["hp"] = 0
    character_data["alive"] = False
    
    return "success"


def revive_character(party: dict, character: str) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    if character_data["alive"]:
        return "already_alive"
    
    character_data["hp"] = 1
    character_data["alive"] = True

    return "success"


# Level management functions
"""
level_up_character()
level_down_character()
"""

def level_up_character(party: dict, character: str) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    character_data["level"] += 1

    return "success"


def level_down_character(party: dict, character: str) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    if character_data["level"] == 1:
        return "already_level_1"
    
    character_data["level"] -= 1

    return "success"


# Inventory management functions
"""
add_item()
remove_item()
show_inventory()
"""

def add_item(party: dict, character: str, item: str) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    character_data["inventory"].append(item)
    return "success"

# test add_item()
"""print(add_item(party, "conan", "great sword"))
print(party)"""


def remove_item(party: dict, character: str, item: str) -> str:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    _, character_data = found_character

    if item not in character_data["inventory"]:
        return "not_in_inventory"

    character_data["inventory"].remove(item)

    return "success"


def show_inventory(party: dict, character: str) -> str | None:
    found_character = find_character(party, character)

    if found_character is None:
        return "not_in_party"
    
    character_name, character_data = found_character

    if not character_data["inventory"]:
        return "inventory_empty"

    print(f"{character_name}'s inventory:")
    for item in character_data["inventory"]:
        print(item)

# test show_inventory()
"""show_inventory(party, "conan")"""


# User input helper functions
def ask_positive_int(subject: str) -> int:
    while True:
        print()
        user_input = input(f"{subject} (positive whole number, Enter = 1): ")
        if user_input == "":
            user_input = 1
            print(f"{subject} was set to 1")
            return user_input

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input >= 1:
                print(f"{subject} was successfully set to {user_input}.")
                return user_input

            else:
                print("Invalid input! Input must be positive whole number!")

        else:
            print("Invalid input! Input must be positive whole number!")


# test ask_positive_int
"""print(ask_positive_int("HP"))"""


def ask_new_character_name(party: dict) -> str:
    while True:
        name = input("Name: ")

        found_character = find_character(party, name)

        if found_character:
            character_name, _ = found_character
            print(f"Character called {character_name} is already in party! Try another name.")

        else:
            return name
        

# test ask_new_character_name()
"""print(ask_new_character_name(party))"""
        

def ask_inventory() -> list[str] | None:
    inventory = input("Inventory (separate items with ', '): ")

    if not inventory:
            inventory = None
    else:
        inventory = inventory.split(sep=", ")

    return inventory


# Main menu
"""
Main Menu
---------
1 Add character
2 Remove character
3 Show party
4 Statistics

5 Damage character
6 Heal character
7 Kill character
8 Revive character

9 Level up character
10 Level down character

11 Add item
12 Remove item
13 Show inventory

0 Exit
"""

while True:
    print("""
    Main Menu
    ---------
    1 Add character
    2 Remove character
    3 Show party
    4 Statistics
    5 Damage character
    6 Heal character
    7 Kill character
    8 Revive character
    9 Level up character
    10 Level down character
    11 Add item
    12 Remove item
    13 Show inventory
    0 Exit
    """)

    menu_choice = input("Choose: ")

    if menu_choice == "1":
        print()
        print("Add character")

        name = ask_new_character_name(party)
        class_ = input("Class: ")
        level = ask_positive_int("Level")
        hp = ask_positive_int("HP")
        inventory = ask_inventory()

        result = add_character(party, name, class_, level, hp, inventory)

        if result == "success":
            print(f"Character {name} was successfully added.")

        # just defence code:
        elif result == "already_exists":
            print(f"Character called {name} is already in party.")


    elif menu_choice == "2":
        print()
        print("Remove character")

        character_to_remove = input("Character to remove: ")

        result = remove_character(party, character_to_remove)

        if result == "not_in_party":
            print(f"There is no character called {character_to_remove} in the party.")

        else:
            print(f"Character {character_to_remove} was succesfully removed.")
        

    elif menu_choice == "3":
        print()
        print("Show party")

        show_party(party)
        print("Scroll up ↑")

    
    elif menu_choice == "4":
        show_statistics(party)





    elif menu_choice == "0":
        print("Good bye!")
        break


    