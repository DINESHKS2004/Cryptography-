def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

plaintext = input("Enter plaintext: ").encode()
iv = b'12345678'
key = b'ABCDEFGH'

# Padding
while len(plaintext) % 8 != 0:
    plaintext += b' '

previous = iv
ciphertext = b''

for i in range(0, len(plaintext), 8):
    block = plaintext[i:i+8]
    mixed = xor(block, previous)

    # Simple demonstration encryption (XOR with key)
    encrypted = xor(mixed, key)

    ciphertext += encrypted
    previous = encrypted

print("IV:", iv)
print("Encrypted text:", ciphertext.hex())
