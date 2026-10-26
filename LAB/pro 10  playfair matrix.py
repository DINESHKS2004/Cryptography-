
matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

def find_position(ch):
    if ch == 'J':
        ch = 'I'
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

def prepare_text(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace('J', 'I')
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            b = 'X'
            i += 1
        elif text[i] == text[i + 1]:
            b = 'X'
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append(a + b)

    return pairs

def encrypt(text):
    pairs = prepare_text(text)
    result = ''

    for pair in pairs:
        r1, c1 = find_position(pair[0])
        r2, c2 = find_position(pair[1])

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

message = "Must see you over Cadogan West. Coming at once."
print("Plaintext:", message)
print("Ciphertext:", encrypt(message))
