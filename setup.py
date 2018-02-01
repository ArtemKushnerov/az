from setuptools import setup, find_packages


setup(
    name='adownloader',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'adownloader=main:main'
        ]
    }
)
