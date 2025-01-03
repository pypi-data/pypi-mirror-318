from setuptools import setup, find_packages

setup(
    name='meowdb',
    version='0.1.0',
    description='A Python interface for the MeowDB in-memory database server.',
    author='Ayon',
    author_email='fakecoder@duck.com',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
