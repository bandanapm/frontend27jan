

total_age = 0
student_count = 0


age = int(input("Enter the age of the student (enter 99 to exit): "))

# While age is not equal to 99, continue the loop
while age <= 99:
    # Add the age to total_age
    total_age += age
    # Increment student_count by 1
    student_count += 1
    # Get the age from the user again
    age = int(input("Enter the age of the student (enter 99 to exit): "))

# Calculate the average age
if student_count != 0:
    average_age = total_age / student_count
else:
    average_age = 0

print("Number of students:", student_count)
print("Total age:", total_age)
print("Average age:", average_age)
