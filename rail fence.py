def encryptRailFence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]


    dir_down = False
    row, col = 0, 0


    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down


        rail[row][col] = text[i]
        col += 1


        row += 1 if dir_down else -1


    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])


    return "".join(result)




def decryptRailFence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]


    dir_down = None
    row, col = 0, 0


    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False


        rail[row][col] = '*'
        col += 1


        row += 1 if dir_down else -1


    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1


    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False


        result.append(rail[row][col])
        col += 1


        row += 1 if dir_down else -1


    return "".join(result)




choice = input("Enter E for Encryption or D for Decryption - ").upper()


text = input("Enter text - ")
key = int(input("Enter key (number of rails) - "))


if choice == 'E':
    print("Cipher Text - ", encryptRailFence(text, key))
elif choice == 'D':
    print("Original Text - ", decryptRailFence(text, key))
else:
    print("Invalid choice!")
