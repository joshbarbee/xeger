from setuptools import setup, find_packages
import os, codecs

def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

long_description = read('README.md')

setup(
    name="xeger-lark",
    version="0.1.2",
    description="A library for generating matching strings from a valid PCRE regex",
    author="Josh Barbee",
    author_email="joshbarbee1@gmail.com",
    url="https://github.com/joshbarbee/xeger",
    packages=find_packages(),
    install_requires=["regex", "lark", "pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_data={"xeger": ["xeger/grammar.lark"]},
)
