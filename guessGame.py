import random 

jackpot = random.randint(1, 100)

guess = int(input("Guess the number "))

counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
    
    guess = int(input("Guess the number"))
    counter += 1

print("Correct guess")
print("You took", counter, "attempts")