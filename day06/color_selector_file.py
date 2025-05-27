import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "examples/files/colors.txt"  # Default file

try:
    with open(filename, 'r') as file:
        colors = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
    sys.exit(1)

print("Select a color:")
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")

try:
    choice = int(input("Enter the number of your chosen color: "))
    if 1 <= choice <= len(colors):
        print(f"You selected: {colors[choice - 1]}")
    else:
        print("Error: Number out of range.")
except ValueError:
    print("Error: Please enter a valid whole number.")
