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

