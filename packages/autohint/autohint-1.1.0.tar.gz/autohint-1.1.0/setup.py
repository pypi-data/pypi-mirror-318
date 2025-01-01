from setuptools import setup, find_packages

setup(
    name="autohint",  # Module name
    version="1.1.0",
    description="AutoHint provides real-time search suggestions with internet integration.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jai Akash",
    author_email="akdevelopments007@gmail.com",  # Replace with your email
    url="https://github.com/Jkdevlopments/autohint",  # Your GitHub link
    packages=find_packages(),
    install_requires=[
        "prompt-toolkit",
        "requests",
        "bs4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)