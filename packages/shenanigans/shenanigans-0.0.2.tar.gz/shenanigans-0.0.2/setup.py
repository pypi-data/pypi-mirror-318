from setuptools import setup, find_packages


setup(
    name='shenanigans',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[],
    author='Noahlski',
    author_email='noahc018@proton.me',
    description='Random utilities for great convienence.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)