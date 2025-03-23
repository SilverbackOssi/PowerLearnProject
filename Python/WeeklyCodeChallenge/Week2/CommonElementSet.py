'''
Write a program that accepts user input to create two sets of integers.
Then, create a new set that contains only the elements that are common to both sets.
'''

# Program to find common elements between two sets of integers

def get_integer_set(prompt):
    """
    Prompts the user to enter a set of integers separated by spaces and returns a set of integers.
    """
    try:
        user_input = input(prompt)
        int_set = set(map(int, user_input.split()))
        return int_set
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return get_integer_set(prompt)

# Get user input for two sets
set1 = get_integer_set("Enter the first set of integers separated by spaces: ")
set2 = get_integer_set("Enter the second set of integers separated by spaces: ")

# Find common elements
common_set = set1.intersection(set2)

# Display the result
print("\nCommon elements between both sets:", common_set)
