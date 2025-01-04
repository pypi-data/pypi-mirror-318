from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smarttitletool",  # The package name on PyPI
    version="1.0.0",  # Initial version
    author="Khalid Sulaiman Al-Mulaify",
    author_email="khalidmfy@gmail.com",
    description="A simple tool for flexible smart title case formatting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically find the smarttitletool directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    keywords="title case formatter smart title tool string manipulation",
)
