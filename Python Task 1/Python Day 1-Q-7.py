# Example usage
input_str = "My name is Samson Joshua, studying in Guvi"

from collections import Counter


def most_frequent_char(s):
    # Remove spaces to only count characters
    s = s.replace(" ", "")

    # Use Counter to count the frequency of each character
    freq_counter = Counter(s)

    # Find the character with the maximum frequency
    most_common_char = freq_counter.most_common(1)[0][0]

    return most_common_char



result = most_frequent_char(input_str)
print("Most Frequent Character:", result)

