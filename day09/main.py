import sys
from color_module import read_colors, print_menu, choose_color

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "examples/files/colors.txt"

colors = read_colors(filename)
if colors is None:
    print(f"Error: The file '{filename}' does not exist.")
    sys.exit(1)

print("Select a color:")
print_menu(colors)

try:
    choice = int(input("Enter the number of your chosen color: "))
    selected = choose_color(colors, choice)
    if selected:
        print(f"You selected: {selected}")
    else:
        print("Error: Number out of range.")
except ValueError:
    print("Error: Please enter a valid whole number.")
