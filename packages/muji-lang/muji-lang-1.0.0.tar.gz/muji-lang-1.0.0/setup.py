from setuptools import setup, find_packages  
  
setup(  
    name='muji-lang',  
    version='1.0.0',  
    packages=find_packages(),  
    entry_points={  
        'console_scripts': [  
            'muji=muji.main:main',  
        ],  
    },  
    author='Your Name',  
    author_email='guluguluman4@gmail.com',  
    description='Muji Programming Language Interpreter',  
    # long_description=open('README.md').read(),  
    # long_description_content_type='text/markdown',  
    url='https://github.com/theSandeshStha/muji-bhasa',  
    classifiers=[  
        'Programming Language :: Python :: 3',  
        'Operating System :: OS Independent',  
    ],  
    python_requires='>=3.6',  
)  