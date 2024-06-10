number = 123456789

def sum_first_last_digit(number):
    # Get the last digit
    last_digit = number % 10

    # Get the first digit
    while number >= 10:
        number //= 10
    first_digit = number

    # Calculate the sum
    digit_sum = first_digit + last_digit

    return digit_sum

result = sum_first_last_digit(number)
print("Sum of first and last digit:", result)
