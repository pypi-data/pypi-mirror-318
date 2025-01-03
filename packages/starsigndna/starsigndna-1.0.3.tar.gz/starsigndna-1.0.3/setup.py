#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['typer',
                'numpy',
                'pandas',
                'scipy',
                'scikit-learn',
                'bionumpy',
                'matplotlib',
                'seaborn']

test_requirements = ['pytest>=3', "hypothesis"]

setup(
    author="Christian Bope",
    author_email='chrisbop@uio.no',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Mutation signature analysis package",
    entry_points={
        'console_scripts': [
            'starsigndna=starsigndna.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description="starsigndna",
    include_package_data=True,
    keywords='starsigndna',
    name='starsigndna',
    packages=find_packages(include=['starsigndna', 'starsigndna.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/uio-bmi/starsigndna',
    version='1.0.3',
    zip_safe=False,
)
