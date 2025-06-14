
def read_colors(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return None

def print_menu(colors):
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")

def choose_color(colors, index):
    if 1 <= index <= len(colors):
        return colors[index - 1]
    return None
