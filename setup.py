import setuptools
import os

required_dependencies = []
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'

if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        required_dependencies = f.read().splitlines()

setuptools.setup(
    name='data_container',
    version='0.1.0',
    author='Alexander Gübler',
    description='A data container to ensure correct dataframes',
    install_requires=required_dependencies
)