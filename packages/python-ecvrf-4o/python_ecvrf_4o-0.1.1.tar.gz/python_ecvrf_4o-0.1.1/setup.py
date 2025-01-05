# File: setup.py

from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Long description from README.md
README = (HERE / "README.md").read_text(encoding="utf-8")

# Version of the package
VERSION = "0.1.1"

# Dependencies
INSTALL_REQUIRES = [
    "cryptography>=3.4.7,<4.0",
    "PyCryptodome>=3.10.1,<4.0",
    "ecdsa>=0.17.0,<1.0"
]

# Setup configuration
setup(
    name="python-ecvrf-4o",  # Ensure this matches the PyPI package name
    version=VERSION,
    description="An Elliptic Curve Verifiable Random Function (ECVRF) library, initially designed for Omne.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="OmneDAO Foundation",
    author_email="leadership@omne.foundation",
    url="https://github.com/OmneDAO/python-ecvrf",
    project_urls={
        "Documentation": "https://github.com/OmneDAO/python-ecvrf#readme",
        "Source": "https://github.com/OmneDAO/python-ecvrf",
        "Tracker": "https://github.com/OmneDAO/python-ecvrf/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",  # Update to "5 - Production/Stable" when ready
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",  # Ensure this matches your LICENSE file
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",  # Specify supported Python versions
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="ecvrf cryptography vrf elliptic-curve verifiable-random-function",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7, <4",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "dev": [
            "pytest>=6.2.4,<7.0",
            "flake8>=3.8.4,<4.0",
            "black>=21.7b0,<22.0",
            "isort>=5.8.0,<6.0",
            "mypy>=0.910,<1.0",
            "sphinx>=4.2.0,<5.0",
            "sphinx_rtd_theme>=0.5.0,<1.0",
        ],
        "docs": [
            "sphinx>=4.2.0,<5.0",
            "sphinx_rtd_theme>=0.5.0,<1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            # "ecvrf-cli=ecvrf.cli:main",  # Uncomment and modify if you add CLI scripts
        ],
    },
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    license="MIT",  # Ensure this matches your LICENSE file
)
