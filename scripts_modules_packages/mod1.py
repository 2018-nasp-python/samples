#! /usr/bin/env python3
"""Simple module to demonstrate module include processing

Attributes:
    mod1_global: example of module level variable 

"""
from log_setup import log

# Log module load start
log('module __name__ = {} : start'.format(__name__))

mod1_global = "mod1 global variable"


def mod1func():
    """ Basic demonstration module level function - logs invocations
        
    """
    log("executing mod1func")


if __name__ == '__main__':
    # If executed as script simply invoke mod1func
    mod1func()


# Log module load end
log('module __name__ = {} : end'.format(__name__))
