from setuptools import setup, find_packages

setup(
    name='anurags_package',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
    'console_scripts': [
        'anurags_package=game_package.main:play',
    ],
    }, 
    author='Anurag mishra',
    description='A fun command-line game!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/anurag9601/own-package.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
