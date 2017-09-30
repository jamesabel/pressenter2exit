
from setuptools import setup

import pressenter2exit

application_name = 'pressenter2exit'

setup(
    name=application_name,
    description='Facilitates exit of a Python CLI program in a controlled way',
    version=pressenter2exit.__version__,
    author='James Abel',
    author_email='j@abel.co',
    license='MIT License',
    url='https://github.com/jamesabel/pressenter2exit',
    download_url='https://github.com/jamesabel/pressenter2exit/archive/master.zip',
    keywords=['cli', 'exit', 'control'],
    packages=[application_name],
    install_requires=[],
    classifiers=[]
)