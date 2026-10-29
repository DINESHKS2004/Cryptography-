key = input("Enter 8-character key: ")

if len(key) != 8:
    print("Key must contain 8 characters")
else:
    binary_key = ''.join(format(ord(c), '08b') for c in key)
    left = binary_key[:28]
    right = binary_key[28:56]

    print("\nInitial Key (56 bits):")
    print(left + right)

    for i in range(1, 17):
        left = left[1:] + left[0]
        right = right[1:] + right[0]

        subkey = left[:24] + right[:24]

        print("K" + str(i) + ":", subkey)
