from setuptools import setup, find_packages

setup(
    name="unique-prime-checker",
    version="0.1.0",
    author="vivek korat",
    author_email="koratvivek0@gmail.com",
    description="A simple library to check if a number is prime",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/koratvivek/prime_checker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
