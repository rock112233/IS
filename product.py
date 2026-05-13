# Caesar Cipher Encryption
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


# Rail Fence Cipher Encryption
def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]

    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)

        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    ciphertext = ""

    for row in fence:
        ciphertext += ''.join(row)

    return ciphertext


# Product Cipher
plaintext = "HELLOWORLD"

# Step 1: Caesar Cipher
step1 = caesar_encrypt(plaintext, 3)

# Step 2: Rail Fence Cipher
final_cipher = rail_fence_encrypt(step1, 3)

print("Plaintext           :", plaintext)
print("After Caesar Cipher :", step1)
print("Final Product Cipher:", final_cipher)
