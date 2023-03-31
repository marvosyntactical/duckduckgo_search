#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

with open("requirements.txt", encoding="utf-8") as req_fp:
    install_requires = req_fp.readlines()

setup(
    name='ddgs',
    version='0.1',
    description = 'Search for words, documents, images, news, maps and text translation using the DuckDuckGo.com search engine.',
    author='deedy5',
    url='https://cegit.ziti.uni-heidelberg.de/mkoss/tst_pytorch',
    license='Apache License',
    install_requires=install_requires,
    packages=find_packages(exclude=[]),
    python_requires='>=3.10',
    project_urls={
        'Source': 'https://github.com/marvosyntactical/duckduckgo_search',
    },
    entry_points={
        'console_scripts': [
        ],
    }
)
