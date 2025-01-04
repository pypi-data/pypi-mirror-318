from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="monitoro",
    version="0.2.0",
    author="Omar Kamali",
    author_email="support@monitoro.co",
    description="A Python client for the Monitoro API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monitoro-inc/python-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
        "tqdm>=4.60.0",
    ],
)
