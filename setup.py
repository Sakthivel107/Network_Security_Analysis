from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    hypen_e_dot="-e ."
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[require.replace('\n',"") for require in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        return requirements
setup(
    name="Network Security Analysis",
    version='0.0.1',
    author="Sakthivel",
    author_email="sakthivel107g@gmail.com",
    packages=find_packages(),
   install_requirements=get_requirements('requirements.txt')

)