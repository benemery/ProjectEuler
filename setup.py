#!/usr/bin/env python
from distutils.core import setup, Command

with open('README.md', 'rb') as fin:
    README = fin.read()

VERSION = "0.0.1"

PACKAGE_NAME = 'pe'

requires = [
]

tests_require = [
    'pytest',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description='Project Euler solutions',
      long_description=README,
      author='Ben Emery',
      url='https://github.com/benemery/%s' % PACKAGE_NAME,
      download_url='https://github.com/benemery/ProjectEuler/tarball/ProjectEuler',
      packages=[PACKAGE_NAME, ],
      install_requires=requires,
      extras_require={
        'tests': tests_require,
    },
)