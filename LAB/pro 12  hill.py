
import math

key = [[9, 4], [5, 7]]

def encrypt(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())

    if len(text) % 2 != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - ord('A')
        p2 = ord(text[i + 1]) - ord('A')

        c1 = (9 * p1 + 4 * p2) % 26
        c2 = (5 * p1 + 7 * p2) % 26

        result += chr(c1 + 65) + chr(c2 + 65)

    return result


def decrypt(ciphertext):
    # Determinant = 9*7 - 4*5 = 43 = 17 mod 26
    # Inverse of 17 mod 26 is 23
    inverse_key = [[5, 12], [15, 25]]

    result = ""

    for i in range(0, len(ciphertext), 2):
        c1 = ord(ciphertext[i]) - 65
        c2 = ord(ciphertext[i + 1]) - 65

        p1 = (5 * c1 + 12 * c2) % 26
        p2 = (15 * c1 + 25 * c2) % 26

        result += chr(p1 + 65) + chr(p2 + 65)

    return result


plaintext = input("Enter plaintext: ")

ciphertext = encrypt(plaintext)
print("Encrypted ciphertext:", ciphertext)

recovered = decrypt(ciphertext)
print("Decrypted plaintext:", recovered)
