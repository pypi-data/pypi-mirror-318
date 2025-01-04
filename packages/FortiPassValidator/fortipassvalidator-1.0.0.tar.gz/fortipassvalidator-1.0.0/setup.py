from setuptools import setup, find_packages

setup(
    name="FortiPassValidator",
    version="1.0.0",
    description="A Python library for validating passwords with customizable rules.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ahmed Abdelrahman",
    author_email="ahmad18189@gmail.com",
    url="https://github.com/ahmad18189/FortiPassValidator",
    packages=find_packages(),
    install_requires=[
        "profanity-check==1.0.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

