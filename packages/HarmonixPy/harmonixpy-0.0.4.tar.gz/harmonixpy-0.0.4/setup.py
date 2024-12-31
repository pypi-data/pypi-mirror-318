"""Setup tools for HarmonixPy package"""
from setuptools import setup, find_packages  # type: ignore

# Read the README file for the long description
try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "HarmonixPy: A simple module for serving HTML and managing dependencies with Flask."

setup(
    name="HarmonixPy",  # Package name (should be unique)
    version="0.0.4",  # Versioning
    packages=find_packages(),  # Automatically finds subpackages
    install_requires=[
        "flask",  # Add core dependencies
    ],
    entry_points={
        'console_scripts': [
            'harmonixpy = harmonixpy.__main__:main',  # Link CLI command to main function
        ],
    },
    include_package_data=True,  # Include non-Python files (e.g., HTML, CSS)
    description="A simple module for serving HTML and managing dependencies with Flask.",
    long_description=long_description,  # Use README for detailed info
    long_description_content_type="text/markdown",  # README format
    author="Taripretei Zidein",
    author_email="inspirante01@gmail.com",
    url="https://github.com/d-inspiration/HarmonixPy",  # URL to the project repo
    classifiers=[  # Optional: Categorize your project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Compatible Python version
)
