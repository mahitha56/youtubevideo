from Crypto.Cipher import AES

# Rijndael (AES-128) Key and Plaintext
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")

# Create AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
ciphertext = cipher.encrypt(plaintext)

print("Plaintext :", plaintext.hex())
print("Ciphertext:", ciphertext.hex())