from setuptools import setup, find_packages


setup(
    name='sqlalchemy-utilities',
    version='1.0.1',
    description='Included sqlalchemy serializers',
    author='Vijay Tiwari',
    author_email='rsvijaytiwari@gmail.com',
    packages=find_packages(include=['utilities', 'utilities.*']),
    install_requires=['sqlalchemy']
)
