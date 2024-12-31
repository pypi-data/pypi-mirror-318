from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="custom_app_store",  # Your package name
    version="0.1.0",
    author="Amrita",
    author_email="amrandal09@gmail.com",
    description="Database operations made simple",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify Markdown
    url="https://github.com/amrita09-pix/custom_app_store",  # Update with your repo URL
    packages=find_packages(),
    install_requires=["pymongo"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Dependencies
    python_requires=">=3.6",
)