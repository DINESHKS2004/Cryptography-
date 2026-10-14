
text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

result = ""
j = 0

for ch in text:
    if ch.isalpha():
        shift = ord(key[j % len(key)]) - ord('A')
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        j += 1
    else:
        result += ch

print("Ciphertext:", result)
