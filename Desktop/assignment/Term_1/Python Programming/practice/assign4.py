# Creating a empty array list named my_list and using for loop ask 5 user input and append to the list
my_list = []
for i in range(5):
    number = int(input("Please enter a number: "))
    my_list.append(number)
print("The elements inside the list are: ", my_list)

# Accessing first, second and third to fifth element of my_list
print("The second element in the list is: ", my_list[1])
print("The last element in the list is: ", my_list[-1])
print("The third to fifth element in the list are: ", my_list[2:5])

# Combime my_list with provided value of new_list
new_list = [7, 8, 9, 10]
combined_list = my_list + new_list
print("The new combined list is: ", combined_list)

# Check length of the combined list then append new item, then sort the list
print("The length of combined_list is: ", len(combined_list))
combined_list.append(11)
combined_list.sort()
print("The sorted combined list is: ", combined_list)

# Check the count of provided value inside the array list, the remove its first occurance from the list
occurance_7 = combined_list.count(7)
print("The occurrences of 7 in the combined list: ", occurance_7)
combined_list.remove(7)
print("The updated combined list after removing element 7 is: ", combined_list)

# Use list comprehension to create squared list where each element is squared of element in combined list
squared_list = [num ** 2 for num in combined_list]
print("The updated list with it's value squared is: ", squared_list)
