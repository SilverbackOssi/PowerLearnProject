'''
Create a program that stores a list of words.
Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
'''

# Program to filter words with an odd number of characters

# List of words
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

# List comprehension to filter words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Display the result
print("Words with an odd number of characters:", odd_length_words)
