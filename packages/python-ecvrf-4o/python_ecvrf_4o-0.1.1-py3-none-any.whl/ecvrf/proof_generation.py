# File: src/ecvrf/proof_generation.py

import hashlib
from typing import Tuple
from ecdsa import SECP256k1, SigningKey, ellipticcurve
from .key_management import KeyManager
from .hash_to_curve import hash_to_curve
from .utils import encode_point, validate_input

class VRF:
    """
    Implements the ECVRF (Elliptic Curve Verifiable Random Function) functionalities.
    """

    def __init__(self, key_manager: KeyManager):
        """
        Initializes the VRF with a given KeyManager.

        Args:
            key_manager (KeyManager): An instance of KeyManager for key operations.
        """
        self.key_manager = key_manager

    def prove(self, private_key_pem: bytes, alpha: bytes) -> Tuple[bytes, bytes]:
        """
        Generates a VRF proof and the corresponding output (beta) for a given input alpha.

        Args:
            private_key_pem (bytes): PEM-encoded private key.
            alpha (bytes): The input data.

        Returns:
            Tuple[bytes, bytes]: A tuple containing beta and the proof, both in bytes.
        """
        validate_input(alpha, "Alpha")
        private_key = self.key_manager.load_private_key(private_key_pem)
        public_key = private_key.get_verifying_key()

        # Step 1: Hash alpha to a point on the curve
        H = hash_to_curve(alpha, self.key_manager.curve)

        # Step 2: Multiply H by the private key scalar to get the VRF output point
        beta_point = H * private_key.privkey.secret_multiplier

        # Step 3: Serialize the proof (beta_point)
        proof = encode_point(beta_point)

        # Step 4: Compute beta as the hash of the proof
        beta = hashlib.sha256(proof).digest()

        return beta, proof
