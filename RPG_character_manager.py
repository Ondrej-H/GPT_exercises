# RPG Character Manager
#  -------------------

# sample dict
party = {
    "Conan": {
        "class": "Barbarian",
        "level": 12,
        "hp": 48,
        "inventory": ["Axe", "Potion"],
        "alive": True
    },

    "Merlin": {
        "class": "Wizard",
        "level": 12,
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

group = {}


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
HP: {character_data["hp"]}
Inventory: {inventory_contents}
Alive: {character_data["alive"]}
""")
        

# test show_party()
"""show_party(party)"""


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
print(get_highest_level_characters(party))

