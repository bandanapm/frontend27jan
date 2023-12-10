# Author: Bandana C0916126
# Date : November 23, 2023
# Version :1.0.0.0
# Variables used : firstNames, lastNames, firstName, lastName, sentinel, i
# To create a program where user input first name in one arrey and lastname in a parallel arrey. The output should be a list of email addresses where the address is of the following form: first.last@mycollege.edu

# Initialize lists to store first names and last names
firstNames = []
lastNames = []

# Set sentinel character
sentinel = "exit"

# Checking conditions and output
# Repeating loop until user enter sentinal value
while True:
    # Enter first name 
    firstName = input("Enter first name or exit to end the program: ")

    # Check if the user enter first name or sentinel value
    if firstName == sentinel:
        break

    # Enter last name 
    lastName = input("Enter last name: ")

    # Adding first and last name to the fisrt and last name array
    firstNames.append(firstName)
    lastNames.append(lastName)

# Output
for i in range(len(firstNames)):
    email_address = f"{firstNames[i].lower()}.{lastNames[i].lower()}@mycollege.edu"
    print(f"Email address for {firstNames[i]} {lastNames[i]}: {email_address}")
