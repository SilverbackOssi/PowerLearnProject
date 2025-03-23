'''
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()).
However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
'''

# Class Design: Smartphone

class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def info(self):
        return f"{self.brand} {self.model} costs ${self.price}"

# Inheritance Example: Smartphone with AI Features
class AISmartphone(Smartphone):
    def __init__(self, brand, model, price, ai_assistant):
        super().__init__(brand, model, price)
        self.ai_assistant = ai_assistant
    
    def use_ai(self):
        print(f"Activating {self.ai_assistant} on {self.model}...")

# Polymorphism Challenge: Vehicles
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving... 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying... ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing... ⛵")

# Testing the classes
phone1 = AISmartphone("Apple", "iPhone 14", 999, "Siri")
print(phone1.info())
phone1.call("123-456-7890")
phone1.use_ai()

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
