# Inserting a string
string = "Guvi Geeks Network Private Limited"

#here we are defining a function called remove_vowels with the string as parameter.
def remove_vowels(string):
    #we are entering the upper and lower case of the vowels for the program to identify them
    vowels = "aeiouAEIOU"

    #here we are giving command to exclude the characters and show an result without the characters
    #join is an empty string
    result = ''.join([char for char in string if char not in vowels])
# this is a function that returns the new string result that contains string without vowels
    return result


# Calling the function and printing the result
output_string = remove_vowels(string)
print(output_string)