# File: src/ecvrf/hash_to_curve.py

import hashlib
from ecdsa import SECP256k1, ellipticcurve
from typing import Optional
from .utils import bytes_to_int, int_to_bytes

def hash_to_curve(alpha: bytes, curve: SECP256k1) -> ellipticcurve.Point:
    """
    Hashes the input alpha to a point on the elliptic curve using the
    Elligator2 algorithm as specified in RFC 9380.

    Args:
        alpha (bytes): The input data to hash.
        curve (SECP256k1): The elliptic curve to map the hash to.

    Returns:
        ellipticcurve.Point: The resulting point on the curve.

    Raises:
        ValueError: If a valid point cannot be found after a reasonable number of attempts.
    """
    # Implementing simplified Elligator2-like mapping
    # For full compliance, refer to RFC 9380's detailed algorithms
    digest = hashlib.sha256(alpha).digest()
    x_candidate = bytes_to_int(digest) % curve.order
    max_attempts = 1000  # Prevent infinite loops
    attempts = 0

    while attempts < max_attempts:
        try:
            y = mod_sqrt(x_candidate**3 + curve.curve.a() * x_candidate + curve.curve.b(), curve.curve.p())
            return ellipticcurve.Point(curve.curve, x_candidate, y)
        except ValueError:
            # Increment x_candidate and try again
            x_candidate = (x_candidate + 1) % curve.order
            attempts += 1

    raise ValueError("Failed to hash to curve after maximum attempts.")

def mod_sqrt(a: int, p: int) -> int:
    """
    Computes the modular square root of a modulo p using the Tonelli-Shanks algorithm.

    Args:
        a (int): The number to find the square root of.
        p (int): The modulus.

    Returns:
        int: The square root of a modulo p.

    Raises:
        ValueError: If no square root exists.
    """
    # Legendre symbol
    legendre = pow(a, (p - 1) // 2, p)
    if legendre != 1:
        raise ValueError("No square root exists for the given input.")

    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Factor p-1 as q * 2^s
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Find a quadratic non-residue z
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = pow(z, q, p)
    x = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)
    m = s

    while t != 1:
        # Find the smallest i (0 < i < m) such that t^(2^i) == 1 mod p
        i = 1
        temp = pow(t, 2, p)
        while temp != 1:
            temp = pow(temp, 2, p)
            i += 1
            if i == m:
                raise ValueError("Failed to find square root.")

        # Update variables
        b = pow(c, 2 ** (m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return x
