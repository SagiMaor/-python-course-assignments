input_text = """Lorem ipsum dolor qui ad labor ad labor sint dolor  tempor incididunt ut labor ad dolore lorem ad
Ut labor ad dolor lorem qui ad ut labor   ut ad commodo commodo
Lorem ad dolor in reprehenderit in lorem ut labor ad dolore eu in labor dolor
sint occaecat ad labor proident sint in in qui labor ad dolor ad in ad labor
"""

file_in = 'examples/dictionary/words_and_spaces.txt'
file_out = 'examples/dictionary/words_and_spaces_counted.txt'

import os
os.makedirs(os.path.dirname(file_in), exist_ok=True)

with open(file_in, 'w') as f:
    f.write(input_text)

with open(file_in, 'r') as f:
    text = f.read()

words = text.lower().split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

with open(file_out, 'w') as f:
    for word in sorted(counts):
        f.write(f"{word.ljust(14)}{counts[word]}\n")
