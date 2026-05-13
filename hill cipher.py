def getKeyMatrix(key):
    keyMatrix = [[0]*3 for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix




# Function to multiply matrices
def multiplyMatrix(a, b):
    result = [0]*3
    for i in range(3):
        for j in range(3):
            result[i] += a[i][j] * b[j]
        result[i] %= 26
    return result


def encrypt(message, key):
    keyMatrix = getKeyMatrix(key)


    message = message.upper()
    messageVector = [ord(c) % 65 for c in message]


    cipherVector = multiplyMatrix(keyMatrix, messageVector)


    cipherText = "".join(chr(c + 65) for c in cipherVector)
    return cipherText




def modInverse(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return -1




def inverseKey(keyMatrix):
    invKey = [[0]*3 for _ in range(3)]


    # Determinant
    det = (keyMatrix[0][0]*(keyMatrix[1][1]*keyMatrix[2][2] - keyMatrix[1][2]*keyMatrix[2][1])
          -keyMatrix[0][1]*(keyMatrix[1][0]*keyMatrix[2][2] - keyMatrix[1][2]*keyMatrix[2][0])
          +keyMatrix[0][2]*(keyMatrix[1][0]*keyMatrix[2][1] - keyMatrix[1][1]*keyMatrix[2][0]))


    det = det % 26
    invDet = modInverse(det)


    if invDet == -1:
        print("Key is not invertible!")
        return None


    invKey[0][0] = (keyMatrix[1][1]*keyMatrix[2][2] - keyMatrix[1][2]*keyMatrix[2][1]) * invDet % 26
    invKey[0][1] = (keyMatrix[0][2]*keyMatrix[2][1] - keyMatrix[0][1]*keyMatrix[2][2]) * invDet % 26
    invKey[0][2] = (keyMatrix[0][1]*keyMatrix[1][2] - keyMatrix[0][2]*keyMatrix[1][1]) * invDet % 26


    invKey[1][0] = (keyMatrix[1][2]*keyMatrix[2][0] - keyMatrix[1][0]*keyMatrix[2][2]) * invDet % 26
    invKey[1][1] = (keyMatrix[0][0]*keyMatrix[2][2] - keyMatrix[0][2]*keyMatrix[2][0]) * invDet % 26
    invKey[1][2] = (keyMatrix[0][2]*keyMatrix[1][0] - keyMatrix[0][0]*keyMatrix[1][2]) * invDet % 26


    invKey[2][0] = (keyMatrix[1][0]*keyMatrix[2][1] - keyMatrix[1][1]*keyMatrix[2][0]) * invDet % 26
    invKey[2][1] = (keyMatrix[0][1]*keyMatrix[2][0] - keyMatrix[0][0]*keyMatrix[2][1]) * invDet % 26
    invKey[2][2] = (keyMatrix[0][0]*keyMatrix[1][1] - keyMatrix[0][1]*keyMatrix[1][0]) * invDet % 26


    return invKey


def decrypt(cipher, key):
    keyMatrix = getKeyMatrix(key)
    invKey = inverseKey(keyMatrix)


    if invKey is None:
        return "Decryption not possible"


    cipherVector = [ord(c) % 65 for c in cipher]


    messageVector = multiplyMatrix(invKey, cipherVector)


    message = "".join(chr(c + 65) for c in messageVector)
    return message


message = input("Enter 3-letter plaintext: ")
key = input("Enter 9-letter key: ")


if len(message) != 3 or len(key) != 9:
    print("Invalid input length!")
else:
    cipher = encrypt(message, key)
    print("Encrypted Text:", cipher)


    decrypted = decrypt(cipher, key)
    print("Decrypted Text:", decrypted)
