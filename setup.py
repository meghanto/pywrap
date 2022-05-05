from setuptools import find_packages, setup
setup(
    name='pywrap',
    packages=find_packages(),
    version='0.0.1',
    description='My first Python library',
    author='meghanto',
    license='MIT',
    install_requires=['cppimport','pybind11'],
    py_modules = ['pywrap'],
)
