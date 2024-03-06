from setuptools import find_packages, setup


# function to get depedencies list dynamically from given path 
def get_requirements(path):
    '''
        This function will return list of requirements
    Args:
        path : str
    Returns:
        list : requirements list 
    '''
    with open(path) as file:
        requirements = file.read().splitlines()
        requirements = [req.replace("\n","") for req in requirements if req != '-e .']
    return requirements
setup(
    name ='Student Prediction System',
    version='1.0.0',
    packages=find_packages(),
    author="Ilesh",
    author_email="ilesh21190@gmail.com",
    install_requires=get_requirements('requirements.txt')
)