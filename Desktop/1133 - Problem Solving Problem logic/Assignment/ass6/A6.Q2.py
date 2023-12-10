# Author: Bandana C0916126
# Date : November 23, 2023
# Version :1.0.0.0
# Variables used :  itemNames, itemCosts, numberStocks, itemName, itemCost, numberStock, i
# To create a program where take input in parallel arrays, the type of item, its cost, and the number in stock. Output should be in table formate

def main():
    # Initialize lists to store first names and last names
    itemNames = []
    itemCosts = []
    numberStocks = []

    # Taking user input
    while True:
        itemName = input("Enter item name or exit to end the program: ")
        if itemName.lower() == 'exit':
            break

        # Taking cost from user
        itemCost = float(input("Enter item cost: "))
        numberStock = int(input("Enter the number in stock: "))

        # Adding data to its recpective array
        itemNames.append(itemName)
        itemCosts.append(itemCost)
        numberStocks.append(numberStock)

    # Output
    print("---------------------------------------------")
    print(" Item Name     Cost      Number in Stock    ")
    print("---------------------------------------------")
    # using loop to display each item in lists
    for i in range(len(itemNames)):
        print(f" {itemNames[i]:<12}   ${itemCosts[i]:.2f}      {numberStocks[i]:<6}   ")
    print("---------------------------------------------")

# calling main function
if __name__ == "__main__":
    main()