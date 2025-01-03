from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(
    name="scav",
    description="SCAV: Safety Concept Activation Vector Jailbreak Framework",
    long_description=long_description,
    version="1.1",
    author="SCAV Team",
    author_email="rhuangbi@connect.ust.hk",
    url="https://github.com/SproutNan/AI-Safety_SCAV",
    packages=find_packages(),
    license="MIT",
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        "transformers",
        "torch",
        "numpy",
    ],
)
