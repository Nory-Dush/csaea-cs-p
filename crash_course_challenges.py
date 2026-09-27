# This is Challange 1: Tip Calculator

bill = 50
tip_percent = 0.2
tip = bill * tip_percent
total = tip + bill

print(f" Tip:${tip} Total:${total}")

# This is Challange 2: Pizza Order

import math
 
students = 23
slices_per_student = 2
slices_per_pizza = 8
slices_needed = students * slices_per_student
pizzas_to_order = slices_needed / slices_per_pizza
slices_leftover = math.ceil(pizzas_to_order) * slices_per_pizza - slices_needed

print(f" {math.ceil(pizzas_to_order)} pizza(s) to order, {slices_leftover} slice(s) left.")

# This is Challange 3: Temperature Converter
fahrenheit = 212
# C = (F - 32) * 5 / 9
x = 32
y = 5
z = 9

C = (fahrenheit-x) * y / z

print(f"212 F is equal to {C} C")

# This is Challange 4: Report Card 

score = 84

if score >= 90 and score <= 100:
    print("A") 

elif score >= 80 and score < 90:
    print("B")

elif score >= 70 and score < 80:
    print("C")
    
elif score >= 60 and score < 70:
    print("D")

else:
    print("F")

# Challange 5: Login Screen

password = "csaea2026"
attempt = "CSAEA2026"

if attempt == password:
    print("Access granted")

elif attempt != password:
    print("Access denied")

# Challange 6: Even/Odd Parking

plate = 4827

if plate % 2 == 0:
    print("Park on the east side")

elif plate % 2 != 0:
    print("Park on the west side")

# Challange 7: Roller Coaster Gate

height = 50
age = 8
has_adult = True

if height < 48:

    print("You may not ride!")

elif height >= 48 and age >= 10 or has_adult == True :
    print("You may ride!")

else:
    print("You may not ride!")

# Challage 8: Name Tag Generator

first = "Ada"
last = "Lovelace"
school = "CSAEA"

print("Hello my name is " + first + " " + last + " and I am from " + school + ".")

# Challange 11: Rocket Launch

start = 10

for i in range (10 , 0 , -1 ):
    print(i)
print("Liftoff!")

# Challange 12: Times Table Helper

number = 7

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}") 