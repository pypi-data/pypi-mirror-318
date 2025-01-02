from setuptools import setup, find_packages

setup(
    name="log_loss_tool",  # Nome único do pacote no PyPI
    version="0.2.0",       # Atualize para refletir a nova versão
    description="A Python library to visualize and calculate Log-Loss, including optimal threshold calculation.",
    long_description=open("README.md").read(),  # Leia a descrição do README
    long_description_content_type="text/markdown",  # O README está em Markdown
    author="Rodrigo Campos",
    author_email="rodrigocamposag90@gmail.com",
    url="https://github.com/RodrigoCamposDS/log_loss_tool",  # URL do repositório
    packages=find_packages(),  # Automaticamente encontra subpacotes
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0"
    ],
    python_requires=">=3.6",  # Versão mínima do Python
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)