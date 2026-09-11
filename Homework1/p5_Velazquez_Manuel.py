def caesar_cipher(text, shift):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""

    for character in text:

        if character in lowercase:
            old_index = lowercase.index(character)
            new_index = (old_index + shift) % 26
            result += lowercase[new_index]

        elif character in uppercase:
            old_index = uppercase.index(character)
            new_index = (old_index + shift) % 26
            result += uppercase[new_index]

        else:
            # Keep spaces, punctuation, and numbers unchanged.
            result += character

    return result


def caesar_decipher(cyphertext, shift):
    # Decryption is just the opposite shift.
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    frequencies = {}

    # Start every letter at zero.
    for letter in alphabet:
        frequencies[letter] = 0

    # Count letters.
    for character in text.lower():
        if character in alphabet:
            frequencies[character] += 1

    return frequencies


def main():
    print("Caesar Cipher Program")
    print()

    message = input("Enter a message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_cipher(message, shift)

    print()
    print("Encrypted text:")
    print(encrypted)

    print()
    print("Letter frequencies:")

    frequencies = letter_frequency(message)

    for letter in frequencies:
        print("{}: {}".format(letter, frequencies[letter]))

    decrypted = caesar_decipher(encrypted, shift)

    print()
    print("Decrypted text:")
    print(decrypted)


if __name__ == "__main__":
    main()