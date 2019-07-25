try:
	import setuptools
	from setuptools import setup, find_packages
except ImportError:
	print("Please install setuptools.")

import os

long_description = '区間を用いた演算等に使ってください'
if os.path.exists('README.txt'):
	long_description = open('README.txt').read()

setup(
	name='interval',
	version='1.0.0',
	description='区間演算用のパッケージ',
	long_description=long_description,
	license='MIT',
	author='Yuta Ura',
	author_email='yuuta3594@outlook.jp',
	url='https://github.com/YutaUra',
	keywords='interval',
	packages=find_packages(),
	install_requires=[],
	classifiers=[
		'Programming Language :: Python ::3.6',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: MIT License'
	]
)
