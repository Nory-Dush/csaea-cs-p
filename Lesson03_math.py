#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 743543 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 7 / 2
print("Float division:", float_divide)

integer_divide = 7 // 2
print("Integer division:", integer_divide)

mod = 7 % 2
print("Modulus: ", mod) 

exponent = 7 ** 2
print("Exponent:", exponent)

#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  
# Create separate variables for width, height, and result. Print result.

width = 8
height = 5
area = width * height
print("The area of the rectangle is:" , area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  

pie = 3.14
radius = 7
radius_squared = radius ** 2
circle_area = pie * radius_squared
print("The area of the circle is:" , circle_area)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  
# Use only one print statement. Print the result in this format: 
#     Book: <$ cost of book>
#     Notebook: <$ cost of notebook>
#     Total: <$>

book = 12.99
notebook = 3.50
books_bought = 3
notebooks_bought = 4
book_cost = book * books_bought
notebook_cost = notebooks_bought * notebook
total_cost = book_cost + notebook_cost

print(f" Book: ${book} \n Notebook: ${notebook}0 \n Total: ${total_cost}" )

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 

number = 57
if number % 2 == 0:
    print("Even")
else:
    print("Odd")