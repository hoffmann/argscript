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
    print 'action_bar called with arguments msg: %s, times: %s' %(msg, times)
    

if __name__ == '__main__':
    argscript.run()

