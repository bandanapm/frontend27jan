class book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self): 
        if self.available:  #Check if the Available status is True
            self.available = False
            return True
        else:
            print("Sorry, The book isn't Available")
            return False
        
    def return_book(self):
        if not self.available:
           self.available = True
           print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")
            
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
           book.borrow_book()
           self.borrowed_books.append(book)
           print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} didn't borrow the book : {book.title}")       

class LibrarySystem:
    def __init__(self):
        self.booklist = [] # Creating the list

    def add_book(self, book):   # Adding book to the list
        self.booklist.append(book)
        print(f"'{book.title}' has been added to the Catalog list")

    def remove_book(self, book):    # Removing book from the list
        if book in self.booklist:
            self.booklist.remove(book)
            print(f"Removed '{book.title}' from the Catalog list")
        else:
            print(f"'{book.title}' is not in the Catalog list")

    def display_catalog(self):  # Displaying book from the list
        print("\n Catalog List:")
        if self.booklist:
            items_cat=len(self.booklist)
            print(f"{items_cat} Items in Catalog : ")
            for book in self.booklist:
                if book.available:  # Checking if the availability is True or False
                    status = "Available"
                else:
                    status = "Borrowed"
            print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - '{status}'")
        else:
            print("No any Items in Catalog")
            
library = LibrarySystem()
while True:
    print("\n1. Display catalog list")
    print("2. Add book to catalog")
    print("3. Remove book from catalog")
    print("4. Borrow book")
    print("5. Return book")
    ''' print("6. Display User's Borrowed Books") '''
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        library.display_catalog()

    elif choice == '2':
        title = input("Enter the name of book: ")
        author = input("Enter the author of book: ")
        isbn = input("Enter the ISBN of book: ")
        new_book = book(title, author, isbn)
        library.add_book(new_book)

    elif choice == '3':
        library.display_catalog()
        title_to_remove = input("Enter the Book Name to remove: ")
        book_to_remove = next((book for book in library.booklist if book.title == title_to_remove), None)
        if book_to_remove:
            library.remove_book(book_to_remove)
        else:
            print("Book not found!!.")        

    elif choice == '4':
        library.display_catalog()
        user_name = input("Enter your name: ")
        book_to_borrow = input("Enter the Book Name you want to borrow: ")
        user = User(len(library.booklist), user_name)
        for book in library.booklist:
            if (user.name == user_name and book.title == book_to_borrow):
                user.borrow_book(book)
                break
            else:
               print("Book not found.")    

    elif choice == '5':
        user_name = input("Enter your name: ")
        book_to_return = input("Enter the title of the book you want to return: ")
        for book in user.borrowed_books:
            if (user.name == user_name and book.title == book_to_return):
                user.return_book(book)
                break
            else:
                print("You haven't borrowed this book.")

    elif choice == '6':
        print("Thankyou!! Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")

