"""
argscript 
=========

Argscript is a port of werkzeug.script to argparse. Argscript generates
a an argparse command line parser from the function definitions of a script.

An action is a function in the same module starting with `action_` which 
takes a number of arguments where every argument has a default. The type 
of the default value specifies the type of the argument. Arguments can 
then be passed by using `--name=value` from the shell. [werkzeug.script]

Installation
------------

**development version:**::

    git clone git@github.com:hoffmann/argscript.git
    cd argscript
    sudo python setup.py install


**from pypi.python.org:**::

    pip install argscript


"""

from distutils.core import setup
setup(name='argscript',
      version='0.5',
      py_modules=['argscript'],
      author="Peter Hoffmann",
      author_email="ph@peter-hoffmann.com",
      url="https://github.com/hoffmann/argscript",
      license="BSD",
      description="Generate argparse parser from function definitions.",
      long_description=__doc__,
      classifiers=[
        'Development Status :: 4 - Beta', 
        'Environment :: Console',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
      ],
      platforms='any'
      )
