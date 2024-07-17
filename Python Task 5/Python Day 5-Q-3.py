from functools import reduce

# Generate the first 50 elements of the Fibonacci series using a lambda function
fib_series = reduce(lambda x, _: x + [x[-1] + x[-2]], range(48), [0, 1])

# Print the Fibonacci series
print(fib_series)
