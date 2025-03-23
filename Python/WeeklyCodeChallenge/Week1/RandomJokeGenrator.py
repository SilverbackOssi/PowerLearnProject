'''
3. Random Joke Generator 🤣
Build a program that stores a list of jokes and randomly selects one to display every time the user runs it.
Add a fun twist with jokes about Python or programming! 🐍💡
'''

import random

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Python programmers prefer snakes? Because they don’t need semicolons!",
    "How do you comfort a JavaScript bug? You console it!",
    "Why did the programmer go broke? Because he used up all his cache!",
    "What is a programmer’s favorite place to hang out? The Foo Bar!"
]

# Randomly select and display a joke
print(random.choice(jokes))
