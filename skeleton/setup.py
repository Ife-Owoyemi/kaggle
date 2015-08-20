try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Prediction Guide',
	'author': 'Fernando Ramirez',
	'ul': 'URL to get it at, not one yet',
	'download_url': 'Where to download it, not one of those either',
	'author_email': 'framirez730@gmail.com, will change to a unique project email',
	'version': '0.1',
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name': 'predictionGuide'
}
setup(**config)