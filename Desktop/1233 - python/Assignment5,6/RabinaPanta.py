#Name:Rabina Panta
#Student_ID: C0920331

class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True    #Initially all books are available
    
    def borrow_book(self):
        if self.available:
            self.available= False
            return True
        else:
            print(f"The book '{self.title}' is currently not available.") 
            return False
    
    def return_book(self):
        self.available = True
        print(f"Book '{self.title}' has been returned successfully.") 
    
        
    
class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name 
        self.borrowed_books = []
    
    def borrow(self,book):
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")  
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrowed '{book.title}'.")   

#a list to manage all the book objects
library_catalog = []


#Function to add a book to the library 
def add_book():
    title = input("Enter the title of the book:")
    author = input("Enter the name of author of the book:")
    isbn = input("Enter the ISBN of the book:")
    new_book = Book(title,author,isbn) 
    library_catalog.append(new_book)  
    print(f"New book '{title}' by {author} added successfully to the library.")      

#Function to remove a book from library
def remove_book():
    title = input("Enter the title of the book to remove:")
    for book in library_catalog:
        if book.title.lower() == title.lower():
            library_catalog.remove(book)
            print(f"'{book.title}' is removed successfully from the library.") 
        else:
            print(f"'{book.title}' is not in the library.")
user= None   #Initializing user as None initially
#Function to borrow book
def borrow_book():
    global user #Using the global user instance
    title = input("Enter the title of the book to borrow: ")
    for book in library_catalog:
        if book.title.lower() == title.lower():
            if book.available:
                book.borrow_book()
                if user is None:
                    user = User(1,"Raman")  #Creating user instance if it does not exist
                # Assume 'user' is an instance of the User class
                user.borrow(book)
                return
            else:
                print(f"The book '{title}' is currently not available for borrowing.")
                return
#Function to return book
def return_book():
    title = input("Enter the title of the book to return: ")
    for book in user.borrowed_books:
        if book.title.lower() == title.lower():
            user.return_book(book)
            return
        
    print(f"You haven't borrowed '{title}'.")
           
#Function to display menu 
def menu():
    print("Menu:")
    print("1. Add a book")
    print("2.Remove a book")
    print("3.Borrow a book")
    print("4. Return a book")
    print("5.Exit")
while True:
    menu()  
    choice= input("Enter your choice:")
    
    if choice=="1":
        add_book()
    elif choice=="2":
        remove_book()
    elif choice=="3":
        borrow_book()
    elif choice=="4":
        return_book()
    elif choice=="5":
        print("Exiting the library system.")  
        break
    else:
        print("Please enter a valid choice between 1 to 5.")               



                        