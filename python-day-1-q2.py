# Total number of rows that the pyramid needs, which can be altered as per requirement
num_rows = 5

# Mentioning the starting number
start_number = 1

# S represents the current row number, starting from 1 and going up to the num_rows
for S in range(1, num_rows + 1):
    # spaces to align numbers properly, can be altered as per the requirement
    print("   "* (num_rows - S), end="   ")

    # This loop prints the numbers for each row of the pyramid
    for J in range(1, S * 2):
        print(start_number, end=" ")
        start_number += 1
        # This commend breaks the loop if the last number (20) is reache
        if start_number >20:
            break

    # Move to the next line for the next row
    print()
