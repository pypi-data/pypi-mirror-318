from setuptools import setup, find_packages 
from pathlib import Path 

# Read the contents of the README file 
this_directory = Path(__file__).parent 
long_description = (this_directory / "README.txt").read_text()

setup(
    name='qdesc',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g., pandas if your function requires it
    ],
    author='Paolo Hilado',
    author_email='datasciencepgh@proton.me',
    long_description='README.txt', 
    long_description_content_type='text/markdown', # or 'text/x-rst' for reStructuredText # other metadata fields... )
)
