# Total number of rows that the pyramid needs, which can be altered as per requirement
num_rows = 5

# Mentioning the starting number of the numeric
start_number = 1

# S represents the current row number starting from 1 to the num_rows
for S in range(1, num_rows + 1):
    # need to print the spaces to align numbers properly and this can also be altered as per the requirement
    print("   "* (num_rows - S), end="   ")

    # Loop to pring the lines for the pyramid
    for J in range(1, S * 2):
        print(start_number, end=" ")
        start_number += 1
        # This commend breaks the loop if the last number (20) is reached
        if start_number >20:
            break

    # Move to the next line for the next row
    print()
