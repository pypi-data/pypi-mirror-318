import os
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
def encrypt(key, plain_text):
    if not plain_text:
        return plain_text
    
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes long.")
    key_bytes = key.encode('utf-8')

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plain_text.encode('utf-8')) + padder.finalize()

    cipher_bytes = encryptor.update(padded_data) + encryptor.finalize()
    return b64encode(iv + cipher_bytes).decode('utf-8')

def decrypt(key, cipher_text):
    if not cipher_text:
        return cipher_text
        
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes long.")
    key_bytes = key.encode('utf-8')

    cipher_data = b64decode(cipher_text.encode('utf-8'))
    iv = cipher_data[:16]
    cipher_bytes = cipher_data[16:]

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
    decryptor = cipher.decryptor()

    plain_bytes = decryptor.update(cipher_bytes) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plain_bytes = unpadder.update(plain_bytes) + unpadder.finalize()

    return plain_bytes.decode('utf-8')