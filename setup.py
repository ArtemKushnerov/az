from setuptools import setup, find_packages


setup(
    name='az',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'az=cli:run'
        ]
    },
    install_requires=[
        'click==6.7', 'setuptools==38.5.1', 'python_dateutil==2.7.2', ' PyYAML==3.12'
    ]
)
