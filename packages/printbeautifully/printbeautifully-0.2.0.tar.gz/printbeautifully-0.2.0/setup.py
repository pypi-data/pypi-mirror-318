from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name='printbeautifully',
    version='0.2.0',
    packages=['beautifulprint'],
    url='https://github.com/FAReTek1/beautifulprint',
    license='MIT',
    author='faretek1',
    author_email='',
    description='Pretty print but it\'s prettier than pretty print',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
