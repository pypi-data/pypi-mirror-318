import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Read the content of the requirements.txt file
with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

VERSION = '0.0.49'
DESCRIPTION = 'a python package for ths data '
LONG_DESCRIPTION = ' a python package for ths data  '

# Setting up
setup(
    name="thsdata",
    version=VERSION,
    author="",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(where='.', exclude=(), include=('*',)),
    keywords=['python', 'thsdata'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_data={
        'thsdata': ['*.so', '*.h', '*'],
    },
    python_requires=">=3.10",
    install_requires=requirements,
)
