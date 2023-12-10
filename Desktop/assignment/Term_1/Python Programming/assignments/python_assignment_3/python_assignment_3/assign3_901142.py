def main():
    # Ask user input for starting value
    starting_value = int(input("Enter the value for start: "))

    # Ask user input for ending value
    ending_value = int(input("Enter the value for end: "))

 # Check if starting value is less than or equal to ending value
    if starting_value <= ending_value:
        # Store the sum value in local variable and print the output with string formatting
        sum_value = calculate_odd_sum(starting_value, ending_value)
        # display the output
        print(
            f"The sum of all odd numbers between {starting_value} and {ending_value}, is {sum_value}")

    else:
        print("OOPS !, start value should be less than or equal to end value.")

# Calculate the sum of odd numbers for the given range of value


def calculate_odd_sum(starting_value, ending_value):

    # Declare local variable to store the sum of odd numbers which is later updated from inside the loop
    sum_value = 0
    # Iterate through the range of value from starting to the end, ending_value + 1 is used because the range()
    # function generates a sequence up to, but not including, the ending value.
    for num in range(starting_value, ending_value + 1):
        # Check if the current value is even or odd
        if num % 2 != 0:
            sum_value += num
    # Return the sum value after the loop is ended
    return sum_value


# execute main method to run the program
main()
