#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author        : yuzijian
# @Email         : yuzijian1010@163.com
# @FileName      : setup.py
# @Time          : 2024-12-30 11:51:53
# @description   : 
"""


# setup.py
from setuptools import setup, find_packages

setup(
    name='PanMCL',
    version='0.6.6',  # 更新版本号
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'PanMCL=my_commandline_tool.cli:main',
        ],
    },
    description='A simple command-line tool',
    author='yuzijian',
    author_email='yuzijian1010@163.com',
    url='https://github.com/yourusername/PanMCL',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

