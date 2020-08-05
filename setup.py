#!/usr/bin/env python

import setuptools

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    "numpy", "matplotlib"
]

setup_requirements = [ ]

test_requirements = [
    "pytest"
]

setuptools.setup(
    author="Mark Kness",
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
    ],
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='',
    name='colorpy',
    packages=setuptools.find_packages(
        include=[
            'colorpy',
        ]
    ),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='',
    version='0.1.1',
)
