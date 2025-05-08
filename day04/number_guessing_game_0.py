import random

number = random.randint(1, 20)
guess = input("Guess a number between 1 and 20: ")

if not guess.isdigit():
    print("Please enter a valid number.")
else:
    guess = int(guess)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
