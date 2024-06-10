#inserting a string
input_string = "Guvi Geeks Network Private Limited"

#here we are defining a function called is_palindrome to take a parameter or a string
def is_palindrome(input_string):

    #here we are removing the non-alphanumeric characters and converting upper to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    #Checking if the cleaned string is equal to its reverse by slicing method
    return cleaned_string == cleaned_string[::-1]


# Calling the function and printing the result

Result = is_palindrome(input_string)
print("Is the string a palindrome?", Result)