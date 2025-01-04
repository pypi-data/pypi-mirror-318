# zscryptography

A simple encryption library using AES.

## Installation

```bash
pip install zscryptography
```
## Usage
```xml
from zscryptography import *

# Initialize the encryption service with a secure key(32 bytes)
key = "thisisaverysecretkey123456789012"
encryptor = EncryptionService(key)

# Encrypt the plaintext
plain_text = "Hello, World!"
encrypted_text = encryptor.encrypt(plain_text)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = encryptor.decrypt(encrypted_text)
print(f"Decrypted: {decrypted_text}")
```