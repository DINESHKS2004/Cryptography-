
def decrypt_playfair(ciphertext, key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for ch in key + alphabet:
        if ch in alphabet and ch not in matrix:
            matrix.append(ch)

    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_pos(ch):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == ch:
                    return r, c

    ciphertext = "".join(
        ch for ch in ciphertext.upper() if ch.isalpha()
    ).replace("J", "I")

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        r1, c1 = find_pos(a)
        r2, c2 = find_pos(b)

        if r1 == r2:
            plaintext += matrix[r1][(c1-1) % 5]
            plaintext += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1-1) % 5][c1]
            plaintext += matrix[(r2-1) % 5][c2]
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


ciphertext = """
KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ
"""

key = input("Enter Playfair key: ")
print("Decrypted message:")
print(decrypt_playfair(ciphertext, key))
