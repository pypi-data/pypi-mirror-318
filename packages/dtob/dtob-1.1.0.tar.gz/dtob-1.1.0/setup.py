from setuptools import setup, find_packages

setup(
    name="dtob",
    version="1.1.0",
    description="Convert dictionaries into objects with attribute-style access.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/husseinnaeemsec/dicttoobject",
    author="Hussein Naeem",
    author_email="husseinnaeemsec@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
