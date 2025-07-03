from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dayspan",
    version="1.0.2",
    author="Cong Gao",
    author_email="cnggao@gmail.com",
    description="Calculate days between two dates (inclusive)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dayspan",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "dayspan=dayspan.cli:main",
        ],
    },
)
