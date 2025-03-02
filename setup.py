from setuptools import setup, find_packages

setup(
    name="Biblioteca",
    version="1.0",
    description="Aplicacion que simula una gestion de una biblioteca",
    author="Dawid Gruszka",
    author_email="dawidgruszka@outlook.es",
    packages=find_packages(),
    intall_requires=[
        "SQLAlchemy",
        "pytest",
        "setuptools"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)