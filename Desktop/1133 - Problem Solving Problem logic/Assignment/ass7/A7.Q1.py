# Author: Bandana C0916126
# Date: November 29, 2023
# Version: 1.0.0.0
# To sort the array using a selection sort and display the number of scores that are less than 500 and those greater than 500 from a given array.

# Initializing values
Scores = [198, 486, 651, 85, 216, 912, 73, 319, 846, 989]
N = 10

# Initializing lists for scores less than 500 and more than 500
LessThan500List = []
GreaterThan500 = []

# Selection sort for scores less than 500
for i in range(N):
    min_index = i
    for j in range(i + 1, N):
        if Scores[j] < Scores[min_index] and Scores[j] < 500:
            min_index = j
    Scores[i], Scores[min_index] = Scores[min_index], Scores[i]
    if Scores[i] < 500:
        LessThan500List.append(Scores[i])
    else:
        GreaterThan500.append(Scores[i])

# Output
print("Scores less than 500 in ascending order:", LessThan500List)
print("Scores greater than 500:", GreaterThan500)

# Logical Explaination:
# 1, First of all, initalizing the array where we keep the value whose value is less than 500 and greater than 500.
# 2, Using for loop to check each and every value in the Scores[].
# 3, During each iteration, it swaps the current element with the minimum element found, effectively sorting the array in ascending order. 
# 4, After for loop using if condition to append the value in the each list.
# 5, At last, Outputs are diplayed.