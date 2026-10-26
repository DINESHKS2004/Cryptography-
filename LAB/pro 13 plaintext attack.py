
import numpy as np

MOD = 26

def mod_inverse_matrix(matrix):
    det = int(round(np.linalg.det(matrix))) % MOD
    det_inv = pow(det, -1, MOD)

    adj = np.array([
        [matrix[1, 1], -matrix[0, 1]],
        [-matrix[1, 0], matrix[0, 0]]
    ])

    return (det_inv * adj) % MOD


def text_to_numbers(text):
    return [ord(ch) - ord('A') for ch in text.upper() if ch.isalpha()]


# Known plaintext and corresponding ciphertext
plaintext = "HELP"
ciphertext = "HIAT"

p = text_to_numbers(plaintext)
c = text_to_numbers(ciphertext)

# Form matrices using pairs of letters as columns
P = np.array([[p[0], p[2]],
              [p[1], p[3]]])

C = np.array([[c[0], c[2]],
              [c[1], c[3]]])

try:
    P_inv = mod_inverse_matrix(P)
    key = (C @ P_inv) % MOD

    print("Recovered Hill Cipher Key:")
    print(key)

    print("Key matrix recovered successfully.")

except ValueError:
    print("Cannot recover key: plaintext matrix is not invertible modulo 26.")
