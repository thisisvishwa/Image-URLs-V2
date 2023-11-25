from setuptools import setup, find_packages

setup(
    name='odoo_custom_module',
    version='1.1',
    description='Odoo Custom Module for Displaying External Product Images',
    author='Vishwa G',
    packages=find_packages(),
    install_requires=[
        'odoo17',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)