# Example usage
nums = [10, 20, 30, 9]
target = 59

def find_triplet(nums, target):
    # Initialize the result list to store triplets
    triplets = []

    #Use three nested loops to generate all possible combinations of triplets from the list
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    triplets.append((nums[i], nums[j], nums[k]))

    return triplets

result = find_triplet(nums, target)

#printing the program
print("Triplets with sum equal to", target, ":", result)
