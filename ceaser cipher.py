def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result




def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result




message = input("Enter your message - ")
shift_value = int(input("Enter shift value - "))


# Encrypting
encrypted_message = encrypt(message, shift_value)
print("Encrypted Message - ", encrypted_message)


# Decrypting
decrypted_message = decrypt(encrypted_message, shift_value)
print("Decrypted Message - ", decrypted_message)def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result




def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result




message = input("Enter your message - ")
shift_value = int(input("Enter shift value - "))


# Encrypting
encrypted_message = encrypt(message, shift_value)
print("Encrypted Message - ", encrypted_message)


# Decrypting
decrypted_message = decrypt(encrypted_message, shift_value)
print("Decrypted Message - ", decrypted_message)
