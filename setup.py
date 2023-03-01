import os

from setuptools import setup, find_packages

VERSION = '0.2.4'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-keycloak',
    version=VERSION,
    long_description=README,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    # package_data={'': ['templates/*.html', 'templates/*.css']},
    package_data={'': ['templates/*.html']},
    extras_require={
        'dev': [
            'bumpversion==0.5.3',
            'twine',
        ],
        'doc': [
            'Sphinx==1.4.4',
            'sphinx-autobuild==0.6.0',
        ]
    },
    setup_requires=[
        'pytest-runner',
        'python-keycloak-client @ git+https://github.com/Cactiw/python-keycloak-client.git',
    ],
    
    install_requires=[
        'python-keycloak-client @ git+https://github.com/Cactiw/python-keycloak-client.git',
        'Django>=4.1',
    ],
    tests_require=[
        'pytest-django',
        'pytest-cov',
        'mock>=2.0',
        'factory-boy',
        'freezegun'
    ],
    url='https://github.com/dabocs/django-keycloak',
    license='MIT',
    author='Ahmad Dabo',
    author_email='dabo.cs@gmail.com',
    description='Install Django Keycloak.',
    classifiers=[]

)
