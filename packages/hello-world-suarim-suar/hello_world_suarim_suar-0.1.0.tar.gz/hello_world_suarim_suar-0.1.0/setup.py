from setuptools import setup, find_packages

setup(
    name="hello-world-suarim-suar",  # Package name
    version="0.1.0",  # Version number
    description="A simple Hello, World! package with classes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/hello-world",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
