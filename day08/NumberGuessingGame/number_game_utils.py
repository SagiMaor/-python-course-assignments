import random

def generate_number():
    return random.randint(1, 20)

def toggle_mode(mode):
    return not mode

def show_number(number):
    print(f"The number is {number}.")

def process_guess(guess, number):
    if guess < number:
        print("Too low!")
        return False
    elif guess > number:
        print("Too high!")
        return False
    else:
        print("You got it!")
        return True

def move_number(number):
    number += random.choice([-2, -1, 0, 1, 2])
    return max(1, min(20, number))
