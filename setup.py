from setuptools import setup, find_packages

setup(
    name = 'Defiance',
    version = '1',
    include_package_data = True,
    packages = find_packages(),
    description = 'Code for defiance web application',
    install_requires = ['distribute'],
    url = 'http://www.defiance.in',
)

