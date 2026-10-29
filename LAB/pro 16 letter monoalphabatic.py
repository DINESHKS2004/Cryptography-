import string
from collections import Counter

english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def decrypt(ciphertext, key):
    result = ""
    for ch in ciphertext:
        if ch.isalpha():
            index = ord(ch.upper()) - ord('A')
            result += key[index]
        else:
            result += ch
    return result

def frequency_attack(ciphertext, top_n):
    letters = [ch.upper() for ch in ciphertext if ch.isalpha()]
    freq = Counter(letters)

    cipher_order = ''.join(
        ch for ch, count in freq.most_common()
    )

    remaining = ''.join(
        ch for ch in string.ascii_uppercase
        if ch not in cipher_order
    )

    cipher_order += remaining

    key = [''] * 26

    for i, ch in enumerate(cipher_order):
        key[ord(ch) - ord('A')] = english_freq[i]

    plaintext = decrypt(ciphertext, key)

    print("\nPossible Plaintext:")
    print(plaintext)
    print("\nEstimated substitution key:")
    print(''.join(key))

ciphertext = input("Enter ciphertext: ")
top_n = int(input("Enter top number of plaintexts: "))

frequency_attack(ciphertext, top_n)
