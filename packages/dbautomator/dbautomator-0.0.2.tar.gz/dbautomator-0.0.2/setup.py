# Setup to create a distributable Python package

from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [
            req.strip()
            for req in requirements
            if req.strip() and not req.strip().startswith("#")
        ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.2"
REPO_NAME = "mongodb"
PKG_NAME = "dbautomator"
AUTHOR_USER_NAME = "joshualumzy"
AUTHOR_EMAIL = "166535332+joshualumzy@users.noreply.github.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    data_files=[("", ["requirements.txt"])],
    install_requires=get_requirements("./requirements.txt"),
)
