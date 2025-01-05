# File: tests/test_key_management.py

import pytest
import os
from ecvrf.key_management import KeyManager
from ecdsa import SigningKey, VerifyingKey, SECP256k1

@pytest.fixture
def key_manager():
    """
    Fixture to provide a KeyManager instance for tests.
    """
    return KeyManager()

@pytest.fixture
def keypair(key_manager):
    """
    Fixture to generate a key pair for testing.
    """
    private_pem, public_pem = key_manager.generate_keypair()
    return private_pem, public_pem

def test_generate_keypair(key_manager):
    """
    Test key pair generation.
    """
    private_pem, public_pem = key_manager.generate_keypair()
    assert isinstance(private_pem, bytes), "Private key is not bytes."
    assert isinstance(public_pem, bytes), "Public key is not bytes."
    assert private_pem.startswith(b"-----BEGIN"), "Private key PEM format invalid."
    assert public_pem.startswith(b"-----BEGIN"), "Public key PEM format invalid."

def test_load_private_key(key_manager, keypair):
    """
    Test loading of a private key from PEM.
    """
    private_pem, _ = keypair
    private_key = key_manager.load_private_key(private_pem)
    assert isinstance(private_key, SigningKey), "Loaded private key is not a SigningKey instance."
    assert private_key.curve == SECP256k1, "Loaded private key curve mismatch."

def test_load_public_key(key_manager, keypair):
    """
    Test loading of a public key from PEM.
    """
    _, public_pem = keypair
    public_key = key_manager.load_public_key(public_pem)
    assert isinstance(public_key, VerifyingKey), "Loaded public key is not a VerifyingKey instance."
    assert public_key.curve == SECP256k1, "Loaded public key curve mismatch."

def test_save_and_load_keys(key_manager, keypair, tmp_path):
    """
    Test saving keys to files and loading them back.
    """
    private_pem, public_pem = keypair
    private_key = key_manager.load_private_key(private_pem)
    public_key = key_manager.load_public_key(public_pem)
    
    # Define file paths
    private_key_path = tmp_path / "private_key.pem"
    public_key_path = tmp_path / "public_key.pem"
    
    # Save keys
    key_manager.save_private_key(private_key, str(private_key_path))
    key_manager.save_public_key(public_key, str(public_key_path))
    
    assert os.path.exists(private_key_path), "Private key file was not created."
    assert os.path.exists(public_key_path), "Public key file was not created."
    
    # Load keys from files
    loaded_private, loaded_public = key_manager.load_keys_from_files(str(private_key_path), str(public_key_path))
    
    assert loaded_private.to_pem() == private_pem, "Loaded private key does not match original."
    assert loaded_public.to_pem() == public_pem, "Loaded public key does not match original."

def test_load_invalid_private_key(key_manager):
    """
    Test loading an invalid private key.
    """
    invalid_pem = b"-----BEGIN PRIVATE KEY-----\nInvalidKeyData\n-----END PRIVATE KEY-----"
    with pytest.raises(ValueError):
        key_manager.load_private_key(invalid_pem)

def test_load_invalid_public_key(key_manager):
    """
    Test loading an invalid public key.
    """
    invalid_pem = b"-----BEGIN PUBLIC KEY-----\nInvalidKeyData\n-----END PUBLIC KEY-----"
    with pytest.raises(ValueError):
        key_manager.load_public_key(invalid_pem)

def test_save_private_key_with_password(key_manager, keypair, tmp_path):
    """
    Test saving a private key with password encryption.
    """
    private_pem, _ = keypair
    private_key = key_manager.load_private_key(private_pem)
    password = b'securepassword'
    
    # Define file path
    private_key_path = tmp_path / "private_key_encrypted.pem"
    
    # Save encrypted private key
    key_manager.save_private_key(private_key, str(private_key_path), password=password)
    
    assert os.path.exists(private_key_path), "Encrypted private key file was not created."
    
    # Attempt to load the encrypted private key without decryption
    with pytest.raises(ValueError):
        key_manager.load_private_key(private_key_path.read_bytes())
