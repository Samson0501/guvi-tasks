# providing the list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Using list comprehensions to separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Printing the results to seperate the Even and Odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
