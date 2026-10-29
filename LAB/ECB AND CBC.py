def xor(a, b):
    return ''.join('1' if x != y else '0'
                   for x, y in zip(a, b))

def encrypt(block, key):
    return xor(block, key)

key = "1010"
p1 = input("Enter P1 (4 bits): ")
p2 = input("Enter P2 (4 bits): ")

# ECB Mode
c1 = encrypt(p1, key)
c2 = encrypt(p2, key)

print("\nECB Mode:")
print("C1 =", c1)
print("C2 =", c2)

# CBC Mode
iv = "1100"
c1_cbc = encrypt(xor(p1, iv), key)
c2_cbc = encrypt(xor(p2, c1_cbc), key)

print("\nCBC Mode:")
print("C1 =", c1_cbc)
print("C2 =", c2_cbc)
