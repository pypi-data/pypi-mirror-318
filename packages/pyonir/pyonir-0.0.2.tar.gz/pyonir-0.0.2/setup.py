from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='pyonir',
    description='a python library for building web applications',
    long_description=description,
    long_description_type='text/markdown',
    url='https://pyonir.dev',
    author='Derry Spann',
    author_email='pyonir@derryspann.com',
    version='0.0.2',
    packages=find_packages(),
    package_data={
        'pyonir': ['libs/*']
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pyonir-create = pyonir:cli.PyonirSetup"
        ]
    }
)
