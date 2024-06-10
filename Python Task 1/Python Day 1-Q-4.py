# inserting a string
string = "Guvi Geeks Network Private Limited"

def count_unique_characters(string):

    #here we are inserting a data structure called set to remove all the duplicate elements on the string
    unique_characters = set(string)

    #here we are inserting length function to count the number of unique characters on the string
    return len(unique_characters)


# Calling the function and print the result
unique_count = count_unique_characters(string)
print("Number of unique characters:", unique_count)