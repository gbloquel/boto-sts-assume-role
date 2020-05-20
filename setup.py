from codecs import open
from setuptools import setup, find_packages
import os

with open('requirements.txt') as f:
        install_requires = f.read().strip().split('\n')

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'botosts', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name='botosts',
    description=about['__description__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires='>=2.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
