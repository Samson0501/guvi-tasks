# Getting the current date and time from the PC
import datetime

# Creating a text file with the current timestamp in its name
def create_file_with_timestamp_content():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a filename using the timestamp
    filename = "timestamp_file.txt"

    # Create and open the file in write mode
    with open(filename, 'w') as file:
        # Write the current timestamp to the file
        file.write(f"Current timestamp: {current_timestamp}\n")

    print(f"File '{filename}' created successfully with timestamp content.")
    #Calling the function


# Call the function to create the file with timestamp content
create_file_with_timestamp_content()
