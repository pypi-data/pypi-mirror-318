# MIT License
# Copyright (c) 2025 Bhautik Sudani
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages, Extension


# Define the C extension module
my_c_extension = Extension(
    'bxml.xmlmodule',  # This will be the name of the Python module (without .py)
    sources=['bxml/PyInit_xmlmodule.c'],  # C source file(s)
)

setup(
    name="bigger-xml",  # The name of your package
    version="0.0.2",    # The version of your package
    packages=['bxml'],  # Automatically find packages in the current directory
    ext_modules=[my_c_extension],
    install_requires=[  # External dependencies (if any)
    ],
    description="XML Generation Package to Generating Big xmls faster without any memory leakage issue",
    long_description=open("README.md").read(),  # Long descriptiosn read from README.md
    long_description_content_type="text/markdown",  # Format of the long description
    author="Bhautik Sudani",
    author_email="bhautiksudani2765@gmail.com",
    url="https://github.com/bitu2765/bxml",  # Optional: Link to your package repository
    classifiers=[  # Optional: Classifiers to help users find your package
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Markup",  # This indicates that it deals with markup (XML)
        "Topic :: Utilities",  # General utility for working with text
    ],
    python_requires='>=3.6',  # Specify the required Python version
)