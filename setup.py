from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mehrp',
    version='0.0.1',
    description='Easy beeping (merhp) from the terminal.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/c0yote/mehrp',
    author='U.G. Wilson',
    author_email='ugwilson@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators ',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Monitoring',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='beep notification',
    py_modules=['mehrp'],
    install_requires=['simpleaudio'],
    entry_points={
        'console_scripts': [
            'mehrp=mehrp.__main__:main',
        ],
    },
    packages=['mehrp',],
    package_dir={'mehrp':'mehrp'},
    package_data={
        'mehrp':['mehrp.wav']
    },
)