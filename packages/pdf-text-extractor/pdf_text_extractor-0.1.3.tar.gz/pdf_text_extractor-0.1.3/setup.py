import os

from setuptools import setup, find_packages


def parse_requirements(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]


def read_me(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        return f.read()


setup(
    name="pdf-text-extractor",
    version="0.1.3",
    description="Extract text and images from PDF files",
    long_description=read_me('README.md'),
    long_description_content_type="text/markdown",
    author="Shahzod",
    author_email="baxromov.shahzodbek@gmail.com",
    url="https://github.com/baxromov/pdf-text-extractor",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
