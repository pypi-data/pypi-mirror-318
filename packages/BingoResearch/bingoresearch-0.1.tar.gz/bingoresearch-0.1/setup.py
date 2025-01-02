from setuptools import setup, find_packages

setup(
    name='BingoResearch',
    version='0.1', 
    packages=find_packages(),
    install_requires=[  
        'numpy',
    ],
    author='gaomany',
    author_email='18580766357@163.com',
    description='A toolbox for research',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/EndlessBingo/BingoResearch',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
