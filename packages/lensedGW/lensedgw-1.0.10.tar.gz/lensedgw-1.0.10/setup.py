#!/usr/bin/env python

from setuptools import setup, find_packages 

setup(
    name= "lensedGW", # 包名，发布后可用 pip 安装
    version= "1.0.10", # 版本号
    description="lensed waveform for point mass model",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/addone", # 你的项目地址
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
    "pycbc.waveform.fd": [
        "lumDis = lensedGW.main:lumDis",
        "gravitational_lens=lensedGW.main:gravitational_lens",
        "amp_factor=lensedGW.main:amp_factor",
        "lensed_fd_waveform = lensedGW.main:lensed_fd_waveform"
    ],
    }
)
