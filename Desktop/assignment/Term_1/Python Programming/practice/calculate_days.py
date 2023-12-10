# Global constant for living years
TOTAL_LIVING_YEARS_901142 = 90

# Calculate remaining days
def calculate_remaining_days_901142(years_901142):
    remaining_days_901142 = years_901142 * 365
    return remaining_days_901142

# Calculate remaining weeks
def calculate_remaining_weeks_901142(years_901142):
    remaining_weeks_901142 = years_901142 * 52
    return remaining_weeks_901142

# Calculate remaining months
def calculate_remaining_months_901142(years_901142):
    remaining_months_901142 = years_901142 * 12
    return remaining_months_901142
def main_901142():
    # Take input from user for current age
    entered_age_901142 = input("Enter your current age: ")

    # Parse entered age into integer
    parsed_age_901142 = int(entered_age_901142)

    # Calculate remaining years
    remaining_years_901142 = TOTAL_LIVING_YEARS_901142 - parsed_age_901142

    days_901142 = calculate_remaining_days_901142(remaining_years_901142)
    weeks_901142 = calculate_remaining_weeks_901142(remaining_years_901142)
    months_901142 = calculate_remaining_months_901142(remaining_years_901142)

    # Format the message and print in console
    message_901142 = f"You have {days_901142} days, {weeks_901142} weeks, and {months_901142} months left."
    print(message_901142)

# Call main method to execute the program
main_901142()
