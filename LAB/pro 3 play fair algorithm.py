
def playfair(text, key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    matrix = ""

    for ch in key + alphabet:
        if ch in alphabet and ch not in matrix:
            matrix += ch

    grid = [matrix[i:i+5] for i in range(0, 25, 5)]
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""

    if len(text) % 2 != 0:
        text += "X"

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        for r in range(5):
            for c in range(5):
                if grid[r][c] == a:
                    r1, c1 = r, c
                if grid[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += grid[r1][(c1+1)%5]
            result += grid[r2][(c2+1)%5]
        elif c1 == c2:
            result += grid[(r1+1)%5][c1]
            result += grid[(r2+1)%5][c2]
        else:
            result += grid[r1][c2] + grid[r2][c1]

    return result

key = input("Enter keyword: ")
text = input("Enter plaintext: ")
print("Ciphertext:", playfair(text, key))
