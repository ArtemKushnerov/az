from setuptools import setup, find_packages


setup(
    name='az',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'az=cli:run'
        ]
    }
)
