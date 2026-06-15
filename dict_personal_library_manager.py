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


def add_book(
        library: dict,
        title: str,
        author: str | None = None,
        year: int | None = None
        ) -> bool:
    
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


def get_oldest_book(library: dict) -> str | None:
    if not library:
        return None

    oldest_book = None

    for book_name, book_data in library.items():

        if book_data["year"] is None:
            continue
            
        elif oldest_book is None:
            oldest_book = book_name

        elif book_data["year"] < library[oldest_book]["year"]:
            oldest_book = book_name

    return oldest_book


# test get_oldest_book()
"""print(get_oldest_book(library))"""


def get_newest_book(library: dict) -> str | None:
    if not library:
        return None
    
    newest_book = None

    for book_name, book_data in library.items():

        if book_data["year"] is None:
            continue

        elif newest_book is None:
            newest_book = book_name

        elif book_data["year"] > library[newest_book]["year"]:            
            newest_book = book_name

    return newest_book


# test get_newest_book()
"""print(get_newest_book(library))"""


# menu
"""
1 - Add book
2 - Find book
3 - Remove book
4 - Mark as read
5 - Show all books
6 - Show statistics
7 - Exit
"""

while True:

    print("""
1 - Add book
2 - Find book
3 - Remove book
4 - Mark as read
5 - Show all books
6 - Show statistics
7 - Exit
""")

    menu_choice = input("Choose: ")

    if menu_choice == "1":
        print()
        print("Add book")
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year: ")

        add_book(library, title, author, year)

        print(f"Book {title} succesfully added to library.")

    








"""dict_personal_library_manager: Add fn """

