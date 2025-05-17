import sys

def extract_sequences(dna):
    valid = "ACTG"
    result = []
    current = ""
    for char in dna:
        if char in valid:
            current += char
        else:
            if current:
                result.append(current)
                current = ""
    if current:
        result.append(current)
    return sorted(result, key=len, reverse=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dna_sequencing.py <sequence>")
        sys.exit(1)

    sequence = sys.argv[1]
    cleaned_sequences = extract_sequences(sequence)
    print(cleaned_sequences)
