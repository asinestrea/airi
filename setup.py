from setuptools import setup

def read( path ):
	with open(path, 'r') as f:
		return f.read()

setup(
	name = 'gvpp',
	version = '1.1.1',
	description = 'A tool to create animated graph visualizations, based on graphviz, based on legacy source code of gvanim - Massimo Santini',
	long_description = read('README.md'),
	long_description_content_type='text/markdown',
	author = 'Sinestrea',
	author_email = 'git.sinestrea@gmail.com',
	url = 'https://github.com/asinestrea/gvpp',
	license = 'GNU/GPLv3',
	packages = ['gvpp'],
	keywords = 'drawing graph animation',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: Unix',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
