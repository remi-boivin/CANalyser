# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CANanalyser',
    version='0.1.0',
    description='can protocol analyser',
    long_description=readme,
    author='Rémi Boivin',
    author_email='remi.boivin@epitech.eu',
    url='https://github.com/remi-boivin/CANalyser/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)