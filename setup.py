# -*- coding: utf-8 -*-

from os.path import abspath, dirname
from sys import path
from setuptools import setup, find_packages

# To temporarily modify sys.path
SETUP_DIR = abspath(dirname(__file__))

setup(
    name='cobradb',
    version='0.3.0',
    description="""COBRAdb loads genome-scale metabolic models and genome
                   annotations into a relational database.""",
    url='https://github.com/SBRG/cobradb',
    author='Zachary King',
    author_email='zaking@ucsd.edu',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systems biology, genome-scale model',
    packages=find_packages(),
    install_requires=[
        'biopython>=1.74,<2',
        # Be careful upgrading cobra for use with BiGG; ancient models (e.g.
        # iND750.xml) cause errors with cobra versions >=0.15
        'cobra>=0.14.2,<0.15',
        'configparser==4.0.2',
        'escher>=1.7.3,<2',
        'ipykernel==4.5.1',
        'ipywidgets==7.4.0',
        'jinja2==2.11.3',
        'jupyter-client==4.4.0',
        'lxml>=4.4.1,<5',
        'nbconvert==5.0.0',
        'notebook==4.4.1',
        'numpy==1.17.2',
        'pandas==1.0.3',
        'psycopg2>=2.8.3,<3',
        'pytest>=4.6.6,<5',
        'python-libsbml>=5.18.0,<6',
        'scipy==1.3.1',
        'six>=1.12.0,<2',
        'SQLAlchemy>=1.3.10,<2',
        'terminado==0.5',
        'tornado>=4.5.3,<5'
    ],
)
