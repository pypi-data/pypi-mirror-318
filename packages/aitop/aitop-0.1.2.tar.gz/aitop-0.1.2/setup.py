#!/usr/bin/env python3
"""Setup script for AITop."""
from setuptools import setup, find_packages
from pathlib import Path

# Get version from version.py
exec(open('aitop/version.py').read())

# Read README.md for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="aitop",
    version=__version__,
    description="A system monitor focused on AI/ML workload monitoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alexander Warth",
    author_email="alexander.warth@mailbox.org",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "psutil>=5.9.0,<6.0.0",  # System and process utilities
        "typing_extensions>=4.5.0,<5.0.0",  # For Python <3.8 compatibility
        "rich>=13.0.0,<14.0.0",  # Terminal UI and formatting
        "py3nvml>=0.2.7,<0.3.0",  # NVIDIA GPU monitoring
        "click>=8.1.0,<9.0.0",  # Command line interface
        "tabulate>=0.9.0,<1.0.0",  # Table formatting
        "blessed>=1.20.0,<2.0.0",  # Terminal capabilities
    ],
    extras_require={
        "dev": [
            "black>=23.0.0,<24.0.0",
            "mypy>=1.0.0,<2.0.0",
            "pytest>=7.0.0,<8.0.0",
            "pytest-cov>=4.1.0,<5.0.0",
            "pylint>=2.17.0,<3.0.0",
            "isort>=5.12.0,<6.0.0",
            "flake8>=6.1.0,<7.0.0",
            "pre-commit>=3.3.0,<4.0.0",
        ],
        "docs": [
            "sphinx>=7.0.0,<8.0.0",
            "sphinx-rtd-theme>=1.3.0,<2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "aitop=aitop.__main__:main",
        ],
    },
    package_data={
        "aitop": ["config/*.json"],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Monitoring",
    ],
)
