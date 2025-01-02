from setuptools import setup, find_packages

setup(
    name="mliseuvce",  # Choose a unique name for your package
    version="0.1.0",
    author="no author",
    author_email="my@gmail.com",
    description="A collection of educational ML and ANN functions",
    long_description="no description",
    long_description_content_type="text/markdown",
    url="https://github.com/Ganesh57803/mluvmodel",  # Link to your GitHub repository
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)