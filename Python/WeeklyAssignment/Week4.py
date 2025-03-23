'''
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
'''

# Program to read a file and write a modified version to a new file with error handling

def process_file():
    """
    Reads a user-specified file, modifies its content, and writes to a new file.
    Handles errors if the file does not exist or cannot be read.
    """
    input_filename = input("Enter the filename to read: ")
    output_filename = "modified_" + input_filename
    
    try:
        # Read input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Processing complete! Modified content saved in {output_filename}.")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except IOError:
        print("Error: Unable to read the file. Please check permissions.")

# Run the program
process_file()
