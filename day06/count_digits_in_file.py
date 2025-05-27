digit_counts = {str(d): 0 for d in range(10)}

with open("examples/files/numbers.txt", "r") as file:
    content = file.read()

for char in content:
    if char.isdigit():
        digit_counts[char] += 1

with open("report.txt", "w") as report:
    for digit in sorted(digit_counts.keys()):
        report.write(f"{digit} {digit_counts[digit]}\n")
