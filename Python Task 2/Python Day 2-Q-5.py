# Example usage
mangoes = [7, 3, 10, 4, 5, 8, 2, 6, 12, 11]
students = 6

def distribute_mangoes(mangoes, students):
    # Sorting the list of mangoes
    mangoes.sort()

    # Calculating the number of mangoes each student should get
    bags_per_student = len(mangoes) // students
    remaining_bags = len(mangoes) % students

    # Initialize variables to keep track of minimum and maximum differences
    min_difference = float('inf')
    max_difference = 0

    # Initialize variables to store the index of the last bag distributed
    last_bag_index = 0

    # Iterate through the bags and distribute them to students
    for i in range(students):
        # Calculate the number of bags the current student should get
        bags_to_distribute = bags_per_student
        if remaining_bags > 0:
            bags_to_distribute += 1
            remaining_bags -= 1

        # Calculate the difference between the number of mangoes in the bags
        difference = mangoes[last_bag_index + bags_to_distribute - 1] - mangoes[last_bag_index]

        # Update minimum and maximum differences
        min_difference = min(min_difference, difference)
        max_difference = max(max_difference, difference)

        # Update the index of the last bag distributed
        last_bag_index += bags_to_distribute

    return min_difference, max_difference

min_diff, max_diff = distribute_mangoes(mangoes, students)
print("Minimum difference between bags:", min_diff)
print("Maximum difference between bags:", max_diff)
