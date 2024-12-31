from setuptools import setup, find_packages
import os

# Read the README file for long description
long_description = ""
with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sbuuid",
    version="0.2.1",
    packages=find_packages(),
    description="A package to generate globally unique IDs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shouvik Bajpayee",
    author_email="shouvikbajpayee.private@gmail.com",
    url="https://github.com/shouvikbj/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
