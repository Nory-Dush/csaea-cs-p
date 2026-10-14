# STRING MANIPULATION IN PYTHON
# built-in methods: len(), upper(), lower(), capitalize()

greeting = "Hello" 

# String formatting, string concatination 

first_name = "Ada"
last_name = "Lovelace"
#Option 1
print("Hello", first_name, last_name, "!")
#Concatenation:
print("Hello" + first_name + " " + last_name + "!")
#f-strings
print(f"Hello, {first_name} {last_name}")

# 0 1 2 3 4
# H e l l o

greeting = "Hello"
second_letter = greeting[1]
print(second_letter)

# String indexing and slicing

word = "Super-cali-fragil-istic-expi-ali-docious"
print("\nThe word is:" , word)
print("First letter is:" , word[0])
print("Last letter is:" , word[-1])
print("Range of letters (non-inclusive):" , word[3:7] )
# Does not include second number
print("First five letters:" , word[:5])
print("Everything after the first five letters:" , word[5:])
print("Last seven letters:" , word[-7:])
print("Step through every second character:" , word[::2])
# Two colons means there are hidden zeros [0:0:2]
print("String in reverse:" , word[::-1])

last_name = "Lovelace"
length = len(last_name)
print("Length of string:" , length)

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

favorite_quote = "I will not be afraid"
quote_length = len(favorite_quote)
print(f"Favorite quote: {favorite_quote} \nQuote length: {quote_length}")

# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

user_word = "motivational"
print("The second through sixth characters are:", user_word[1:6])

# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada

firstname = "Ada"
lastname = "Lovelace"

print(f"Enter first name: {firstname} \nEnter last name: {lastname} \nFormatted name: {lastname}, {firstname}")
