import os
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

class EncryptionService:
    def __init__(self, key):
        if len(key) not in [32]:
            raise ValueError("Key must be 32 bytes long.")
        self.key = key.encode('utf-8')

    def encrypt(self, plain_text):
        if not plain_text:
            return plain_text

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(plain_text.encode('utf-8')) + padder.finalize()

        cipher_bytes = encryptor.update(padded_data) + encryptor.finalize()
        return b64encode(iv + cipher_bytes).decode('utf-8')

    def decrypt(self, cipher_text):
        if not cipher_text:
            return cipher_text

        cipher_data = b64decode(cipher_text.encode('utf-8'))
        iv = cipher_data[:16]
        cipher_bytes = cipher_data[16:]

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        plain_bytes = decryptor.update(cipher_bytes) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plain_bytes = unpadder.update(plain_bytes) + unpadder.finalize()

        return plain_bytes.decode('utf-8')
