#!/usr/bin/env python
import codecs
import re

from setuptools import find_packages, setup

with codecs.open('sphinxcontrib/log_cabinet.py', encoding='utf8') as f:
    version = re.search('__version__ = \'(.*?)\'', f.read())

with codecs.open('README.rst', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='sphinxcontrib-log-cabinet',
    version='1.0.0',
    url='http://bitbucket.org/davidism/sphinxcontrib-log-cabinet',
    license='BSD',
    author='David Lord',
    author_email='davidism@gmail.com',
    description='Organize changelog directives in Sphinx docs.',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    namespace_packages=['sphinxcontrib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['sphinx'],
)
