from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SchoginiAI",
    version="0.1.4",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample AI toolkit by Schogini Systems",
    long_description=long_description,
    #long_description_content_type="text/x-rst",
    long_description_content_type="text/markdown",
    url="https://github.com/schogini/SchoginiAI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
)

