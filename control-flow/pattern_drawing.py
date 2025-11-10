# File: pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop for rows
while row < size:
    # Nested for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to next line
    print()  # Move to the next row after printing all columns
    row += 1  # Increment row counter
