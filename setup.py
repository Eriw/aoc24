from setuptools import setup, find_packages

setup(
    name="aoc24",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # For downloading input files
        "numpy",     # For matrix operations
        "networkx",  # For graph problems
        "parse",     # For parsing input strings
    ],
    extras_require={
        "dev": [
            "pytest",  # For running tests
        ],
    },
    entry_points={
        "console_scripts": [
            "aoc=aoc24.cli:main",
        ],
    },
    python_requires=">=3.8",
    author="Your Name",
    description="Advent of Code 2024 Solutions",
)
