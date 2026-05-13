import random
import string


alphabet = string.ascii_lowercase


key_list = list(alphabet)
random.shuffle(key_list)
key = "".join(key_list)


encrypt_map = dict(zip(alphabet, key))
decrypt_map = dict(zip(key, alphabet))


message = input("Enter the message - ").lower()




encrypted = ""
for ch in message:
    if ch in encrypt_map:
        encrypted += encrypt_map[ch]
    else:
        encrypted += ch


decrypted = ""
for ch in encrypted:
    if ch in decrypt_map:
        decrypted += decrypt_map[ch]
    else:
        decrypted += ch


print("\nAlphabet Mapping - ")
for a, k in zip(alphabet, key):
    print(a, "->", k)


print("\nEncrypted Message - ", encrypted)
print("Decrypted Message - ", decrypted)
