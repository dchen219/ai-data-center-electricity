"""Setup script for dc_energy_prediction package."""

from pathlib import Path

from setuptools import find_packages, setup

# Read the requirements file
requirements_path = Path(__file__).parent / "requirements.txt"
with open(requirements_path) as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

# Read the README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="dc_energy_prediction",
    version="0.1.0",
    author="Data Center Energy Research Team",
    description="AI-powered data center energy consumption prediction using LLM + RAG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/dc-energy-prediction",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dc-energy=dc_energy_prediction.cli.main:main",
            "dc-pipeline=main:main",
        ],
    },
    include_package_data=True,
)
