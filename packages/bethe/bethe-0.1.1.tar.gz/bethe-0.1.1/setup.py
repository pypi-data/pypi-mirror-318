from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bethe',
    version='0.1.1',
    url='https://github.com/CyberGuy99/bethe',
    author='CyberGuy99',
    author_email='rushilcd@umd.edu',
    description='Bethe Equation Solver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy'
    ],
)
