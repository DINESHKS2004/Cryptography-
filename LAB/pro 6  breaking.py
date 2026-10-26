import math

ciphertext = input("Enter ciphertext: ").upper()

# Most frequent ciphertext letters
c1 = ord('B') - ord('A')  # B = 1
c2 = ord('U') - ord('A')  # U = 20

# Assume most frequent plaintext letters are E and T
p1 = ord('E') - ord('A')  # E = 4
p2 = ord('T') - ord('A')  # T = 19

for a in range(1, 26):
    if math.gcd(a, 26) == 1:
        b = (c1 - a * p1) % 26

        if (a * p2 + b) % 26 == c2:
            a_inv = pow(a, -1, 26)
            result = ""

            for ch in ciphertext:
                if ch.isalpha():
                    c = ord(ch) - ord('A')
                    p = (a_inv * (c - b)) % 26
                    result += chr(p + ord('A'))
                else:
                    result += ch

            print("a =", a, "b =", b)
            print("Plaintext:", result)
