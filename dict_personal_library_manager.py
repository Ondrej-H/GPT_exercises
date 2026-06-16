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


def find_book(library: dict, title: str) -> tuple[str, dict] | None:
    for book_name, book_data in library.items():
        if title.lower() == book_name.lower():
            return book_name, book_data

    return None


# test find_book()
"""print(find_book(library, "1984"))"""


def remove_book(library: dict, title_to_remove: str) -> bool:
    for book_name in library.keys():
        if title_to_remove.lower() == book_name.lower():
            del library[book_name]
            return True
    
    return False


# test remove_book
"""remove_book(library, "1984")
print(library)"""


def mark_as_read(library: dict, title_to_mark: str) -> bool:
    for book_name in library:
        if title_to_mark.lower() == book_name.lower():
            library[book_name]["read"] = True
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


def list_books_with_unknown_year(library: dict) -> list[str]:
    books_with_unknown_year = []

    for book_name, book_data in library.items():
        if book_data["year"] is None:
            books_with_unknown_year.append(book_name)

    return books_with_unknown_year


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
        year_input = input("Year: ")

        if not author:
            author = None

        year = int(year_input) if year_input else None

        success = add_book(library, title, author, year)

        if success:
            print(f"Book {title} was successfully added to the library.")
        
        else:
            print(f"Book {title} is already in the library!")


    elif menu_choice == "2":
        print()
        print("Find book")

        book_to_find = input("Book to find: ")
        
        found_book = find_book(library, book_to_find)

        if found_book:
            book_name, book_data = found_book
            print()
            print("Book found:")
            
            print(f"Title: {book_name}")            

            if book_data["author"]:
                print(f"Author: {book_data['author']}")
            else:
                print("Author: Unknown")
            
            if book_data["year"] is None:
                print("Year: Unknown")
            else:
                print(f"Year: {book_data['year']}")
                            
            if book_data["read"]:
                print(f"Read: Book was already read.")
            else:
                print(f"Read: Book is yet to read.")      

        else:
            print(f"Book {book_to_find} was not found in library.")


    elif menu_choice == "3":
        print()
        print("Remove book")
        book_to_remove = input("Book to remove: ")

        confirmation = input(f"Are you sure you want to remove {book_to_remove}? y/n > ")

        if confirmation == "y":
            success = remove_book(library, book_to_remove)

            if success:
                print(f"Book {book_to_remove} was successfully removed.")
            else:
                print("Such book is not in library. No book was removed.")

        else:
            print("Removing book cancelled.")


    elif menu_choice == "4":
        print()
        print("Mark as read")

        book_to_mark_as_read = input("Which book was read? > ")

        success = mark_as_read(library, book_to_mark_as_read)

        if success:
            print(f"Book {book_to_mark_as_read} was marked as read.")

        else:
            print("No such book in the library.")


    elif menu_choice == "5":
        print()
        print("Show all books")

        all_books_list = list_all_books(library)

        if all_books_list:
            for book in all_books_list:
                print(book)

        else:
            print("Library is empty!")


    elif menu_choice == "6":
        print()
        print("Statistics")
        print(f"Total books: {len(library)}")
        print(f"Read books: {count_read_books(library)}")
        print(f"Unread books: {count_unread_books(library)}")
        
        oldest_book = get_oldest_book(library)
        if oldest_book:
            print(f"Oldest book: {oldest_book}")            
        else:
            print("Oldest book: Unknown")

        newest_book = get_newest_book(library)
        if newest_book:
            print(f"Newest book: {newest_book}")
        else:
            print("Newest book: Unknown")

        books_without_year = list_books_with_unknown_year(library)
        if books_without_year:
            print("However, these books were not included because their year is unknown:")
            print(", ".join(books_without_year))

    elif menu_choice == "7":
        print("Good bye!")
        break

'''

'''


"""dict_personal_library_manager: """

