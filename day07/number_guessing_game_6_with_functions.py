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

def game_loop():
    debug_mode = False
    move_mode = False
    number = generate_number()

    while True:
        if debug_mode:
            print(f"[DEBUG] Number to guess: {number}")

        guess_input = input("Guess ('x'=exit, 's'=show, 'd'=debug, 'm'=move, 'n'=new game): ")

        if guess_input == 'x':
            print("Exiting game.")
            break
        elif guess_input == 's':
            show_number(number)
        elif guess_input == 'd':
            debug_mode = toggle_mode(debug_mode)
            print(f"Debug mode {'ON' if debug_mode else 'OFF'}")
        elif guess_input == 'm':
            move_mode = toggle_mode(move_mode)
            print(f"Move mode {'ON' if move_mode else 'OFF'}")
        elif guess_input == 'n':
            print("Starting a new game.")
            number = generate_number()
        elif guess_input.isdigit():
            guess = int(guess_input)
            if process_guess(guess, number):
                number = generate_number()
                print("Starting a new game...")
            if move_mode:
                number = move_number(number)
        else:
            print("Please enter a valid number.")

def main():
    game_loop()

if __name__ == "__main__":
    main()
