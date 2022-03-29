import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Tensor-SC',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/deepomicslab/Tensor-SC',
    license='MIT',
	author='WANG Ruohan',
    author_email='ruohawang2-c@my.cityu.edu.hk',
    description='Tensor-SC is an implementation of a probabilistic tensor decomposition framework for single-cell multi-omics data integration.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['numpy', 'torch==1.9.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)
