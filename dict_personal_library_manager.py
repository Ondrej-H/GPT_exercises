# PERSONAL LIBRARY MAGER
#  --------------------

# library for testing
library = {
    "1984": {
        "author": "George Orwell",
        "year": 1949,
        "read": True
    },

    "Dune": {
        "author": "Frank Herbert",
        "year": 1965,
        "read": False
    }
}


def add_book(library: dict, title: str, author: str, year: int) -> bool:
    if title in library:
        return False
    
    library[title] = {
        "author": author,
        "year": year,
        "read": False
    }
    return True


# test add_book()
"""add_book(library, "Les Miserables", "Victor Hugo", 1862)
print(library)"""


def find_book(library: dict, title: str) -> dict | None:
    if title in library:
        return library[title]
    
    return None


# test find_book()
"""print(find_book(library, "1984"))"""


def remove_book(library: dict, title: str) -> bool:
    if title in library:
        del library[title]
        return True
    
    return False


# test remove_book
"""remove_book(library, "1984")
print(library)"""


