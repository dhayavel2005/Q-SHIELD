"""
Kyber-768 Module for Q-SHIELD

Implements:
1. Key Generation
2. Encapsulation
3. Decapsulation

Uses:
- Open Quantum Safe (OQS)
- liboqs-python
"""

import oqs


class KyberKEM:

    def __init__(self):

        self.alg_name = "Kyber768"

    def generate_keypair(self):

        kem = oqs.KeyEncapsulation(self.alg_name)

        public_key = kem.generate_keypair()

        secret_key = kem.export_secret_key()

        print("Key pair generated successfully")

        return public_key, secret_key

    def encapsulate(self, public_key):

        kem = oqs.KeyEncapsulation(self.alg_name)

        ciphertext, shared_secret = kem.encap_secret(
            public_key
        )

        print("Session key encapsulated")

        return ciphertext, shared_secret

    def decapsulate(self, ciphertext, secret_key):

        kem = oqs.KeyEncapsulation(self.alg_name)

        kem.import_secret_key(secret_key)

        shared_secret = kem.decap_secret(
            ciphertext
        )

        print("Session key recovered")

        return shared_secret


if __name__ == "__main__":

    print("========== KYBER-768 TEST ==========")

    kyber = KyberKEM()

    pk, sk = kyber.generate_keypair()

    ct, ss1 = kyber.encapsulate(pk)

    ss2 = kyber.decapsulate(ct, sk)

    print("\nSender Secret : ", ss1.hex()[:32])
    print("Receiver Secret :", ss2.hex()[:32])

    if ss1 == ss2:
        print("\nSUCCESS: Shared secrets match")
    else:
        print("\nERROR: Shared secrets do not match")
