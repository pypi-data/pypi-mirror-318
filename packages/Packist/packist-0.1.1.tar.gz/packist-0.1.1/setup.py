from setuptools import setup, find_packages

setup(
    name="Packist",
    version="0.1.1",
    description="A Python package example",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Aayush",
    author_email="aayushpratapsingh14@gmail.com",
   # url="https://github.com/yourusername/your_package",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
