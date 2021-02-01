import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
PATH_VERSION = os.path.join(HERE, 'src', '__version.py')

ABOUT = {}

with open(PATH_VERSION, mode='r', encoding='utf-8') as f:
    exec(f.read(), ABOUT)

requirements = [
    "numba",
    "numpy",
    "cudatoolkit",
    "pytest",
]


setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__description__'],
    license="BSD",
    author="Srinath Kailasa",
    author_email='srinathkailasa@gmail.com',
    url='https://github.com/skailasa/pyrsvd',
    packages=find_packages(
        exclude=['*.test']
    ),
    zip_safe=False,
    install_requires=requirements,
    keywords='pyrsvd',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]