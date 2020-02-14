from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name="brailler", 
        version="1.0", 
        packages=find_packages(),
        description="Read and write to and from braille",
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=[
            ],
        python_requires=">=3.6",
)
