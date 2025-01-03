# setup.py

from setuptools import setup, find_packages

setup(
    name='ann6',  # Package name
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy'],  # List your dependencies (numpy is required for your code)
    description='A simple neural network implementation',
    long_description=open('README.md').read(),  # Long description from README.md
    long_description_content_type='text/markdown',
    author='wanderer22',
    author_email='wanderingwolves22@gmail.com',
    url='https://github.com/yourusername/mllab4',  # GitHub URL for your project (or any hosting service)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
