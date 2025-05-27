import sys
import codecs

def apply_rot13_to_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    encoded_content = codecs.encode(content, 'rot_13')

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(encoded_content)

    print(f"ROT13 transformation applied to '{filename}'.")

if __name__ == "__main__":
    apply_rot13_to_file(sys.argv[1])
