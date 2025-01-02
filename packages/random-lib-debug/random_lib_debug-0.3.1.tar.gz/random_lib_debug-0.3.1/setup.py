
from setuptools import setup, find_packages

setup(
    name='random_lib_debug',
    version='0.3.1',
    packages=find_packages(),
    py_modules=['lib'],
    description='A library to generate random integers',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        # ... other classifiers ...
    ],
)