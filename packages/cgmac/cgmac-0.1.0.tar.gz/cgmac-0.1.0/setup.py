from setuptools import setup, find_packages
from os import path
import re

with open('LICENSE.txt') as f:
    LICENSE = f.read()
with open('README.md', 'r') as fp:
    long_description = fp.read()
    
AUTHOR = 'Hikaru Sugimoto'
AUTHOR_EMAIL = 'sugimoto.hikaru14@gmail.com'
URL = 'https://github.com/HikaruSugimoto/cgmac'
DOWNLOAD_URL = 'https://github.com/HikaruSugimoto/cgmac'

setup(
    name='cgmac',
    version='0.1.0',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description='Calculate CGM-derived measures',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=LICENSE,
    url=URL,
    packages=find_packages(),
    install_requires=[
        'pandas<=2.2.3',
        'numpy<=1.26.4',
        'statsmodels<=0.14.4',
    ]
)
