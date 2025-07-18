# pattern_drawing.py

# Prompt the user for a pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for rows
row = 0

# Use a while loop to handle each row
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
