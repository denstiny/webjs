# -*- coding: UTF-8 -*-
"""

 @author      : denstiny (2254228017@qq.com)
 @file        : setup
 @created     : Sunday Apr 14, 2024 15:03:54 CST
 @github      : https://github.com/denstiny
 @blog        : https://denstiny.github.io

"""

from setuptools import setup, find_packages

setup(
    name="webjs",
    version="0.1.0",
    install_requires = [
        "PyQt6-WebEngine>=6.6.0"
    ],
    author="denstiny",
    author_email="2254228017@qq.com",
    description="A simple browser",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/denstiny/webjs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
)
