# RPG Character Manager
#  -------------------

# sample dict
party = {
    "Conan": {
        "class": "Barbarian",
        "level": 5,
        "hp": 48,
        "inventory": ["Axe", "Potion"],
        "alive": True
    },

    "Merlin": {
        "class": "Wizard",
        "level": 4,
        "hp": 25,
        "inventory": ["Staff", "Scroll"],
        "alive": True
    },

    "Cheddar the Wise": {
        "class": "Master of Cheese",
        "level": 12,
        "hp": 70,
        "inventory": [
            "Legendary Gouda",
            "Cheese Wheel +2",
            "Potion of Lactose Resistance"
        ],
        "alive": True
    }
}

# Core functions (4 functions)

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
        return "not_found"
    
    character_name, _ = found_character
    del party[character_name]
    return "success"
    

