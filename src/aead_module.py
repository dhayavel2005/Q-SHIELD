
"""
AEAD Module for Q-SHIELD

Implements:
1. AES-GCM Encryption
2. AES-GCM Decryption

Author: Dhaya R.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class AEADCipher:

    def __init__(self):

        self.mode = AES.MODE_GCM

    def encrypt(self, plaintext, key):

        # AES-256 requires 32-byte key
        key = key[:32]

        cipher = AES.new(key, self.mode)

        ciphertext, tag = cipher.encrypt_and_digest(
            plaintext
        )

        nonce = cipher.nonce

        print("Encryption successful")

        return ciphertext, nonce, tag

    def decrypt(
            self,
            ciphertext,
            nonce,
            tag,
            key):

        key = key[:32]

        cipher = AES.new(
            key,
            self.mode,
            nonce=nonce
        )

        plaintext = cipher.decrypt_and_verify(
            ciphertext,
            tag
        )

        print("Decryption successful")

        return plaintext


if __name__ == "__main__":

    print("========== AES-GCM TEST ==========")

    aead = AEADCipher()

    key = get_random_bytes(32)

    message = b"Hello from Q-SHIELD"

    ct, nonce, tag = aead.encrypt(
        message,
        key
    )

    pt = aead.decrypt(
        ct,
        nonce,
        tag,
        key
    )

    print("\nOriginal Message :",
          message.decode())

    print("Recovered Message:",
          pt.decode())
