'''
@Author: John
@Date: 2020-03-02 19:31:30
@LastEditors: John
@LastEditTime: 2020-03-02 22:40:27
@Description: 
'''
from setuptools import setup, find_packages

setup(
    name='scrapy-redis-cluster',
    version='0.6',
    packages=find_packages(),
    url='https://github.com/geebytes/scrapy_redis_cluster',
    license='MIT',
    author='thsheep',
    author_email='thsheep@thsheep.com',
    description='scrapy-redis cluster',
    keywords='scrapy_redis_cluster',
    install_requires=[
        'Scrapy>=1.8.0',
        'redis>=3.0.1',
        'six>=1.14.0',
        'redis-py-cluster>=2.0.0',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
