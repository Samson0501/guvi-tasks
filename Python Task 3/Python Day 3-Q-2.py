#Defining the fuction to take the argument filename
def read_file(filename):
    # Try to open and read the file
    try:
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Print the content to the console
            print(content)
    except FileNotFoundError:
        # If the file is not found, print an error message
        print(f"File '{filename}' not found.")

#Example
filename = 'Guvi.txt'
read_file(filename)
