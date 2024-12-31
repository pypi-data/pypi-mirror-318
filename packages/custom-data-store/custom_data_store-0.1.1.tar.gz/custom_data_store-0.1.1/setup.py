from setuptools import setup, find_packages

setup(
    name="custom_data_store",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["pymongo"],
    author="Amrita",
    author_email="amrandal09@gmail.com",
    description="A simple database called appstore for storing any information that you want and will perform basic CRUD operations on them",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amrita09-pix/MongoDB_connect",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7.0",
)
