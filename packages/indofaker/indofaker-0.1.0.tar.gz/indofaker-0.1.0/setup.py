from setuptools import setup, find_packages

setup(
    name="indofaker",  # Nama library di PyPI
    version="0.1.0",  # Versi awal
    author="Firza Aditya",
    author_email="elbuho1315@gmail.com",
    description="A Python library to generate fake data with Indonesian characteristics.",
    long_description=(
        "IndoFaker is a Python package that provides tools to generate fake data "
        "such as names, addresses, phone numbers, and other information with a distinct Indonesian flair. "
        "It is useful for testing, prototyping, or populating databases with realistic yet fictitious data."
    ),
    long_description_content_type="text/plain",
    url="https://github.com/firzaelbuho/indofaker",  # Link ke repositori GitHub
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
