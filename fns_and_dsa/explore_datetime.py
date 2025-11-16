from datetime import datetime, timedelta, timezone

egypt_tz = timezone(timedelta(hours=2))

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format
    """
    current_date = datetime.now(egypt_tz)
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate the future date by adding the given number of days to current date
    """
    current_date = datetime.now(egypt_tz)
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    while True:
        try:
            days_input = int(input("Enter the number of days to add to the current date: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    calculate_future_date(days_input)

if __name__ == "__main__":
    main()

