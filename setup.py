import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
PATH_VERSION = os.path.join(HERE, 'pyrsvd', '__version.py')

ABOUT = {}

with open(PATH_VERSION, mode='r', encoding='utf-8') as f:
    exec(f.read(), ABOUT)

requirements = [
    "cupy==8.3.0",
    "numba==0.51.2",
    "numpy==1.19.2",
    "pytest==6.2.2",
]


setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__description__'],
    license="BSD",
    author="Srinath Kailasa",
    author_email='srinathkailasa@gmail.com',
    url='https://github.com/skailasa/pyrsvd',
    zip_safe=False,
    install_requires=requirements,
    keywords='pyrsvd',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]
)
