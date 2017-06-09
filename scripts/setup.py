from distutils.core import setup


setup(
	name='Layout-menu-curses',
	version='0.1.0',
	author='fmount',
	author_email='francesco.pantano@linux.com',
	packages=['menu', 'menu.utils', 'menu.config'],
	url='http://pypi.python.org/pypi/menu/',
	license='MIT',
	description='Useful curses menu utility.',
	long_description=open('../README.md').read(),
	install_requires=[
		"six",
		"curses-menu",
	],
)
