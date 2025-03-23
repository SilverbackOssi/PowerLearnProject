'''
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color.
Ask the user for input and store the information in the dictionary.
Then, print the dictionary to the console.
'''

# Program to store and display user information in a dictionary

def get_person_info():
    """
    Prompts the user for personal information and stores it in a dictionary.
    """
    person = {}
    person["name"] = input("Enter your name: ")
    
    try:
        person["age"] = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input for age. Please enter a number.")
        return get_person_info()
    
    person["favorite_color"] = input("Enter your favorite color: ")
    
    return person


person_info = get_person_info()
print("\nPerson Information:")
print(person_info)
