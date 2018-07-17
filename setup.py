from setuptools import setup
import phulpy

long_description = open('README.rst', 'r').read()

setup(
    name='phulpy',
    version=phulpy.__version__,
    packages=['phulpy'],
    setup_requires=['wheel'],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "phulpy = phulpy.__main__:__main__"
        ],
    },
    description="The task manager for python",
    long_description=long_description,
    url='https://github.com/jefersondaniel/phulpy',
    author='Jeferson Daniel',
    author_email='jeferson.daniel412@gmail.com',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
