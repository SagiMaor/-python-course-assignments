import random

secret_number = random.randint(1, 20)

guess = int(input("Guess the number I'm thinking of (between 1 and 20): "))

if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Correct! You guessed it!")
