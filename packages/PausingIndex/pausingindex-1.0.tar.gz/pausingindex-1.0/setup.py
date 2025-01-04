from setuptools import setup
from setuptools import find_packages

version_py = "PausingIndex/_version.py"
exec(open(version_py).read())

setup(
    name="PausingIndex", # Replace with your own username
    version=__version__,
    author="Benxia Hu",
    author_email="hubenxia@gmail.com",
    description="Calculate Promoter Pausing Index",
    long_description="Calculate Promoter Pausing Index from RNApolII ChIP-seq data using longest TSS and TES",
    url="https://pypi.org/project/PausingIndex/",
    entry_points = {
        "console_scripts": ['PausingIndex = PausingIndex.PausingIndex:main',]
        },
    python_requires = '>=3.12',
    packages = ['PausingIndex'],
    install_requires = [
        'numpy',
        'pandas',
        'argparse',
        'pybedtools',
        'pysam',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe = False,
  )
