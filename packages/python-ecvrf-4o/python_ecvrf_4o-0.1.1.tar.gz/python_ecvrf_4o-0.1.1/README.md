# ECVRF Library

A custom Elliptic Curve Verifiable Random Function (ECVRF) implementation.

## Features

- Key Generation and Management
- Proof Generation and Verification
- Hash-to-Curve Mapping
- Comprehensive Testing Suite
- Security Audits and Static Analysis

## Installation

```bash
pip install -e .
```

## Usage
```python
from ecvrf import KeyManager, VRF, VRFVerifier
```

# Initialize KeyManager
```python
km = KeyManager()
```

# Generate Key Pair
```python
private_pem, public_pem = km.generate_keypair()
```

# Initialize VRF and Verifier
```python
vrf = VRF(km)
verifier = VRFVerifier(km)
```

# Input Data
```python
alpha = b"Sample input for ECVRF."
```

# Generate Proof and Beta
```python
beta, proof = vrf.prove(private_pem, alpha)
```

# Verify Proof
```python
is_valid = verifier.verify(public_pem, alpha, beta, proof)
print(f"Verification successful: {is_valid}")
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License