# contacts_app.py
"""
Personal Contacts Application

Author: Bandana Pachabhaiya Magar
Date: November 30, 2023
Description: This program allows users to manage personal contacts by adding, viewing, updating, and deleting contacts.
"""

# Data structures
contacts_list = []

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts_list.append(contact)
    print(f"Contact for {name} added successfully!\n")

# Function to view all contacts
def view_all_contacts():
    print("\nAll Contacts:")
    for contact in contacts_list:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    print()

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            print(f"\nUpdating contact for {name}:")
            field = input("Enter the field to update (name/phone/email/address): ")
            new_value = input(f"Enter the new value for {field}: ")
            contact[field] = new_value
            print(f"Contact updated successfully!\n")
            return
    print(f"Contact for {name} not found. Update failed.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            contacts_list.remove(contact)
            print(f"Contact for {name} deleted successfully!\n")
            return
    print(f"Contact for {name} not found. Deletion failed.\n")

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search for: ")
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            print(f"\nContact found for {name}:")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n")
            return
    print(f"Contact for {name} not found.\n")

# Main menu
while True:
    print("Personal Contacts Application")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_all_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("Exiting the Personal Contacts Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
