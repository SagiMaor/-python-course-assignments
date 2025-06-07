file_in = 'examples/dictionary/words_and_spaces.txt'
file_out = 'examples/dictionary/words_and_spaces_counted.txt'

with open(file_in, 'r') as f:
    text = f.read()

words = text.lower().split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

with open(file_out, 'w') as f:
    for word in sorted(counts):
        f.write(f"{word.ljust(14)}{counts[word]}\n")
