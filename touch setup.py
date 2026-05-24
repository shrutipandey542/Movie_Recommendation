from setuptools import setup
with open("README.md","r",encoding="utf-8") as fh:
    Long_description =fh.read()

AUTHOR_NAME = 'SHRUTI','SIDDHI'
SRC_REPO = 'src'
lIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = 'AUTHOR_NAME',
    author_email = 'pandeyshruti2807@gmail.com''siddhilagad3301@gmail.com',
    description = 'a simple python package for movie recommendation ',
    Long_description = Long_description ,
    Long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    Python_requires = '>=3.7',
    install_requires = lIST_OF_REQUIREMENTS,
)

