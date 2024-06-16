import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = fh.read()

__version__ = "0.0.0"
REPO_NAME="chicken-disease"
AUTHOR_USER_NAME='nobrainghost'
SRC_REPO="chiken-disease"
AUTHOR_EMAIL="mulwabenard24@gmail.com"

setuptools.setup(
    name=f"{REPO_NAME}",
    version=__version__,
    author_email=f"{AUTHOR_EMAIL}",
    description="py package for a CNN application to detect chicken diseases",
    long_description=long_description,
    long_description_content='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),


)
