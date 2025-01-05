# File: tests/test_proof_verification.py

import pytest
from ecvrf.key_management import KeyManager
from ecvrf.proof_generation import VRF
from ecvrf.proof_verification import VRFVerifier
from ecvrf.utils import generate_secure_random_bytes

@pytest.fixture
def vrf(key_manager):
    """
    Fixture to provide a VRF instance for tests.
    """
    return VRF(key_manager)

@pytest.fixture
def verifier(key_manager):
    """
    Fixture to provide a VRFVerifier instance for tests.
    """
    return VRFVerifier(key_manager)

@pytest.fixture
def keypair(key_manager):
    """
    Fixture to generate a key pair for testing.
    """
    private_pem, public_pem = key_manager.generate_keypair()
    return private_pem, public_pem

@pytest.fixture
def sample_input():
    """
    Fixture to provide a sample input for VRF.
    """
    return b"Sample input for ECVRF verification."

def test_verify_valid_proof(verifier, vrf, keypair, sample_input):
    """
    Test verification of a valid proof.
    """
    private_pem, public_pem = keypair
    beta, proof = vrf.prove(private_pem, sample_input)
    is_valid = verifier.verify(public_pem, sample_input, beta, proof)
    assert is_valid, "Valid proof failed to verify."

def test_verify_invalid_proof_wrong_beta(verifier, vrf, keypair, sample_input):
    """
    Test verification fails when beta does not match the proof.
    """
    private_pem, public_pem = keypair
    beta, proof = vrf.prove(private_pem, sample_input)
    tampered_beta = generate_secure_random_bytes(32)
    is_valid = verifier.verify(public_pem, sample_input, tampered_beta, proof)
    assert not is_valid, "Verification should fail with incorrect beta."

def test_verify_invalid_proof_tampered_proof(verifier, vrf, keypair, sample_input):
    """
    Test verification fails when the proof is tampered.
    """
    private_pem, public_pem = keypair
    beta, proof = vrf.prove(private_pem, sample_input)
    tampered_proof = bytearray(proof)
    tampered_proof[0] ^= 0xFF  # Flip bits to tamper
    tampered_proof = bytes(tampered_proof)
    is_valid = verifier.verify(public_pem, sample_input, beta, tampered_proof)
    assert not is_valid, "Verification should fail with tampered proof."

def test_verify_invalid_proof_wrong_input(verifier, vrf, keypair, sample_input):
    """
    Test verification fails when the input alpha does not match the proof.
    """
    private_pem, public_pem = keypair
    beta, proof = vrf.prove(private_pem, sample_input)
    wrong_input = b"Different input for VRF."
    is_valid = verifier.verify(public_pem, wrong_input, beta, proof)
    assert not is_valid, "Verification should fail with incorrect input."

def test_verify_invalid_public_key(verifier, vrf, keypair, sample_input, key_manager):
    """
    Test verification fails when using an incorrect public key.
    """
    private_pem, public_pem = keypair
    beta, proof = vrf.prove(private_pem, sample_input)
    
    # Generate a different key pair
    other_private_pem, other_public_pem = key_manager.generate_keypair()
    
    is_valid = verifier.verify(other_public_pem, sample_input, beta, proof)
    assert not is_valid, "Verification should fail with incorrect public key."

def test_verify_with_invalid_proof_format(verifier, keypair, sample_input):
    """
    Test verification fails when the proof format is invalid.
    """
    _, public_pem = keypair
    beta = generate_secure_random_bytes(32)
    invalid_proof = b"InvalidProofFormat"
    with pytest.raises(ValueError):
        verifier.verify(public_pem, sample_input, beta, invalid_proof)
