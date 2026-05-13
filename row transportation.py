def row_transposition_encrypt(message, key):
    cols = len(key)
    
    # Add padding if needed
    while len(message) % cols != 0:
        message += 'X'

    rows = len(message) // cols

    # Create matrix
    matrix = []
    k = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(message[k])
            k += 1
        matrix.append(row)

    # Arrange columns according to sorted key
    ciphertext = ""

    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])

    for col_index, _ in key_order:
        for row in matrix:
            ciphertext += row[col_index]

    return ciphertext


message = "HELLOWORLD"
key = [3, 1, 4, 2]

encrypted = row_transposition_encrypt(message, key)

print("Plaintext :", message)
print("Ciphertext:", encrypted)
