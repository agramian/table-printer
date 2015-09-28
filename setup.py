#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='table_printer',
      version='0.1.4',
      description='Python Table Printer',
      long_description=read_md('README.md'),
      author='Abtin Gramian',
      author_email='abtin.gramian@gmail.com',
      url='https://github.com/agramian/table-printer',
      packages=['table_printer'],
      download_url = 'https://github.com/agramian/table-printer/tarball/v0.1.4',
      keywords = ['table', 'display', 'print', 'tabular', 'data'],
      classifiers = []
     )
