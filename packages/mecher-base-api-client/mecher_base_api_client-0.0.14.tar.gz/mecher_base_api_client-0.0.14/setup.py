import os
from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

setup(
    description='Base for API clients',
    long_description='Base for API clients',
    name='mecher_base_api_client',
    url='https://github.com/MaximChernyak98/mecher_base_api_client',

    maintainer='mecher',
    version=os.getenv("PACKAGE_VERSION", "0.0.1"),
    keywords=['testing'],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    dependency_links=[],
    long_description_content_type='text/plain',
    setup_requires=['setuptools-git-versioning'],
)
