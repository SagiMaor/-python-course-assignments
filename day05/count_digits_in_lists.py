numbers = [1203, 1256, 312456, 98]

digit_count = {str(d): 0 for d in range(10)}

for number in numbers:
    for digit in str(number):
        digit_count[digit] += 1

for digit in sorted(digit_count.keys()):
    print(f"{digit} {digit_count[digit]}")
