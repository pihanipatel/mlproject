from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirment(file_path)->List[str]:
    '''This function will return the list of requirement'''
    requirement=[]
    with open(file_path) as f:
        requirement=f.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
        return requirement  
   
setup(
name='mlproject',
version='0.0.1',
author='Pihani Patel',
author_email='pihanipatel6@gmail.com',
packages=find_packages(),
install_requires=get_requirment('requirement.txt')

)