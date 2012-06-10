argscript
=========

Port of [werkzeug.script][ws] to [argparse][].

Since werkzeug.script is beeing deprecated, I've ported it to argpares.

Basic Usage is the same as werkzeug.script:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """Docstring for script"""

    import argscript

    # actions go here
    def action_foo(arg='test'):
        """doc for action foo
        
        arg -- first argument
        """
        pass

    def action_lee(bar=4):
        """doc for action bar

        bar -- run with bar
        """
        pass

    if __name__ == '__main__':
        argscript.run()


[ws]: http://werkzeug.pocoo.org/docs/script/
[argparse]: http://docs.python.org/library/argparse.html
