import sys

if len(sys.argv) != 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)

height = float(sys.argv[1])
width = float(sys.argv[2])

area = height * width
perimeter = 2 * (height + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
