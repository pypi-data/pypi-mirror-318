from setuptools import setup, find_packages
import ezsec_requests
setup(
    name='ezsec-requests',
    version='0.1.2',    
    description='A set of pre-formatted request sending functions to interact with ezsec-api',
    url='https://www.ezsec-api.com',
    author='EZSEC LLC',
    author_email='mbultman@ezsec-api.com',
    license='MIT License',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
    ],
)
