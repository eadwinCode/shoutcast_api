from setuptools import find_packages
from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='shoutcast-api',
      version='1.0.5',
      description='Shoutcast Radio Directory API ',
      author='eadwinCode',
      author_email='ezeudoh.tochukwu@gmail.com',
      url='https://github.com/eadwinCode/shoutcast_api',
      license='MIT',
      packages=find_packages(),
      keywords='shoutcast radio api',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Topic :: Internet :: WWW/HTTP',
      ],
      zip_safe=False,
      install_requires=[
        'requests==2.23.0',
        'xmltodict==0.12.0',
      ],
)