from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e.'
def get_list_requirements(file_path: str)->List[str]:
    '''
    this funtion will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)

    return requirments


setup(
name='ml_prj_SPI',
version='0.0.1',
author='atulk',
author_email='atuljssate@gmail.com',
package=find_packages(),
install_requires=get_list_requirements('requirements.txt')

)



