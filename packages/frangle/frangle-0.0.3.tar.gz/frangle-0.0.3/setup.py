"""Setup file for the frangle project."""

import os
import re

import setuptools


def read_resource(filename):
    """Read in content from a file.

    Args:
        filename (str): The relative path of file to read.

    Returns:
        str: The content of the specified file as a string.

    """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
    with open(path, 'r', encoding='utf8') as f:
        return f.read()


def find_version(text):
    """Find the current version of a package in a string.

    This function uses a regular expression to extract the version
    number from the provided `__init__.py` text. It assumes the text
    contains a line in the format: `__version__ = "x.y.z"`.

    Args:
        text (str): The text of the `__init__.py` file to parse.

    Returns:
        str: The version number as a string.

    """
    match = re.search(r"^__version__\s*=\s*['\"](.*)['\"]\s*$", text,
                      re.MULTILINE)
    return match.group(1)


AUTHOR = "Conservation Technology Lab at the San Diego Zoo Wildlife Alliance"
DESC = "frangle: tools for image and video data preparation."

setuptools.setup(
    name="frangle",
    version=find_version(read_resource('frangle/__init__.py')),
    author=AUTHOR,
    description=DESC,
    long_description=read_resource('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/conservationtechlab/frangle",
    license="MIT",
    packages=['frangle'],
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'ffmpeg',
        'pygame',
        'pyyaml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering',
    ],
)
