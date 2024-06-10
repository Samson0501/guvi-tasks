#providing a string
nums = [4, 2, -3, 1, 6]

def has_sublist_with_zero_sum(nums):
    #create a set to store prefix sums
    prefix_sums = set()

    #initialize prefix sum
    prefix_sum = 0

    #iterate through the list and check for zero sum sublists
    for num in nums:
        #update the prefix sum by adding the current number
        prefix_sum += num

        #if the prefix sum is zero or if it has been seen before,
        #it means there is a sublist with zero sum
        if prefix_sum == 0 or prefix_sum in prefix_sums:
            return True

        # Add the current prefix sum to the set
        prefix_sums.add(prefix_sum)

    #if no sublist with zero sum is found, return False
    return False

result = has_sublist_with_zero_sum(nums)
print("Sublist with zero sum exists:", result)
