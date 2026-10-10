# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down = math.floor(4.8)
print(f"Round Down: {round_down}")

exponent = math.pow(2,5)
print(exponent)

# CONSTANTS are variables that NEVER change. They are written in ALL CAPS
PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

diameter = 14
radius = diameter / 2
radius2 = math.pow(radius , 2)
PI = math.pi 
circle_area = PI * radius2
print("Area:" , circle_area)

# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator 

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

seed = 0.2
step1 = seed + 657
step2 = step1 - 279
step3 = step2 * 3
result = math.ceil(step2)
print(result)


