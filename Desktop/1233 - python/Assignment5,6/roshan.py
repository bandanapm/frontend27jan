class ModelBook:
    """
    A book in a library is represented by the ModelBook class.
    It includes information on the book's ID, title, and author.
    """

    def __init__(self, book_id, book_title, book_author):
        """
        Initialises a new instance of the ModelBook class. 
        :param book_id: The ID of the book. 
        :param book_title: The title of the book. 
        :param book_author: The author of the book.
        """
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author


class ModelLibrary:
    """
    A library is represented by the ModelLibrary class.
    It includes a dictionary of books, where the key is the book's ID and the value is a ModelBook instance.
    """

    def __init__(self):
        """
        Initializes a new instance of the ModelLibrary class.
        """
        self.book_list = {}

    def add_new_book(self, book_title, book_author, book_id):
        """
        Adds a new book to the library.
        :param book_title: The title of the new book.
        :param book_author: The author of the new book.
        :param book_id: The ID of the new book.
        """
        if book_id in self.book_list:
            print(f"Book ID {book_id} already exists. Cannot add book.")
            return

        new_book = ModelBook(book_id, book_title, book_author)
        self.book_list[book_id] = new_book
        print(f"Book '{book_title}' has been added successfully.")

    def remove_book(self, book_id):
        """
        Removes a book from the library.
        :param book_id: The ID of the book to be removed.
        """
        if book_id not in self.book_list:
            print(f"No book found with ID {book_id}.")
            return

        removed_book = self.book_list.pop(book_id)
        print(
            f"Book '{removed_book.book_title}' has been removed successfully.")



def main():
    """
    The main function that runs the library management system.
    """
    '''Create instance of the ModelLibrary class'''
    lib = ModelLibrary()

    # Execute the infinite loop until the user decides to quit
    while True:
        print('* * * * * * Welcome to Library Management System * * * * * *')
        print('What would you like to do?\n1. Add new book\n2. Remove a book\n3. Exit')
        # Ask user's input for desired action
        option = input("Enter your choice: ")

        # Perform the action based on user's input
        if option == '1':
            '''If input is 1, perform addition of book'''
            title = input("Enter title of the book: ")
            author = input("Enter the author of the book: ")
            id = int(input("Enter the ID of the book: "))
            lib.add_new_book(title, author, id)
        elif option == '2':
            '''If input is 2, remove the book'''
            id = int(input("Enter the ID of the book to be removed: "))
            lib.remove_book(id)
        elif option == '3':
            # If input is 3, quit and exit the program
            print("Thank you !")
            break
        else:
            print("OOPS, invalid option selected, try again !")


if __name__ == "__main__":
    main()
