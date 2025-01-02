from setuptools import setup, find_packages

setup(
    name='agraph_utils',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'agraph-python',
        'pandas'
    ],
    author='Hans Aasman',
    author_email='hansaasman@gmail.com',
    description='A set of utilities for working with AllegroGraph',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hansaasman/agraph_utils',
    classifiers=[
        'Programming Language :: Python :: 3',
        #'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)