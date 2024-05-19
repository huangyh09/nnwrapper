"""
BetabinGLM: Beta-binomial regression model
See: https://github.com/StatBiomed/BetabinGLM
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

reqs = [
    'numpy>=1.9.0', 
    'scipy>=1.4.0', 
    'matplotlib', 
    'pandas',
    'scikit-learn',
    'torch',
    'tqdm'
]

here = path.abspath(path.dirname(__file__))

# Set __version__ for the project.
exec(open("./nnwrapper/version.py").read())

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nnwrapper',

    version=__version__,

    description='Some utilities and wrappers for Neural Network Models',
    long_description=long_description,
    url='https://github.com/huangyh09/nnwrapper',

    # Author details
    author=['NNWrapper Team'],
    author_email='yuanhua@hku.hk',

    # Choose your license
    license='Apache-2.0',

    # What does your project relate to?
    keywords=['Neural Network Models', 'Machine Learning'],
    
    packages=find_packages(),
    install_requires=reqs,

    extras_require={
        'docs': [
            #'sphinx == 1.8.3',
            'sphinx_bootstrap_theme']},

    py_modules = ['nnwrapper']

    # buid the distribution: python setup.py sdist
    # upload to pypi: twine upload dist/...
)