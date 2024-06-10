#inserting the lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

def find_duplicates(list1, list2, list3):
    # Use set intersection to find duplicates
    duplicates = set(list1) & set(list2) & set(list3)
    return list(duplicates)

result = find_duplicates(list1, list2, list3)
print("Duplicates:", result)
