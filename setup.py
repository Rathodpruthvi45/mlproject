from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements.'''
    requirements = []
    HYPEN_E_DOT = '-e .'
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines
        requirements = [req.strip() for req in requirements]  # Strip whitespace
        
        # Remove '-e .' if it exists
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Pruthvi',
    author_email='pruthvirathod4545@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
