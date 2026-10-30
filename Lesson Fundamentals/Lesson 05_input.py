# USER INPUT IN PYTHON

print("\n--- User Input Demonstration ---")

# Basic text input
name = input("Enter your name: ")
print("Hello,", name)

# Input is always stored as a string, even if you type a number
age = input("Enter your age: ")
print("You said your age is:", age, "(type:", type(age), ")")

# To use numbers, we must cast (convert) the string to int or float
age_number = int(age)
print("Next year, you will be:", age_number + 1)

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

# ---------------------------------------------------------
# CHALLENGES
# ---------------------------------------------------------

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

color = input("Type your favorite color: ")
print(f"Your favorite color is {color}!")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

num_one = int(input("Number 1: "))
num_two = int(input("Number 2: "))
print(f"The sum of your numbers is... {num_one + num_two}!" )

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
import math

diameter = float(input("Give me a diameter for a circle please: "))
radius = diameter / 2
radius_squared = radius ** 2
area = radius_squared * math.pi
print("The area of the circle is:" , area )

# Challenge: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random

sides = int(input("How many sides should the die have? "))
roll = random.randint(1,sides)
print(f"You rolled... {roll}")