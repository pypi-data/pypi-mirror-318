# File: src/ecvrf/key_management.py

from ecdsa import SECP256k1, SigningKey, VerifyingKey
from ecdsa.util import sigencode_string, sigdecode_string
from cryptography.hazmat.primitives import serialization
from typing import Tuple
import os

class KeyManager:
    """
    Manages ECVRF key generation, serialization, and deserialization.
    """

    def __init__(self, curve: str = "SECP256k1"):
        """
        Initializes the KeyManager with the specified elliptic curve.

        Args:
            curve (str): The name of the elliptic curve to use.
                         Supported: "SECP256k1"
        """
        if curve != "SECP256k1":
            raise ValueError("Unsupported curve. Currently, only SECP256k1 is supported.")
        self.curve = SECP256k1

    def generate_keypair(self) -> Tuple[bytes, bytes]:
        """
        Generates a new ECVRF key pair.

        Returns:
            Tuple[bytes, bytes]: A tuple containing the private key and public key in PEM format.
        """
        private_key = SigningKey.generate(curve=self.curve)
        public_key = private_key.get_verifying_key()
        pem_private = private_key.to_pem()
        pem_public = public_key.to_pem()
        return pem_private, pem_public

    def load_private_key(self, pem_private: bytes) -> SigningKey:
        """
        Loads a private key from its PEM-encoded form.

        Args:
            pem_private (bytes): The PEM-encoded private key.

        Returns:
            SigningKey: The loaded private key object.
        """
        try:
            private_key = SigningKey.from_pem(pem_private)
            if private_key.curve != self.curve:
                raise ValueError("Private key curve does not match KeyManager curve.")
            return private_key
        except Exception as e:
            raise ValueError(f"Invalid private key PEM format: {e}")

    def load_public_key(self, pem_public: bytes) -> VerifyingKey:
        """
        Loads a public key from its PEM-encoded form.

        Args:
            pem_public (bytes): The PEM-encoded public key.

        Returns:
            VerifyingKey: The loaded public key object.
        """
        try:
            public_key = VerifyingKey.from_pem(pem_public)
            if public_key.curve != self.curve:
                raise ValueError("Public key curve does not match KeyManager curve.")
            return public_key
        except Exception as e:
            raise ValueError(f"Invalid public key PEM format: {e}")

    def save_private_key(self, private_key: SigningKey, filepath: str, password: bytes = None) -> None:
        """
        Saves the private key to a file in PEM format, optionally encrypted with a password.

        Args:
            private_key (SigningKey): The private key to save.
            filepath (str): The path to the file where the key will be saved.
            password (bytes, optional): Password to encrypt the private key. Defaults to None.
        """
        encryption_algorithm = serialization.NoEncryption()
        if password:
            from cryptography.hazmat.primitives import serialization as crypto_serialization
            encryption_algorithm = crypto_serialization.BestAvailableEncryption(password)
        
        pem_private = private_key.to_pem()
        with open(filepath, "wb") as f:
            f.write(pem_private)

    def save_public_key(self, public_key: VerifyingKey, filepath: str) -> None:
        """
        Saves the public key to a file in PEM format.

        Args:
            public_key (VerifyingKey): The public key to save.
            filepath (str): The path to the file where the key will be saved.
        """
        pem_public = public_key.to_pem()
        with open(filepath, "wb") as f:
            f.write(pem_public)

    def load_keys_from_files(self, private_key_path: str, public_key_path: str) -> Tuple[SigningKey, VerifyingKey]:
        """
        Loads private and public keys from their respective files.

        Args:
            private_key_path (str): Path to the PEM-encoded private key file.
            public_key_path (str): Path to the PEM-encoded public key file.

        Returns:
            Tuple[SigningKey, VerifyingKey]: The loaded private and public key objects.
        """
        if not os.path.exists(private_key_path):
            raise FileNotFoundError(f"Private key file not found: {private_key_path}")
        if not os.path.exists(public_key_path):
            raise FileNotFoundError(f"Public key file not found: {public_key_path}")

        with open(private_key_path, "rb") as f:
            pem_private = f.read()
        with open(public_key_path, "rb") as f:
            pem_public = f.read()

        private_key = self.load_private_key(pem_private)
        public_key = self.load_public_key(pem_public)
        return private_key, public_key
