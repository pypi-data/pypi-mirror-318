from setuptools import setup, find_packages

setup(
    name="python_ercas_ng",
    version='1.0.0',
    author='Amaechi Ugwu',
    author_email='amaechijude178@gmail.com',
    description='This package simplifies ercasng payment processing in python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amaechijude/ErcasPay',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires=">=3.8"
)