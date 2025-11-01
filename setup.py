from setuptools import setup, find_packages
from typing import List
import os

def get_requirements() -> List[str]:
    requirement_list = []
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    try:
        with open(requirements_path, 'r') as file:
            requirements = file.readlines()
            for req in requirements:
                requirement = req.strip()
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")                

    return requirement_list
print(get_requirements())

setup(
    name='MLOPS_Project',
    version='0.0.1',
    author='arnab',
    packages=find_packages(),
    install_requires=get_requirements(),
    author_email="darnab680@gmail.com"
)     