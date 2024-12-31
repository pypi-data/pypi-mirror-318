from setuptools import setup, find_packages

setup(
    name='internal_token_service',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyJWT>=2.9.0'
    ],
)