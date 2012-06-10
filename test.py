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

def action_lee(bar=True):
    """doc for action bar

    bar -- run with bar
    """
    pass

if __name__ == '__main__':
    argscript.run()

