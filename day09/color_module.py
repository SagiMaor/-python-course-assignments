
def read_colors(filename):
    """Reads non-empty lines from a file and returns a list.

    Example:
    >>> read_colors("examples/files/sample.txt")
    ['Red', 'Green', 'Blue']
    """
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return None

def print_menu(colors):
    """Prints a numbered list of colors."""
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")

def choose_color(colors, index):
    """Returns the selected color from a list.

    Example:
    >>> choose_color(["Red", "Green", "Blue"], 2)
    'Green'
    """
    if 1 <= index <= len(colors):
        return colors[index - 1]
    return None
