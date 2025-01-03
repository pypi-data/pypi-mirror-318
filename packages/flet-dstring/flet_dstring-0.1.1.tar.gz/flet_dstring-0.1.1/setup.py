from setuptools import setup, find_packages

setup(
    name='flet_dstring',
    version='0.1.1',
    author='Barkin MADDOX',
    packages=find_packages(),
    description='DString (Dynamic String) is a Python library that provides a simple and intuitive syntax for creating richly styled text in Flet applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'flet>=0.25.2',
    ]
)