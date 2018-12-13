from setuptools import setup, find_packages
from os import path
from io import open

setup(
    name='mehrp',
    version='0.0.0',
    description='Easy beeping (merhp) from the terminal.',
    url='https://github.com/c0yote/mehrp',
    author='U.G. Wilson',
    classifiers=[
        'Development Status :: 4 - BETA',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators ',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Monitoring',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='beep notification',
    py_modules=['mehrp'],
    install_requires=['pyaudio'],
    data_files=[('mehrp_data', ['data/mehrp.wav'])],
    entry_points={
        'console_scripts': [
            'mehrp=mehrp:main',
        ],
    },
)