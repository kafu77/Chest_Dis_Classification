import setuptools
with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Chest_Dis_Classification"
AUTHOR_USER_NAME = "kafu77"
SRC_REPO ="Classifier"
AUTHOR_EMAIL = "kafubere99@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for CV app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)