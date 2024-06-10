input_str = "My name is Samson and I am an Automation Tester"

def count_words(s):
    # Split the string into words using whitespace as the delimiter
    words = s.split()
    # Return the number of words
    return len(words)

# Example usage

result = count_words(input_str)
print("Number of words:", result)
