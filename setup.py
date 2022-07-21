from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.0'
DESCRIPTION = 'A library for storing big data'
LONG_DESCRIPTION = 'easyX: a simple Python library for storing complex, big data structure based on HDF5'

# Setting up
setup(
    name="easyx",
    version=VERSION,
    author="Tony (Muhammad) Yousefnezhad",
    author_email="<myousefnezhad@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/myousefnezhad/easyx',
    packages=find_packages(),
    install_requires=['numpy', 'h5py'],
    keywords=['python', 'big data', 'HDF5', 'data storage', 'nonhomogeneous data structure'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)