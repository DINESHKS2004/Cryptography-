
import math

text = input("Enter plaintext: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) != 1:
    print("Invalid value of a")
else:
    result = ""

    for ch in text:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += ch

    print("Ciphertext:", result)
