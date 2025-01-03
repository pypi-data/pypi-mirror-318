from setuptools import setup, find_packages  
  
setup(  
    name='muji-bhasa',  
    version='1.1.3',  
    packages=find_packages(),  
    entry_points={  
        'console_scripts': [  
            'muji=muji.mukhya:main',  
        ],  
    },  
    author='Gulugulu Man',  
    author_email='guluguluman4@gmail.com',  
    description='Muji Programming Language Interpreter',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/theSandeshStha/muji-bhasa',  
    classifiers=[  
        'Programming Language :: Python :: 3',  
        'Operating System :: OS Independent',  
    ],  
    python_requires='>=3.6',  
)  