from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_data(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(text.encode(), 16))
    return encrypted

def decrypt_data(encrypted_data, key):
    """
    Decrypts data that was encrypted using AES in ECB mode.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode()

# Example usage
key = b'1234567890abcdef'  # 16-byte key
text = "Hi, Arif!"
encrypted = encrypt_data(text, key)
print("Encrypted:", encrypted.hex())
decrypted = decrypt_data(encrypted, key)
print("Decrypted:", decrypted)
