from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Read the README file for the long description
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="SchoginiAI",  # Replace with your desired package name
    version="0.1.5",  # Incremented version
    author="Sreeprakash Neelakantan",
    author_email="schogini@gmail.com",
    description="A sample AI toolkit by Schogini Systems with Retrieval-Augmented Generation (RAG).",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/schogini/SchoginiAI",  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        "langchain>=0.3.14",
        "langchain-community>=0.3.14",
        "openai>=1.59.3",
        "tiktoken>=0.8.0",
        "faiss-cpu>=1.9.0.post1",
        "langchain-openai",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,  # Include additional files as specified in MANIFEST.in
    # Optional: Define entry points for command-line scripts
    # entry_points={
    #     "console_scripts": [
    #         "schogini=SchoginiAI.main:main",
    #     ],
    # },
)

