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
    sequence = input("Please type in a sequence:\n")
    cleaned_sequences = extract_sequences(sequence)
    print(cleaned_sequences)
