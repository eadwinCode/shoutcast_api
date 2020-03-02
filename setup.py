#!/usr/bin/env python
import setuptools
from distutils.core import setup



with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='shoutcast-api',
      version='1.0.0',
      description='Shoutcast Radio Directory API ',
      author='eadwinCode',
      author_email='ezeudoh.tochukwu@gmail.com',
      url='https://github.com/eadwinCode/shoutcast_api',
      license='MIT',
      packages=setuptools.find_packages(),
      keywords='shoutcast radio api',
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=['requests', 'xmltodict'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
)