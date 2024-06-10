#providing list
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_minimum(sorted_list):
    #checking if the list is empty or not
    if sorted_list:
        return sorted_list[0]
    else:
        return None

#sorting the list example
minimum = find_minimum(sorted_list)
print("Minimum element:", minimum)
