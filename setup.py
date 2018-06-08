from setuptools import setup, find_packages


setup(
    name='az',
    version='1.2.0',
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
        'setuptools==38.5.1',
        'python_dateutil==2.7.2',
        ' PyYAML==3.12'
        ,'requests==2.18.4'
    ]
)