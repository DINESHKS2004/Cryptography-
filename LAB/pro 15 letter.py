
from collections import Counter

def frequency_attack(ciphertext, top_n):
    ciphertext = ciphertext.upper()
    results = []

    # Try all 26 possible shift keys
    for key in range(26):
        plaintext = ""

        for ch in ciphertext:
            if ch.isalpha():
                p = (ord(ch) - ord('A') - key) % 26
                plaintext += chr(p + ord('A'))
            else:
                plaintext += ch

        # Score plaintext using common English letters
        freq = Counter(ch for ch in plaintext if ch.isalpha())
        score = sum(freq[ch] * weight for ch, weight in {
            'E': 13, 'T': 9, 'A': 8, 'O': 8, 'I': 7,
            'N': 7, 'S': 6, 'H': 6, 'R': 6
        }.items())

        results.append((score, key, plaintext))

    # Highest score first
    results.sort(reverse=True)

    print("\nTop possible plaintexts:")
    for i, (score, key, plaintext) in enumerate(results[:top_n], 1):
        print(f"{i}. Key={key}, Score={score}: {plaintext}")


ciphertext = input("Enter ciphertext: ")
top_n = int(input("How many possible plaintexts? "))

if 1 <= top_n <= 26:
    frequency_attack(ciphertext, top_n)
else:
    print("Enter a number between 1 and 26.")
