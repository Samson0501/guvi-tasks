#Getting the current date and time from the PC
import datetime

#Creating a text file with the current timestamp in its name
def create_file_with_timestamp():
    #Getting the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    #Creating a filename using the timestamp
    filename = f"file_{current_timestamp}.txt"

    #Createing and opening the file in write mode
    with open(filename, 'w') as file:
        file.write("This file was created with a timestamp in its name.\n")

    print(f"File '{filename}' created successfully.")


#Calling the function to create the file
create_file_with_timestamp()
