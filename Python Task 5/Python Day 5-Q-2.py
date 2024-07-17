data = [10, 'hello', 501, 'world', 22, 37, 'python', 100, 999, 87, 'code', 351]

# Check if each element is an integer
is_integer = [isinstance(x, int) for x in data]

# Check if each element is a string
is_string = [isinstance(x, str) for x in data]

print("Is integer:", is_integer)
print("Is string:", is_string)
