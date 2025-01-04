from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flexibletitle",
    version="1.0.0",
    author="Khalid Sulaiman Al-Mulaify",
    author_email="khalidmfy@gmail.com",
    description="A flexible smart title case formatter for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="title case formatter flexible title string manipulation",
)
