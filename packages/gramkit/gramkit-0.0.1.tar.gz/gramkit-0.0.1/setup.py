from setuptools import setup, find_packages

setup(
    name="gramkit",
    version="0.0.1",
    author="Michael",
    description="A modern, Python-native declarative visualization library (placeholder)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)