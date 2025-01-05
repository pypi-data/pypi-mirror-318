# File: tests/test_proof_generation.py

import pytest
from ecvrf.key_management import KeyManager
from ecvrf.proof_generation import VRF
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
    from ecvrf.proof_verification import VRFVerifier
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
    return b"Sample input for ECVRF."

def test_prove(vrf, keypair, sample_input):
    """
    Test proof and beta generation for a valid input and key pair.
    """
    private_pem, _ = keypair
    beta, proof = vrf.prove(private_pem, sample_input)
    
    assert isinstance(beta, bytes), "Beta is not bytes."
    assert isinstance(proof, bytes), "Proof is not bytes."
    assert len(beta) == 32, "Beta length is incorrect."
    assert len(proof) == 65, "Proof length is incorrect."  # 1 byte prefix + 64 bytes coordinates

def test_prove_consistency(vrf, keypair, sample_input):
    """
    Test that proof generation is deterministic for the same input and key pair.
    """
    private_pem, _ = keypair
    beta1, proof1 = vrf.prove(private_pem, sample_input)
    beta2, proof2 = vrf.prove(private_pem, sample_input)
    
    assert beta1 == beta2, "Beta outputs are not consistent."
    assert proof1 == proof2, "Proofs are not consistent."

def test_prove_different_inputs(vrf, keypair):
    """
    Test that different inputs produce different betas and proofs.
    """
    private_pem, _ = keypair
    input1 = b"First input."
    input2 = b"Second input."
    
    beta1, proof1 = vrf.prove(private_pem, input1)
    beta2, proof2 = vrf.prove(private_pem, input2)
    
    assert beta1 != beta2, "Different inputs should produce different betas."
    assert proof1 != proof2, "Different inputs should produce different proofs."

def test_prove_invalid_input(vrf, keypair):
    """
    Test proof generation with invalid (empty) input.
    """
    private_pem, _ = keypair
    invalid_input = b""
    with pytest.raises(ValueError):
        vrf.prove(private_pem, invalid_input)

def test_prove_invalid_private_key(vrf, sample_input):
    """
    Test proof generation with an invalid private key.
    """
    invalid_private_pem = b"-----BEGIN PRIVATE KEY-----\nInvalidKeyData\n-----END PRIVATE KEY-----"
    with pytest.raises(ValueError):
        vrf.prove(invalid_private_pem, sample_input)
