from setuptools import setup, find_packages

setup(
    name="ampx",
    version="0.0.1",
    author="J Zhang",
    author_email="jzhang@chemoinfolab.com",
    description="A Python package for prediction and design of antimicrobial peptides",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JinZhangLab/ampx",  # 可选
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)