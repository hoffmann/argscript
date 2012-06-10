[argscript][] is a port of [werkzeug.script][ws] to [argparse][]. Argscript generates
a an argparse command line parser from the function definitions of a script.

> An action is a function in the same module starting with `action_` which takes
a number of arguments where every argument has a default. The type of the
default value specifies the type of the argument. Arguments can then be passed by using `--name=value` from the shell. [werkzeug.script][ws]



Basic Usage is the same as werkzeug.script:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """Docstring for test script"""

    import argscript

    # actions go here
    def action_foo(arg1='test'):
        """doc for action foo
        
        arg1 -- first argument
        """
        print 'action_foo called with argument arg1: %s' % arg1 

    def action_bar(msg='', times=1):
        """doc for action bar

        msg -- a message
        times -- number 
        """
        print 'action_lee called with arguments msg: %s, times: %s' %(msg, times)
        

    if __name__ == '__main__':
        argscript.run()

Now you can run the script with the `-h` parameter to show a basic help. The 
docstring from the `test.py` script is reused in the help message.

    $ ./test.py -h
    usage: test.py [-h] {foo,bar} ...

    Docstring for test script

    positional arguments:
      {foo,bar}

    optional arguments:
      -h, --help  show this help message and exit

To get the help message for a particular action call the script with the action
name and the `-h` parameter:

    $ ./test.py bar -h
    usage: test.py bar [-h] [--msg MSG] [--times TIMES]

    doc for action bar

    optional arguments:
      -h, --help     show this help message and exit
      --msg MSG      a message
      --times TIMES  number

Again the function docstring is reuesed in the help message. If you specify
a description for the arguments in the doc string (`variable -- doc`), they are
reuesed too.

Now you can run the script with the action name and the parameters, and the
action function will be called with them. If you obmit a parameter, the default
value will be used to call the function.

    $ ./test.py bar --msg='Hello World' --times=4
    
    action_lee called with arguments msg: Hello World, times: 4


## Installation

You can either install the development version from [github][argscript]:

    git clone git@github.com:hoffmann/argscript.git
    cd argscript
    sudo python setup.py install


or install it from [pypi.python.org][pypi]:

    pip install argscript




[ws]: http://werkzeug.pocoo.org/docs/script/
[argparse]: http://docs.python.org/library/argparse.html
[argscript]: https://github.com/hoffmann/argscript
[pypi]: http://pypi.python.org/pypi/argscript/
