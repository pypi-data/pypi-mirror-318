from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name='sqlalchemy-utilities',
    version='1.0.0',
    description='Included sqlalchemy serializers',
    author='Vijay Tiwari',
    author_email='rsvijaytiwari@gmail.com',
    packages=find_packages(include=['utilities', 'utilities.*']),
    install_requires=parse_requirements("requirements.txt")
)
