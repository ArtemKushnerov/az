from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='azoo',
    version='1.3.0',
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
        'click==8.0.0',
        'python_dateutil==2.8.2',
        'PyYAML==6.0',
        'requests==2.27.1',
        'setuptools==58.0.4',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
