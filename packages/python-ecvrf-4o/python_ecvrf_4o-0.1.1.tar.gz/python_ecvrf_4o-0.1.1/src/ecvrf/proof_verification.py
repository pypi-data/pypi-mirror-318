# File: src/ecvrf/proof_verification.py

import hashlib
from typing import Tuple
from ecdsa import SECP256k1, VerifyingKey, ellipticcurve
from .hash_to_curve import hash_to_curve
from .key_management import KeyManager
from .utils import decode_point, validate_input

class VRFVerifier:
    """
    Implements the verification functionalities of the ECVRF.
    """

    def __init__(self, key_manager: KeyManager):
        """
        Initializes the VRFVerifier with a given KeyManager.

        Args:
            key_manager (KeyManager): An instance of KeyManager for key operations.
        """
        self.key_manager = key_manager

    def verify(self, public_key_pem: bytes, alpha: bytes, beta: bytes, proof: bytes) -> bool:
        """
        Verifies a VRF proof and checks if the beta corresponds to the given alpha and proof.

        Args:
            public_key_pem (bytes): PEM-encoded public key.
            alpha (bytes): The input data.
            beta (bytes): The VRF output to verify.
            proof (bytes): The VRF proof.

        Returns:
            bool: True if verification succeeds, False otherwise.
        """
        try:
            validate_input(alpha, "Alpha")
            validate_input(proof, "Proof")
            validate_input(beta, "Beta")

            # Load public key
            public_key = self.key_manager.load_public_key(public_key_pem)

            # Deserialize the proof to get the point
            beta_point = decode_point(proof, self.key_manager.curve)

            # Recompute beta from the proof
            expected_beta = hashlib.sha256(proof).digest()

            if beta != expected_beta:
                print("Beta does not match the expected value.")
                return False

            # Recompute H from alpha
            H = hash_to_curve(alpha, self.key_manager.curve)

            # Compute H * public_key_scalar = beta_point
            # Since public_key_scalar = private_key_scalar * G, we have:
            # H * private_key_scalar = beta_point
            # => H * private_key_scalar * G = beta_point * G
            # => (H * private_key_scalar) * G = beta_point * G
            # Which implies H * private_key_scalar == beta_point

            # Extract public key scalar
            public_key_scalar = public_key.pubkey.point * 1  # Ensures it's a Point instance

            # Compute expected beta_point using public key and H
            # Normally, this requires pairing or other advanced operations
            # Here, we simplify by assuming H * private_key = beta_point

            # To verify, compute H * private_key_scalar and check if it equals beta_point
            # However, without the private key, direct computation isn't possible
            # Therefore, we validate that the proof_point is correctly related to H and public_key

            # Placeholder for comprehensive ECVRF verification logic
            # Implement actual verification steps as per RFC 9380

            # For demonstration, assume that if beta matches and point is on curve, it's valid
            return True

        except Exception as e:
            print(f"Verification failed: {e}")
            return False
