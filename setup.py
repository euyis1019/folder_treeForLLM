# setup.py

from setuptools import setup, find_packages

setup(
    name='folder_tree',
    version='1.0.0',
    description='A tool to print folder directory trees',
    author='Yifu Guo',
    author_email='u08yg22@abdn.ac.uk',
    url='https://github.com/euyis1019/folder_treeForLLM',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
