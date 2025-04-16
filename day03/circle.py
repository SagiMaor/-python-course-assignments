import sys
import math

if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

radius = float(sys.argv[1])

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area}")
print(f"Circumference: {circumference}")
