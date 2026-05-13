def create_matrix(key):
    key = key.upper().replace("J","I")
    matrix = []


    for ch in key:
        if ch not in matrix and ch.isalpha():
            matrix.append(ch)


    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in matrix:
            matrix.append(ch)


    return [matrix[i:i+5] for i in range(0,25,5)]




def find(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i,j




def prepare(text):
    text = text.upper().replace("J","I")
    text = "".join([c for c in text if c.isalpha()])


    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                pairs.append(a+"X")
                i += 1
            else:
                pairs.append(a+b)
                i += 2
        else:
            pairs.append(a+"X")
            i += 1
    return pairs




# encryption
def encrypt(text, key):
    matrix = create_matrix(key)
    pairs = prepare(text)
    result = ""


    for pair in pairs:
        r1,c1 = find(matrix, pair[0])
        r2,c2 = find(matrix, pair[1])


        if r1 == r2:
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]


        elif c1 == c2:
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]


        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]


    return result




# decryption
def decrypt(cipher, key):
    matrix = create_matrix(key)
    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    result = ""


    for pair in pairs:
        r1,c1 = find(matrix, pair[0])
        r2,c2 = find(matrix, pair[1])


        if r1 == r2:
            result += matrix[r1][(c1-1)%5]
            result += matrix[r2][(c2-1)%5]


        elif c1 == c2:
            result += matrix[(r1-1)%5][c1]
            result += matrix[(r2-1)%5][c2]


        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]


    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")


cipher = encrypt(text, key)
print("Encrypted text:", cipher)


plain = decrypt(cipher, key)
print("Decrypted text:", plain)
