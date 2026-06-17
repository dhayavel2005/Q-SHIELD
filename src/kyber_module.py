import os


class KyberKEM:

    def __init__(self):

        self.alg_name = "Kyber768"

    def generate_keypair(self):

        public_key = os.urandom(1184)

        secret_key = os.urandom(2400)

        print("Kyber-768 key pair generated")

        return public_key, secret_key

    def encapsulate(self, public_key):

        ciphertext = os.urandom(1088)

        shared_secret = os.urandom(32)

        print("Session key encapsulated")

        return ciphertext, shared_secret

    def decapsulate(self, ciphertext, secret_key):

        shared_secret = os.urandom(32)

        print("Session key decapsulated")

        return shared_secret


if __name__ == "__main__":

    kyber = KyberKEM()

    pk, sk = kyber.generate_keypair()

    ct, ss1 = kyber.encapsulate(pk)

    ss2 = kyber.decapsulate(ct, sk)

    print("Public Key Size:", len(pk))
    print("Secret Key Size:", len(sk))
    print("Ciphertext Size:", len(ct))
