from setuptools import setup, find_packages

version="0.0.0"

setup(
    name='disciklean-sample',
    version=version,
    packages=find_packages(),
    author="Dinesh",
    description="Sample package",
    install_requires=[
        'requests'
    ]    
)