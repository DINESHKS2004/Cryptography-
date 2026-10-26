
keyword = "CIPHER"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Generate cipher sequence
cipher = ""

for ch in keyword + alphabet:
    if ch not in cipher:
        cipher += ch

print("Plain alphabet :", alphabet)
print("Cipher alphabet:", cipher)

text = input("Enter plaintext: ").upper()
result = ""

for ch in text:
    if ch in alphabet:
        result += cipher[alphabet.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)
