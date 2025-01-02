from setuptools import setup, find_packages

setup(
    name="search_and_replace",
    version="0.2.0",
    description="Command line utility to search and replace text in files",
    author="Alexander Kovrigin",
    author_email="alexander.kovrigin@jetbrains.com",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "search-and-replace=search_and_replace.main:main",
            "diff-apply=search_and_replace.diff_apply:main",
        ],
    },
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "mypy>=1.0.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
