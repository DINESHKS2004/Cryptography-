plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter plaintext: ").upper()
result = ""

for ch in text:
    if ch in plain:
        result += cipher[plain.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)
