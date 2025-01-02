from setuptools import setup, find_packages

setup(
    name='func2json',
    version='0.1.1',
    packages=find_packages(),
    install_requires=['pydantic', 'docstring_parser'],
    author='Thanabordee Noun.',
    author_email='thanabordee.noun@gmail.com',
    description='Convert Python functions to JSON schemas using Pydantic,Compatible with LLM Function Calling.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ThanabordeeN/func2json',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)