from setuptools import setup, find_packages


__author__ = 'Gu Zhengxiong'
__version__ = '0.2.2'

PROGRAM_NAME = 'TMgr'
PACKAGE_NAME = 'tmgr'


with open('requirements.txt') as stream:
    requirements = stream.read().splitlines()


setup(
    name=PROGRAM_NAME,
    version=__version__,
    packages=[PACKAGE_NAME],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'tmgr={name}.main:start_main'.format(name=PACKAGE_NAME)
        ]
    },

    author=__author__,
    author_email='rectigu@gmail.com',
    description='A template manager for the command line.',
    license='GPL-3',
    keywords='Template, Command line',
    url='https://github.com/NoviceLive/' + PACKAGE_NAME,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
