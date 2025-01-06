from setuptools import setup, find_packages

setup(
    name="tiff-wsi-label-removal",
    version="0.1.1",
    author="Yash Verma",
    author_email="yashv7523@gmail.com",
    description="A tool to remove label pages from TIFF/BigTIFF files without loading the entire file into memory. This utility is especially helpful when dealing with Whole Slide Images (WSIs) where a label page is present and may contain sensitive information.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zenquiorra/tiff-wsi-label-removal",
    license="MIT",
    packages=find_packages(),  
    install_requires=[
        "tifffile>=2023.4.12"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
