# Author: Bandana C0916126
# Date: November 29, 2023
# Version: 1.0.0.0
# To check the number given by a user between 0 to 1000 is a perfect square or not using serial search.

# Declare variables
Numbers = []
PerfectSquares = []
InputNumber = 0
i = 0
n = 0

# Taking input from the user
InputNumber = int(input("Enter a number from 0 to 1000: "))

# Serial search function
def serialSearch(Numbers, n):
    for element in Numbers:
        if element == n:
            return True
    return False

# Generate a list of perfect squares up to 100
PerfectSquares = [i ** 2 for i in range(100)]

# Check if the input number is a perfect square
perfect_square = serialSearch(PerfectSquares, InputNumber)

# Print output
if perfect_square:
    print(str(InputNumber) + " is a perfect square.")
else:
    print(str(InputNumber) + " is not a perfect square.")

# Logical Explaination:
# 1, The program begins by prompting the user to input a number between 0 and 1000 using the input function.
# 2, serialSearch takes a list of numbers (Numbers) and a target number (n). It iterates through each element in the list and checks if any element is equal to the target number (n). If a match is found, the function returns True; otherwise, it returns False.
# 3, i ** 2 for i in range(100) this calculate perfect square value form 0 to 100 anf put the value in PerfectSquares.
# 4, Finally, the program prints whether the inputted number is a perfect square or not.