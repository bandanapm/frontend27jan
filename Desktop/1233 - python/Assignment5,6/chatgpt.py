# Bandana Pachabhaiya Magar
# ID: C0916126
import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        if self.available: #Check if the Available status is True
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        else:
            return False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        print("Library Catalog:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")


def save_catalog(library):
    with open("library_catalog.json", "w") as file:
        book_list = [{"title": book.title, "author": book.author, "isbn": book.isbn, "available": book.available}
                     for book in library.books]
        json.dump(book_list, file)


def load_catalog():
    try:
        with open("library_catalog.json", "r") as file:
            book_data = json.load(file)
            library = Library()
            for book_info in book_data:
                book = Book(title=book_info["title"], author=book_info["author"], isbn=book_info["isbn"])
                book.available = book_info["available"]
                library.add_book(book)
            return library
    except FileNotFoundError:
        return Library()


def main():
    library = load_catalog()

    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Choose 1,2,3,4,5 or 6: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            while True:
                isbn = input("Enter the ISBN of the book: ")
                if isbn.isdigit():
                    break
                else:
                    print('input must be an integer')
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            save_catalog(library)
            print(f"Book '{title}' added to the library.")
        elif choice == "3":
            title = input("Enter the title of the book to remove: ")
            for book in library.books:
                if book.title == title:
                    library.remove_book(book)
                    save_catalog(library)
                    print(f"Book '{title}' removed from the library.")
                    break
            else:
                print(f"Book '{title}' not found in the library.")
        elif choice == "4":
            user_name = input("Enter your name: ")
            user_id = input("Enter your user ID: ")
            user = User(user_id, user_name)

            title = input("Enter the title of the book to borrow: ")
            for book in library.books:
                if book.title == title:
                    if user.borrow_book(book):
                        save_catalog(library)
                        print(f"Book '{title}' borrowed successfully.")
                    else:
                        print(f"Book '{title}' is not available for borrowing.")
                    break
            else:
                print(f"Book '{title}' not found in the library.")
        elif choice == "5":
            user_id = input("Enter your user ID: ")
            for user in library.users:
                if user.user_id == user_id:
                    title = input("Enter the title of the book to return: ")
                    for book in user.borrowed_books:
                        if book.title == title:
                            user.return_book(book)
                            save_catalog(library)
                            print(f"Book '{title}' returned successfully.")
                            break
                    else:
                        print(f"Book '{title}' not found in your borrowed books.")
                    break
            else:
                print(f"User with ID '{user_id}' not found.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
