from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Education",
    "Development Status :: 5 - Production/Stable"
]


setup(
    name="awaish_pkg",
    version="1.42",
    description="A simple package offering a collection of useful functions for enhanced productivity.",
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/x-rst",
    url='https://github.com/abuawaish/awaish_pkg',
    author="abuawaish",
    author_email="abuawaish7@gmail.com",
    license='MIT',
    keywords='funny',
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=[]
)
