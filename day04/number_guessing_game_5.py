import random

number = random.randint(1, 20)
debug_mode = False
move_mode = False

while True:
    if debug_mode:
        print(f"[DEBUG] Number to guess: {number}")

    guess = input("Guess ('x'=exit, 's'=show, 'd'=debug, 'm'=move): ")

    if guess == 'x':
        print("Exiting game.")
        break
    if guess == 's':
        print(f"The number is {number}.")
        continue
    if guess == 'd':
        debug_mode = not debug_mode
        print(f"Debug mode {'ON' if debug_mode else 'OFF'}")
        continue
    if guess == 'm':
        move_mode = not move_mode
        print(f"Move mode {'ON' if move_mode else 'OFF'}")
        continue
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        break

    if move_mode:
        number += random.choice([-2, -1, 0, 1, 2])
        number = max(1, min(20, number))  
