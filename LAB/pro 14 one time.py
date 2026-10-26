
import random

text = input("Enter plaintext: ").upper()

# Generate a random key for each letter
key = [random.randint(0, 25) for ch in text if ch.isalpha()]

ciphertext = ""
j = 0

for ch in text:
    if ch.isalpha():
        p = ord(ch) - ord('A')
        c = (p + key[j]) % 26
        ciphertext += chr(c + ord('A'))
        j += 1
    else:
        ciphertext += ch

print("Key:", key)
print("Ciphertext:", ciphertext)
