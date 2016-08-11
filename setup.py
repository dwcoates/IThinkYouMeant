# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='IThinkYouMeant',
    version='0.0.1',
    description='A twitter bot to help others express themselves',
    long_description=readme,
    author='Dodge W. Coates',
    author_email='dodge.w.coates@gmail.com',
    # package_data={},
    url='NONE',
    license='LICENSE',
    # packages=find_packages(exclude=('docs'))
)
