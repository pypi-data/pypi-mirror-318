
from setuptools import setup, find_packages

setup(
    name='random_lib',
    version='0.3.3',
    packages=find_packages(),
    package_dir={"random_lib_debug": "random_lib_debug"},
    description='A library to generate random integers',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        # ... other classifiers ...
    ],
)