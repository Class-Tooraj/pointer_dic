from setuptools import find_packages
from setuptools import setup

setup(
    name='Pointer_dic',
    version='0.1',
    author='Tooraj Jahangiri',
    author_email='toorajjahangiri@gmail.com',
    url='https://github.com/Class-Tooraj/pointer_dic',
    description='Build a specific point dictionary to translate from the previous point to the new one',
    license='MIT',
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'Pointer_dic_cli = Pointer_dic.main:main',
        ],
    },
)
