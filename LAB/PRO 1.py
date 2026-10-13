text = input("Enter text: ")
k = int(input("Enter key (1-25): "))
result = ""

for ch in text:
    if ch.isalpha():
        result += chr((ord(ch.upper()) - 65 + k) % 26 + 65)
    else:
        result += ch

print("Cipher text:", result)
