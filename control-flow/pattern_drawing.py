# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable for the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side in each row
    for col in range(size):
        print("*", end="")
    # Print a newline character after completing the row
    print()
    # Move to the next row
    row += 1
