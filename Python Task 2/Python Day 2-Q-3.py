# providing the list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]


def is_happy(num):
    # Function to check if a number is happy
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

# Count the number of happy numbers using list comprehension
happy_count = sum(1 for num in numbers if is_happy(num))
happy_count = sum(1 for num in numbers if is_happy(num))

# Print the result
print("Number of happy numbers:", happy_count)
