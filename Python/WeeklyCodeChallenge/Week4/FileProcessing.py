'''
🔹 Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

📌 Task Requirements:
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt.
Print a success message once the new file is created.
'''
# Program to read a text file, process its content, and write results to a new file

def process_file(input_filename, output_filename):
    try:
        # Read input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Process content
        word_count = len(content.split())
        uppercase_content = content.upper()
        
        # Write to output file
        with open(output_filename, 'w') as outfile:
            outfile.write(uppercase_content + "\n\n")
            outfile.write(f"Word Count: {word_count}\n")
        
        print("Processing complete! Check output.txt for results.")
    except FileNotFoundError:
        print("Error: input.txt not found. Please create the file and try again.")

# File names
input_file = "input.txt"
output_file = "output.txt"

# Process the file
process_file(input_file, output_file)
