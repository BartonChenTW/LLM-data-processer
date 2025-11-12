"""Setup configuration for LLM Data Processer package."""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="llm-data-processer",
    version="0.0.1",
    author="Barton Chen",
    author_email="",
    description="A Python library for seamlessly working with Large Language Models from multiple providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BartonChenTW/LLM-data-processer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "torch": ["torch>=2.0.0"],
        "tensorflow": ["tensorflow>=2.0.0"],
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    include_package_data=True,
    keywords="llm ai machine-learning huggingface gemini openai data-analysis",
    project_urls={
        "Bug Reports": "https://github.com/BartonChenTW/LLM-data-processer/issues",
        "Source": "https://github.com/BartonChenTW/LLM-data-processer",
    },
)
