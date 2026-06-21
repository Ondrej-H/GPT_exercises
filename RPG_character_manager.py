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
    }
}


def find_character(party: dict, character_to_find: str) -> tuple[str, dict] | None:
    for character in party:

        if character.lower() == character_to_find.lower():

            return character, party[character]
    
    return None

# test find_character
print(find_character(party, "Merlin"))
