# Bandana Pachabhaiya Magar
# ID: C0916126

class Book:   #Book class created
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available   

    def borrow_book(self):
        if self.available:   #Check if the Available status is True
            self.available == False
            return True
        else:
            return False
        
    def return_book(self):
        self.available == True


class User:      #USer class created
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,book):  #borrow books by the user
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            return True
        else:
            return False
        
    def return_book(self,book_index):   #return books by the user
        if 0 <= book_index < len(self.borrowed_books):
            book = self.borrowed_books[book_index]
            book.available = True 
            del self.borrowed_books[book_index]
            print("Book returned successfully.")
            return True
        else:
            print("Invalid book.")
            return False


# initial library books value to show the display part if user select 1 at the begining.
library_books = [
    Book('The Great', 'Bandana', 1),
    Book('Mockingbird', 'Magar', 2),
    Book('2000', 'New', 3)
]


# add book to the list of library system.
def add_book():
    title = input("Enter the title of the book:")
    author = input("Enter the author name:")
    while True:
        isbn = input("Enter the ISBN of the book: ")
        if isbn.isdigit():
            break
        else:
            print('input must be an integer')
    new_book = Book(title,author,isbn) 
    library_books.append(new_book)  
    print(f"'{title}'is added successfully to the library.")         

# remove book from list of library system.
def remove_book():
    title = input("Enter the title of the book that you would like to remove: ")
    for book in library_books:
        if book.title.lower() == title.lower():   #comparing the title that the user enter and from the library book list
            library_books.remove(book)
            print(f"'{book.title}' is removed successfully.") 
    else:
        print(f"Book named'{book.title}' is not found.")

# display book from list of library system.
def display_books():
    print("List of books in a library:")
    for book in library_books:
        status = "Available" if book.available else "Not Available"
        print(f"(Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}) - {status}")


# borrow books from list of library system.
def borrow_books():
    user_name = input("Enter your name: ")
    user_id = input("Enter your user ID: ")
    user = User(user_id, user_name)

    title = input("Enter the title of the book to borrow: ")
    for book in library_books:
        if book.title == title:
            if user.borrow_book(book):
                print(f"Book '{title}' borrowed successfully.")
            else:
                print(f"Book '{title}' is not available for borrowing.")
            break
    else:
        print(f"Book '{title}' not found in the library.")
  
user_list = [
    User('1', 'Alice'),
    User('2', 'Bob'),
]

# returning book to the list of library system.
def return_books():
    user_id = input("Enter your user ID: ").strip().lower()
    for user in user_list:
        if user.user_id.lower() == user_id:
            if not user.borrowed_books:
                print("You have no borrowed books.")
                return  # Exit the function if there are no borrowed books
            print("Borrowed Books:")
            for i, book in enumerate(user.borrowed_books):
                print(f"{i+1}.{book.title}")
            try:
                book_index = int(input("Enter book index:"))
                if user.return_book(book_index):
                    return
                else:
                    return
            except ValueError:
                print("Invalid input")
                return
    else:
        print(f"User with ID '{user_id}' not found.")

def main():
    while True:
        print("\n--Library Management System--")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Choose 1,2,3,4,5 or 6: ")

        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            borrow_books()
        elif choice == "5":
            return_books()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()