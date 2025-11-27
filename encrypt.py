import random
import string

# Create the character set
charset = string.ascii_letters + string.digits + string.punctuation

# Create a shuffled version for encryption
shuffled = list(charset)
random.shuffle(shuffled)

# Create encryption and decryption mappings
encrypt_map = dict(zip(charset, shuffled))
decrypt_map = dict(zip(shuffled, charset))

# Get input
plain_text = input("Original message: ")

# Encrypt
encrypted = ''.join(encrypt_map.get(char, char) for char in plain_text)
print(f"Encrypted message: {encrypted}")

# Decrypt (to verify it works)
decrypted = ''.join(decrypt_map.get(char, char) for char in encrypted)
print(f"Decrypted message: {decrypted}")

# Print the key (so you can decrypt later)
print("\nEncryption key:")
print(f"Original:  {charset}")
print(f"Encrypted: {''.join(shuffled)}")