# setup.py

from setuptools import setup, find_packages

setup(
    name='mathutils_wuyouran',  # 包的名称
    version='0.1.0',   # 包的版本号
    packages=find_packages(),  # 自动发现所有包
    description='A simple math utility package with arithmetic and geometry functions',
    long_description_content_type='text/markdown',
    author='wuyouran',
    author_email='2719875726@qq.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
