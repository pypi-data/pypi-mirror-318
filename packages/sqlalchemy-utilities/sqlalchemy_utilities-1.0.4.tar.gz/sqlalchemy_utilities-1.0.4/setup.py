from setuptools import setup, find_packages


setup(
    name='sqlalchemy-utilities',
    version='1.0.4',
    description='Included sqlalchemy serializers',
    author='Vijay Tiwari',
    author_email='rsvijaytiwari@gmail.com',
    packages=find_packages(include=['sqlalchemy_utilities', 'sqlalchemy_utilities.*']),
    install_requires=['sqlalchemy']
)
