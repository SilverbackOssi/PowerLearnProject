'''
Write a program that accepts user input to create a list of integers.
Then, compute the sum of all the integers in the list.
'''

# Program to accept user input and compute the sum of integers in a list

def get_integer_list():
    """
    Prompts the user to enter integers separated by spaces and returns a list of integers.
    """
    try:
        user_input = input("Enter a list of integers separated by spaces: ")
        int_list = [int(num) for num in user_input.split()]
        return int_list
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return get_integer_list()

def compute_sum(int_list):
    """
    Computes the sum of all integers in the given list.
    """
    return sum(int_list)


numbers = get_integer_list()
total = compute_sum(numbers)
print(f"The sum of the entered numbers is: {total}")
