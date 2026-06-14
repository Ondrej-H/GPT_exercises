# PERSONAL LIBRARY MANAGER
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


def mark_as_read(library: dict, title: str) -> bool:
    if title in library:
        library[title]["read"] = True
        return True
    
    return False


# test mark_as_read()
"""mark_as_read(library, "Dune")
print(library)"""


def list_all_books(library: dict) -> list[str]:
    return list(library)
    # same as:
    """all_books = []
    for title in library.keys():
        all_books.append(title)
    
    return all_books"""


# test list_all_books()
"""print(list_all_books(library))"""


def count_read_books(library: dict) -> int:
    num_read_books = 0

    for book_data in library.values():
        if book_data["read"]:
            num_read_books += 1

    return num_read_books


# test count_read_books()
"""print(count_read_books(library))"""


def count_unread_books(library: dict) -> int:
    num_unread_books = 0

    for book_data in library.values():
        if not book_data["read"]:
            num_unread_books += 1
    
    return num_unread_books


# test count_unread_books()
"""print(count_unread_books(library))"""

""""dict_personal_library_manager: Add fn """

