
str1 = "My name is Samson, i study in Guvi"
str2 = "Automation Testing"


def longest_common_substring(str1, str2):
    # Create a 2D array to store lengths of longest common suffixes of substrings
    m = len(str1)
    n = len(str2)
    lcsuffix = [[0] * (n + 1) for _ in range(m + 1)]

    # To store the length of the longest common substring
    longest_length = 0

    # To store the ending index of the longest common substring in str1
    end_index_str1 = 0

    # Building the lcsuffix array in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcsuffix[i][j] = lcsuffix[i - 1][j - 1] + 1
                if lcsuffix[i][j] > longest_length:
                    longest_length = lcsuffix[i][j]
                    end_index_str1 = i - 1
            else:
                lcsuffix[i][j] = 0

    # Longest common substring is from end_index_str1 - longest_length + 1 to end_index_str1 in str1
    longest_common_substring = str1[end_index_str1 - longest_length + 1:end_index_str1 + 1]
    return longest_common_substring



result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)
