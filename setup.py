from setuptools import find_packages, setup
setup(
    name='pywrap',
    version='0.0.1',
    description='My first Python library',
    author='meghanto',
    license='MIT',
    install_requires=['cppimport','pybind11'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),

)
