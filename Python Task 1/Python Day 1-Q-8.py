str1 = "My name is Samson"
str2 = "It is a good day"

def are_anagrams(str1, str2):
    # Remove any whitespace and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Use Counter to count the frequency of each character in both strings
    from collections import Counter
    return Counter(str1) == Counter(str2)

result = are_anagrams(str1, str2)
print("Are the strings anagrams?", result)
