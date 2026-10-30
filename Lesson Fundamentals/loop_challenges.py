for i in range(10, 0, -3):
    print(i)

for i in range(3):
    if i == 5:
        break
    else:
        print("done")

total = 0
n = 1

while total < 20:
    total = total + n
    n += 2

print(total, n)

count = 0
for letter in "pineapple":
    if letter in "aeiou":
        count += 1
    
    if count:
     print(count)


n = 10

while n == 0:
    n -= 3
print("escaped")

# Pseudocode:
#   repeat 5 times (use a for-loop with range):
#       ask the player for a guess (convert it to an int!)
#       if guess equals secret → print "Got it!" and stop the loop
#       otherwise, if guess is bigger → print "Too high"
#       otherwise → print "Too low"
#   if the loop never stopped early → print "Out of guesses! It was" + secret

import random
secret = random.randint(1, 20)

# Repeat 5 times (use a for-loop with range)

for attempt in range(5):
    # Ask the player for a guess (convert it to an int!)
    guess = int(input("Enter your guess:"))

    if guess == secret:
        print("You win!")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

print("Game over!")
    


