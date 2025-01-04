# zscryptography

A simple encryption library using AES.

## Installation

```bash
pip install zscryptography
```
## Usage
```xml
from zscryptography import *

# Setup key(32 bytes)
key = "thisisaverysecretkey123456789012"

# Encrypt the plaintext
plain_text = "Hello, World!"
encrypted_text = encrypt(key,plain_text)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = decrypt(key,encrypted_text)
print(f"Decrypted: {decrypted_text}")
```