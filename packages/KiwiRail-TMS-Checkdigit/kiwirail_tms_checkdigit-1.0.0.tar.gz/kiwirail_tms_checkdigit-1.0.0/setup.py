from setuptools import setup, find_packages, Command
import unittest
import os
import sys

def read_requirements(file : str):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file : str):
    with open(file) as f:
        return f.read()

long_description = read_file("README.md")
version = read_file("VERSION").strip()  # Remove any trailing newlines
requirements = read_requirements("requirements.txt")

class TestCommand(Command):
    """Run all tests"""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        sys.path.insert(0, os.getcwd())
        sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
        suite = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)

setup(
    name='KiwiRail-TMS-Checkdigit',
    version=version,
    author='Chris Dirks',
    author_email='cdirksfer@email.com',
    url='https://github.com/cdfer/KiwiRail_TMS_Checkdigit_Python',
    description='A package for calculating the check digit of a TMS number',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(exclude=["tests"]),  # Don't include test directory in binary distribution
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    cmdclass={
        'test': TestCommand,
    },
)
