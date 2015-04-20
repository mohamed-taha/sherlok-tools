try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'Sherolk tools contains group of classifiers used for sentiment analysis',
	'author' : 'graduation Project Team',
	'url' : '',
	'download_url' : '',
	'author_email' : '',
	'version' : '0.1',
	'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'sherolkTools'

}

setup(**config)
