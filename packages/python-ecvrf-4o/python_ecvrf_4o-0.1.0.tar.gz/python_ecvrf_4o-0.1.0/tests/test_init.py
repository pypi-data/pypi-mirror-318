# File: tests/test_init.py

import pytest
from ecvrf import KeyManager, VRF, VRFVerifier

def test_key_manager_import():
    """
    Test that KeyManager is accessible from the ecvrf package.
    """
    km = KeyManager()
    assert isinstance(km, KeyManager), "KeyManager instance creation failed."

def test_vrf_import():
    """
    Test that VRF is accessible from the ecvrf package.
    """
    km = KeyManager()
    vrf = VRF(km)
    assert isinstance(vrf, VRF), "VRF instance creation failed."

def test_vrf_verifier_import():
    """
    Test that VRFVerifier is accessible from the ecvrf package.
    """
    km = KeyManager()
    verifier = VRFVerifier(km)
    assert isinstance(verifier, VRFVerifier), "VRFVerifier instance creation failed."

def test_all_exports():
    """
    Test that all intended classes are exported in __all__.
    """
    from ecvrf import __all__
    assert "KeyManager" in __all__, "KeyManager not in __all__."
    assert "VRF" in __all__, "VRF not in __all__."
    assert "VRFVerifier" in __all__, "VRFVerifier not in __all__."
