"""
Author: Bandana Pachabhaiya Magar
ID: C0916126
Date: November 30, 2023
Description: This program allows users to add, view, update, delete and search contacts.
"""

# Import the regular expression (re) module
import re
class ContactManager:
    def __init__(self):
        self.contacts = []  # List to store contact dictionaries

    def addContact(self):
        contact = {}       # initializing a dictionary named contact
        contact['name'] = input("Please enter contact's name: ")
        contact['phone'] = self.get_valid_phonenumber()  # Use the new function to get a valid phone number
        contact['email'] = self.get_valid_email()  # Use the new function to get a valid email
        contact['address'] = input("Please enter the address: ")
        self.contacts.append(contact)

    def get_valid_phonenumber(self):
        while True:
            phone = input("Please enter the phone number: ")
            # Use regular expression to check if the phone number format is valid (exactly 10 digits)
            if re.match(r"^\d{10}$", phone):
                return phone
            else:
                print("Please enter a valid 10-digit phone number. Without country code.")

    def get_valid_email(self):
        while True:
            email = input("Please enter the email: ")
            # Use regular expression to check if the email format is valid
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Please enter a valid email formate. Example[example@gamil.com]")

    def viewContacts(self):
        # Check if there are any contacts in the list
        if self.contacts:
            # Loop to display the details of contact
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone-number: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']} ")
                print("-" * 90)
                print()
        # If there is zero contacts available try adding new one or exit.
        else:
            print("No contacts to view.")
            inputContact = input("Do you want to add contacts? Choose y = yes or n = no :")
            if inputContact.lower() == 'y':
                self.addContact()
            else:
                main()

    def updateContact(self):
        # Prompt the user for the name of the contact to update
        name = input("Please enter the contact's name you would like to update: ")
        contact = self.findContact(name)    # Find the contact in the list based on the provided name
        if contact:
            chooseUpdate = input("Which value you would like to update? (name/phone/email/address): ")
            new_value = input(f"Please enter the new {chooseUpdate}: ")
            contact[chooseUpdate] = new_value    # Update the contact's field with the new value
            print("Contact updated successfully!")  
        else:
            print(f"SORRY! Contact not found.")   

    def deleteContact(self):
        # Prompt the user for the name of the contact to delete
        name = input("Please enter the contact's name: ")
        contact = self.findContact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully!")
            
        else:
            print(f"SORRY! Contact not found.")

    def searchContact(self):
        name = input("Please enter the contact's name: ")
        contact = self.findContact(name)
        if contact:
            print(f"Name: {contact['name']}, Phone-number: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']} ")
        else:
            print(f"SORRY! Contact not found.")
            
    def findContact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():      # Search for the contact in the list by comparing names (case-insensitive)
                return contact
        return None

def main():
    # Create an instance of the ContactManager class
    contact_manager = ContactManager()
    #menu
    while True:
        print("\nPersonal Contacts Application")
        print("1. Add a Contact")
        print("2. View All Contacts")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. Search a Contact")
        print("6. Exit")

        # Prompt the user for their choice
        choice = input("Please enter your choice from 1 to 6: ")

        if choice == '1':
            contact_manager.addContact()      # Call addContact 
        elif choice == '2':
            contact_manager.viewContacts()    # Call viewContacts 
        elif choice == '3':
            contact_manager.updateContact()   # Call updateContact 
        elif choice == '4':
            contact_manager.deleteContact()   # Call deleteContact 
        elif choice == '5':
            contact_manager.searchContact()   # Call searchContact 
        elif choice == '6':
            break                             # Exit the loop and end the program
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()