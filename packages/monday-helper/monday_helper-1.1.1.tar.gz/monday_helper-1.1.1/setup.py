from setuptools import setup, find_packages
from os import path

working_dir = path.abspath(path.dirname(__file__))

with open(path.join(working_dir,'readme.md'), encoding='utf-8') as f:
    long_description = f.read()
    
    
setup(
    name='monday_helper',
    version='1.1.1',
    author='white_hat25',
    author_email='devmarcel30@gmail.com',
    description='Monday API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['requests']
)