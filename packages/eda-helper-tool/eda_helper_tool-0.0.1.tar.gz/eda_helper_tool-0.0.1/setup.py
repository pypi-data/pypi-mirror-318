from setuptools import find_packages, setup
from typing import List

# Development mode package identifier
hyphen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements from the given file.
    
    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of package requirements.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            # Read lines and strip whitespace
            requirements = [req.strip() for req in file_obj if req.strip()]
            
            # Remove the development mode package if it exists
            if hyphen_e_dot in requirements:
                requirements.remove(hyphen_e_dot)

    except FileNotFoundError:
        print(f"Warning: The requirements file {file_path} was not found.")
    except IOError as e:
        print(f"Error reading {file_path}: {e}")

    return requirements


# Function to read the content of the README.md file
def read_readme(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as readme_file:
            return readme_file.read()
    except FileNotFoundError:
        print(f"Warning: The README file {file_path} was not found.")
        return ""
    except IOError as e:
        print(f"Error reading {file_path}: {e}")
        return ""


author_user_name = "iamprashantjain"
repo_name = "eda_helper"
pkg_name = "eda_helper-tool"
author_email = 'iamprashantjain2601@gmail.com'

# Read the content of the README.md
long_description = read_readme('README.md')

# Setup configuration
setup(
    name=pkg_name,
    version="0.0.1",
    author=author_user_name,
    author_email=author_email,
    description='Python functions for EDA: univariate, bivariate, and multivariate analysis.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the format of the long description
    url=f"https://github.com/{author_user_name}/{repo_name}",
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=get_requirements('requirements_dev.txt'),  # Get package requirements
)