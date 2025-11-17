from datetime import datetime, timedelta

def display_current_datetime():
    """
    This function displays the current date and time
    in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date


def calculate_future_date(days):
    """
    This function calculates the future date by adding
    the given number of days to today's date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Save future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date


# ------------ Main Program ------------
if __name__ == "__main__":
    # Part 1: Display current date/time
    display_current_datetime()

    # Part 2: User input + future date calculation
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(num_days)
    except ValueError:
        print("Please enter a valid integer.")

