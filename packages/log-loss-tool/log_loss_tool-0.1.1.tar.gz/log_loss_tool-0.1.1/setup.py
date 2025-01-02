from setuptools import setup, find_packages

setup(
    name= "log_loss_tool",
    version= "0.1.1", 
    description="A Python library to visualize the Log-Loss function.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rodrigo Campos",
    author_email="rodrigocamposag90@gmail.com",
    url="https://github.com/RodrigoCamposDS/log_loss_tool",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)