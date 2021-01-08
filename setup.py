# https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matrixmath_pawaer",
    version="0.0.1",
    author="pawaer",
    author_email="pawaer@t-online.de",
    description="First Package. Providing Matrix Calculations, such as multiplication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/pawaer/matrixmath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
