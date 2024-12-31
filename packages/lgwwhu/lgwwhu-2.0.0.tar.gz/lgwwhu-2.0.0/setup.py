#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:09:14 2024

@author: xiaoxiami
"""

from setuptools import setup, find_packages

setup(
    name="lgwwhu",  # 包名，发布后可用 pip 安装
    version="2.0.0",  # 版本号
    description="Lensing gravitational waves",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="zrj",
    author_email="",
    url="",  # 你的项目地址
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points = {"pycbc.waveform.fd":"gravitational_lens_with_amplification = lgwwhu.main:gravitational_lens_with_amplification",
                    "pycbc.waveform.fd":"enerate_waveform=lgwwhu.main:generate_waveform",
                    "pycbc.waveform.fd":"compute_lensed_waveform=lgwwhu.main:compute_lensed_waveform"
                    },
)