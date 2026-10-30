# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.

empty_list = []

# CREATE LISTS
animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print("Animals list:", animals)
print("Numbers list:", numbers)
print("Mixed data types list", mixed)

# print the third element in animals.
# print the last element in numbers
#print the first element in the mixed list
print(animals[2], numbers[-1], mixed[0])

# print the third element in animals.
print(animals[2])
# print the last element in numbers
print(numbers[-1])
#print the first element in the mixed list
print(mixed[0])

animals[-1] = "babirusa"
print(animals)

# add elements to the end of a list
animals.append("glass frog")

print(animals)

# insert an element at a specific index
animals.insert(2, "aye-aye")
print(animals)
animals.insert(1, "camel")
print(animals)

# remove elements
animals.remove("aye-aye")
print(animals)

# remove (pop off) last element and save it into a variable
last_animal = animals.pop()
print(last_animal)
print(animals)

### **Challenge 1: Number Swap**

# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*

nums = [ 1, 2, 3, 4, 5, 6 ]
new_num = input("Please enter a new interger: ")
nums.insert(2, new_num)
print(nums)

### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position and remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
shopping.append("Cheese")
print(shopping)
shopping.append("Butter")
print(shopping)
shopping.append("Eggs")
print(shopping)
shopping.insert(1, "Pasta")
print(shopping)
shopping.remove("Butter")
print(shopping)

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Numbers:", nums)

print("Length of list:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)

if "cat" in animals:
    print("Cat is in the list")
else:
    print("Cat is not in the list")

# Create a list of five floats called measurements.
# Print the length, minimum, maximum, and sum of the list using built-in functions.

measurements = [5.7, 4.11, 6.3, 5.2]
print("Length" , len(measurements), "Max:", max(measurements), "Min:", min(measurements) , "Sum:", sum(measurements))
