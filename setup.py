# https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="??", # pip install ?? 
    version="0.0.0",
    author="??",
    author_email="??",
    description="??",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="GitHub.com??",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='??', # e.g. >=3.6
)
