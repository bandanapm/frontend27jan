import json

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def borrow_book(self):
        if self.available:
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
        self.borrowed_book_user = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_book_user.append(book)
            return True
        else:
            return False
        
    def return_book(self, book):
        if book.return_book():
            self.borrowed_book_user.remove(book)
            return True 
        else:
            return False
        
class Library:
    def __init__(self):
        self.books_library = []

    def add_book(self, book):
        self.books_library.append(book)

    def remove_book(self, book):
        self.books_library.remove(book)
    
    def display_books(self):
        print("List of books contain in a library.")
        for book in self.books_library:
            status = "Available" if book.available else "Not Available"
            print(f"{book.title}, {book.author}, {book.ISBN} - {status}")

def create_file(library):
    with open("library.txt","w") as afile:
        list_of_books = [{"title": book.title, "author": book.author, "isbn": book.ISBN, "available": book.available}
                     for book in library.books]
        json.dump(list_of_books, afile)

def load_file():
    try:
        with open("library.txt","r") as afile:
            library_book_data = json.load(afile)
            library = Library()
            for book_info in library_book_data:
                book = Book(title=book_info["title"], author=book_info["author"], isbn=book_info["isbn"])
                book.available = book_info["availabile"]
                library.add_book(book)
            return library
    except FileNotFoundError:
        return Library()


def main():
    library = load_file()

    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            create_file(library)
            print(f"Book '{title}' added to the library.")
        elif choice == "3":
            title = input("Enter the title of the book to remove: ")
            for book in library.books:
                if book.title == title:
                    library.remove_book(book)
                    create_file(library)
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
                        create_file(library)
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
                            create_file(library)
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

main()
