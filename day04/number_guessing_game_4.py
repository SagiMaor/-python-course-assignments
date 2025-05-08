import random

number = random.randint(1, 20)
debug_mode = False

while True:
    if debug_mode:
        print(f"[DEBUG] Number to guess: {number}")

    guess = input("Guess a number ('x'=exit, 's'=show, 'd'=toggle debug): ")

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
