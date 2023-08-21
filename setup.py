from setuptools import setup, find_packages
from typing import List

e_dot = '-e .'

def get_package_list(file_path:str)->List[str]:

    requirements = []
    with open(file_path) as req_file:
        requirements = req_file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if e_dot in requirements:
            requirements.remove(e_dot)
    
    return requirements

setup(name = 'mlops',
      version = '0.1',
      description = 'end to end mlproject',
      author = 'Kashyap Raiyani',
      author_email= 'kshyp22@gmail.com',
      packages = find_packages(),
      install_requires = get_package_list('requirements.txt'))