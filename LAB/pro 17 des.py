key = input("Enter 8-character key: ")
ciphertext = input("Enter ciphertext: ")

keys = []

for i in range(16):
    keys.append(key[i % len(key):] + key[:i % len(key)])

print("\nDecryption Key Order:")

for i in range(15, -1, -1):
    print("K" + str(i + 1), "=", keys[i])

print("\nDES decryption uses keys in reverse order:")
print("K16, K15, K14, ..., K1")
print("Result: Reverse key schedule generated.")
