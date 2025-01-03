from setuptools import setup, find_packages


setup(
    name='shenanigans',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
    ],
    author='Noahlski',
    author_email='noahc018@proton.me',
    description='Random utilities for great convienence.',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)