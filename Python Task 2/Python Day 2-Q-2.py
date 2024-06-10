# providing the list with numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]


def is_prime(n):
    # Simple function to check if a number is prime
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Use list comprehension to create a list of prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Counting the number of prime numbers
prime_count = len(prime_numbers)

# Print the results
print("Prime numbers:", prime_numbers)
print("Number of prime numbers:", prime_count)
