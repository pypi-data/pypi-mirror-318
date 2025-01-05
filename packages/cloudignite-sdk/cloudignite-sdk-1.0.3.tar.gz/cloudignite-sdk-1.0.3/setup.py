from setuptools import setup, find_packages

setup(
    name="cloudignite-sdk",
    version="1.0.3",
    description="A Python SDK for interacting with CloudIgnite services",
    long_description=open("README.md").read(),
    author="CloudIgnite",
    author_email="arpitrangi72@gmail.com",
    url="https://cloudignite.in",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
