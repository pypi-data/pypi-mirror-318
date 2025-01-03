from setuptools import setup, find_packages

setup(
    name='21blackjack-gui',
    version='1.0.0', 
    description='A python-based blackjack game with a GUI built in tkinter.',
    author='Faizan Ahmed',
    url='https://github.com/outlawF16/blackjack',  
    packages=find_packages(),  
    include_package_data=True,  

    entry_points={
        'console_scripts': [
            'blackjack=blackjack.main:init', 
        ],
    },

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
