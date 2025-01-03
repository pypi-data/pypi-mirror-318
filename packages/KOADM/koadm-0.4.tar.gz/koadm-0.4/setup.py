# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='KOADM',
    version='0.4',
    packages=find_packages(),
    package_data={
        '': ['train_data.csv'],  # 包含当前目录下的 train_data.csv 文件
    },
    include_package_data=True,
    description='Knee osteoarthritis diagnosis model',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='QWB',
    license='MIT',
    install_requires=['pandas','numpy','scikit-learn','xgboost',
    'lightgbm','keras','tensorflow'],
    entry_points={
        'console_scripts': [
            'KOADM=KOADM:main',  # 假设你的主函数名为 main
        ],},
)


