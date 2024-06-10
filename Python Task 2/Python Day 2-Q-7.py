#providing the list
numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4]

def first_non_repeating(nums):
    # Use list comprehension to filter non-repeating elements
    non_repeating = [num for num in nums if nums.count(num) == 1]

    # Return the first non-repeating element if found, otherwise None
    return non_repeating[0] if non_repeating else None

result = first_non_repeating(numbers)
print("First non-repeating element:", result)
