from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='azoo',
    version='1.3.1',
    author="Artsiom Kushnariou",
    author_email="kushnerovartem@gmail.com",
    description="Downloads apks from androzoo repository https://androzoo.uni.lu/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ArtemKushnerov/az',
    entry_points={
        'console_scripts': [
            'az=modules.main:run'
        ]
    },
    packages=find_packages(),
    package_data={
        '': ['*.yaml'],
    },
    install_requires=[
        'click==6.7',
        'setuptools==41.0.1',
        'python_dateutil==2.7.2',
        'PyYAML==4.2b1',
        'requests==2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
