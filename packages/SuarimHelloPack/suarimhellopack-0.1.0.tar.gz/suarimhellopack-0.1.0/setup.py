# setup.py

from setuptools import setup, find_packages

setup(
    name="SuarimHelloPack",  # Package name
    version="0.1.0",         # Initial version
    description="A simple HelloWorld package by Suarim",  # Short description
    long_description=open("README.md").read(),  # Long description (can be a markdown file)
    long_description_content_type="text/markdown",
    author="Suarim",  # Your name
    author_email="your.email@example.com",  # Your email
    url="https://github.com/yourusername/SuarimHelloPack",  # Update with your GitHub URL
    packages=find_packages(),  # Automatically find packages
    classifiers=[  # Classifiers for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
