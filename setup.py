from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'traffic-light-simulator',
    packages = find_packages(), 
    include_package_data = True,
    package_data = {'traffic_light_simulator': ['*']},
    version = '0.1.1',
    description = 'A Traffic Light Simulator',
    author = 'Caleb Hayashida',
    author_email = 'santeyio@gmail.com',
    url = 'https://github.com/santeyio/traffic-light-simulator', 
    download_url = 'https://github.com/santeyio/traffic-light-simulator/archive/0.1.tar.gz', 
    keywords = ['testing', 'example'], 
    classifiers = [],
    entry_points = {
        'console_scripts': ['traffic-light-simulator=traffic_light_simulator.user_interface:main'],
    },
)
