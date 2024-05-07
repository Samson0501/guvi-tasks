def count_vowels(string):
    # This is to count the vowels on the input string
    count_a = count_e = count_i = count_o = count_u = 0
#this is to keep track on the provided variable
    for char in string:
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1
#here we check the vowels inside these loops and increment the corresponding count

    total_vowels = count_a + count_e + count_i + count_o + count_u
    # To calculate the total num of vowels

    return total_vowels, count_a, count_e, count_i, count_o, count_u
 #This command is to identify the num of individual vowels on the input

input_string = "Guvi Geeks Network Private Limited"
total_vowels, count_a, count_e, count_i, count_o, count_u = count_vowels(input_string)
print("Total vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)