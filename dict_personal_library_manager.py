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

