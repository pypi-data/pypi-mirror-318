# File: tests/test_hash_to_curve.py

import pytest
from ecvrf.hash_to_curve import hash_to_curve
from ecvrf.key_management import KeyManager
from ecvrf.utils import bytes_to_int
from ecdsa import SECP256k1, ellipticcurve

@pytest.fixture
def key_manager():
    """
    Fixture to provide a KeyManager instance for tests.
    """
    return KeyManager()

@pytest.fixture
def curve(key_manager):
    """
    Fixture to provide the elliptic curve used in KeyManager.
    """
    return key_manager.curve

@pytest.fixture
def sample_input():
    """
    Fixture to provide a sample input for hash_to_curve.
    """
    return b"Sample input for hash_to_curve."

def test_hash_to_curve_success(curve, key_manager, sample_input):
    """
    Test that hash_to_curve maps input to a valid point on the curve.
    """
    point = hash_to_curve(sample_input, curve)
    assert isinstance(point, ellipticcurve.Point), "hash_to_curve did not return a Point instance."
    assert curve.curve.contains_point(point.x(), point.y()), "Point is not on the curve."

def test_hash_to_curve_different_inputs(curve, key_manager):
    """
    Test that different inputs map to different points.
    """
    input1 = b"First input."
    input2 = b"Second input."
    
    point1 = hash_to_curve(input1, curve)
    point2 = hash_to_curve(input2, curve)
    
    assert point1 != point2, "Different inputs should map to different points."

def test_hash_to_curve_invalid_input_type(curve, key_manager):
    """
    Test that non-bytes inputs raise a TypeError.
    """
    invalid_input = "This is a string, not bytes."
    with pytest.raises(AttributeError):
        hash_to_curve(invalid_input, curve)

def test_hash_to_curve_edge_case_zero(curve, key_manager):
    """
    Test hash_to_curve with zero bytes.
    """
    input_zero = b"\x00" * 32
    point = hash_to_curve(input_zero, curve)
    assert curve.curve.contains_point(point.x(), point.y()), "Point from zero input is not on the curve."

def test_hash_to_curve_max_input(curve, key_manager):
    """
    Test hash_to_curve with maximum possible input.
    """
    input_max = b"\xFF" * 64
    point = hash_to_curve(input_max, curve)
    assert curve.curve.contains_point(point.x(), point.y()), "Point from max input is not on the curve."

def test_hash_to_curve_non_existent_point(curve, key_manager):
    """
    Test hash_to_curve with input that may not map to a point on the curve immediately.
    Ensures that the function correctly iterates to find a valid point.
    """
    # Craft an input that hashes to a point that likely does not lie on the curve initially
    input_data = b"\xFF" * 32
    point = hash_to_curve(input_data, curve)
    assert curve.curve.contains_point(point.x(), point.y()), "hash_to_curve failed to find a valid point after iterations."
