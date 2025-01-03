from setuptools import setup, find_packages

setup(
    name='pygame-play',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pygame'
        ],
    include_package_data=True,
    package_data={
        '': ['main.py'],
    },
    description='A simple pygame player',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='petteer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
