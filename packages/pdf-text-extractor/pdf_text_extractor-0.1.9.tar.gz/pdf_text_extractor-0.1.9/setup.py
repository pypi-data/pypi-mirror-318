import os

from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))


def parse_requirements(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]


def read_version():
    data = {}
    path = os.path.join(ROOT, "pdf_text_extractor", "_version.py")
    with open(path, "r", encoding="utf-8") as f:
        exec(f.read(), data)
    return data["__version__"]


def read_long_description():
    path = os.path.join(ROOT, "README.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


setup(
    name="pdf-text-extractor",
    version=read_version(),
    description="Extract text and images from PDF files",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Shahzod",
    author_email="baxromov.shahzodbek@gmail.com",
    url="https://github.com/baxromov/pdf_to_text",
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'pillow',
        'PyMuPDF',
        'pytesseract'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    project_urls={
        "Documentation": "https://pdf-to-text.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/baxromov/pdf_to_text",
        "Issue Tracker": "https://github.com/baxromov/pdf_to_text/issues",
    },
)
