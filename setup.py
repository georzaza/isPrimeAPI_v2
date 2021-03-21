# This file is only useful for when we want to install
# the api modules globally. To do so, read the instuctions 
# of the "install_api_globally.md" file.
# If we wish a global install we need to change some of the 
# api code a little bit.

from setuptools import find_packages, setup

setup(
    name='api_is_prime',
    packages=find_packages(include=['api_is_prime']),
    version='0.1.0',
    description='UDP Multicast API Over Lan',
    author='G.Zazanis & M.Baliota',
    license='Department of Electrical And Computer Engineering, University of Thessaly',
    install_requires=['invoke-1.5.0  cffi-1.14.5  pycparser-2.20'], 
    email='zazanis@uth.gr  &   mbaliota@uth.gr',
    platform='Developed on Linux, should work on all'
)