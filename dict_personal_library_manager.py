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

def find_book(library: dict, title: str) -> tuple[str, dict] | None:
    for book_name, book_data in library.items():
        if title.lower() == book_name.lower():
            return book_name, book_data

    return None


# test find_book()
"""print(find_book(library, "1984"))"""


def add_book(
        library: dict,
        title_to_add: str,
        author: str | None = None,
        year: int | None = None
        ) -> str:
    
    found_book = find_book(library, title_to_add)

    if found_book:
        return "already_exists"
    
    library[title_to_add] = {
        "author": author,
        "year": year,
        "read": False
    }
    return "success"


# test add_book()
"""add_book(library, "Les Miserables", "Victor Hugo", 1862)
print(library)"""


def remove_book(library: dict, title_to_remove: str) -> str:
    found_book = find_book(library, title_to_remove)
    if found_book is None:
        return "not_found"

    book_name, _ = found_book   # _ means the second value exists, but I don't need it
    del library[book_name]
    return "success"



# test remove_book
"""remove_book(library, "1984")
print(library)"""


def mark_as_read(library: dict, title_to_change: str) -> str:
    found_book = find_book(library, title_to_change)
    
    if not found_book:
        return "not_found"

    _, book_data = found_book

    if book_data["read"]:
        return "already_read"
    
    book_data["read"] = True
    return "success"


# test mark_as_read()
"""mark_as_read(library, "Dune")
print(library)"""


def mark_as_unread(library: dict, title_to_change: str) -> str:
    found_book = find_book(library, title_to_change)
    
    if not found_book:
        return "not_found"

    _, book_data = found_book

    if not book_data["read"]:
        return "already_unread"
    
    book_data["read"] = False
    return "success"


# test mark_as_read()
"""mark_as_unread(library, "1984")
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


def rename_book(
        library: dict,
        book_to_rename: str,
        new_book_name: str
        ) -> str:
    found_book = find_book(library, book_to_rename)

    if found_book is not None:
        if new_book_name not in library:
            book_name, book_data = found_book
            library[new_book_name] = book_data
            del library[book_name]

            return "success"
        
        else:
            return "already_exists"
        
    return "not_found"


# test rename_book()
"""rename_book(library, "1984", "Dune")
print(library)"""


def change_author(
        library: dict,
        book_to_change: str,
        new_author: str
) -> str:
    found_book = find_book(library, book_to_change)

    if found_book is None:
        return "not_found"
    
    if not new_author:
        return "empty"

    _, book_data = found_book
    book_data["author"] = new_author

    return "success"
   

# test change_author()
"""change_author(library, "1984", "")
print(library)"""


def change_year(
        library: dict,
        book_to_change: str,
        new_year: int
) -> str:
    found_book = find_book(library, book_to_change)

    if found_book is None:
        return "not_found"
    
    _, book_data = found_book
    book_data["year"] = new_year

    return "success"


def remove_year(library: dict, book_to_change: str) -> str:
    found_book = find_book(library, book_to_change)

    if found_book is None:
        return "not_found"
    
    _, book_data = found_book
    if book_data["year"] is None:
        return "empty"
    
    book_data["year"] = None
    return "success"


# menu
"""
1 - Add book
2 - Find book
3 - Remove book
4 - Show all books
5 - Show statistics
6 - Edit book
7 - Exit
"""

while True:

    print("""
1 - Add book
2 - Find book
3 - Remove book
4 - Show all books
5 - Show statistics
6 - Edit book
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

        result = add_book(library, title, author, year)

        if result == "success":
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
        found_book = find_book(library, book_to_remove)

        if confirmation == "y":
            result = remove_book(library, book_to_remove)            
            
            if result == "success":
                book_name, _ = found_book
                print(f"Book {book_name} was successfully removed.")
            else:
                print("Such book is not in library. No book was removed.")

        else:
            print("Removing book cancelled.")         


    elif menu_choice == "4":
        print()
        print("Show all books")

        all_books_list = list_all_books(library)

        if all_books_list:
            for book in all_books_list:
                print(book)

        else:
            print("Library is empty!")


    elif menu_choice == "5":
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


    elif menu_choice == "6":
        while True:
            print("""
Edit book menu:
1 - Rename book
2 - Change author
3 - Change year
4 - Remove year
5 - Mark as read
6 - Mark as unread
7 - Back
""")
            edit_choice = input("Choose: ")

            if edit_choice == "1":
                print()
                print("Rename book")
                book_to_rename = input("Book to rename: ")
                found_book = find_book(library, book_to_rename)
                
                if found_book:
                    new_name = input("New name: ")

                    result = rename_book(library, book_to_rename, new_name)

                    if result == "success":
                        print(f"Book {book_to_rename} was successfully renamed to {new_name}.")
                    elif result == "already_exists":
                        print(f"A book named {new_name} already exists in the library! Try another name.")
                else:
                    if book_to_rename == "":
                        print("Invalid name, renaming aborted.")
                    else:
                        print(f"Book {book_to_rename} is not in the library.")

            
            elif edit_choice == "7":
                break



    elif menu_choice == "7":
        print("Good bye!")
        break

"""
new menu:
1 - Add book
2 - Find book
3 - Remove book
4 - Show all books
5 - Show statistics
6 - Edit book
7 - Exit
"""

"""
Edit book menu:
1 - Rename book
2 - Change author
3 - Change year
4 - Remove year
5 - Mark as read
6 - Mark as unread
7 - Back
"""

"""
elif menu_choice == :
        print()
        print("Mark as read")

        book_to_mark_as_read = input("Which book was read? > ")
        result = mark_as_read(library, book_to_mark_as_read)
        
        if result == "not_found":
            print("No such book in the library.")        
        
        else:
            book_name, _ = find_book(library, book_to_mark_as_read)

            if result == "already_read":            
                print(f"Book {book_name} is already marked as read!")

            else:
                print(f"Book {book_name} was marked as read.")
"""

"""dict_personal_library_manager: """

