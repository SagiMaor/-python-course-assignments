from number_game_utils import (
    generate_number,
    toggle_mode,
    show_number,
    process_guess,
    move_number
)

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
