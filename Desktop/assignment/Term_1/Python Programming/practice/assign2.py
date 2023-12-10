def main_901142():
    # Ask input from user
    entered_month_901142 = input("Enter a month between 1 and 12: ")

    # Parse entered month into integer
    parsed_month_901142 = int(entered_month_901142)

    calculate_quarter_901142(parsed_month_901142)

# Determine in which quarter the entered month falls


def calculate_quarter_901142(month_901142):
    # Check if the month falls under first quarter i.e. month is between 1 and 4
    if month_901142 > 0 and month_901142 <= 4:
        print(f"Month {month_901142} is in the first quarter.")
    # Check if the month falls under second quarter i.e. month is between 5 and 7
    elif month_901142 > 4 and month_901142 <= 7:
        print(f"Month {month_901142} is in the second quarter.")
    # Check if the month falls under third quarter i.e. month is either 8 or 9
    elif month_901142 > 7 and month_901142 <= 9:
        print(f"Month {month_901142} is in the third quarter.")
    # Check if the month falls under fourth quarter i.e. month is between 10 and 12
    elif month_901142 > 9 and month_901142 <= 12:
        print(f"Month {month_901142} is in the fourth quarter.")
    # Display error if invalid range is selected for months
    else:
        print("OOPS !, Invalid month range entered 😣\nPlease choose month between 1 to 12.")


# Call main method to execute the program
main_901142()
