#! /usr/bin/env python3
"""
This module demonstrates the use of imports and the structure of modules and
packages
"""
# used to demonstrate reloading of a module
import importlib

# Setup Logging
from log_setup import log
log('module __name__ = {} : start'.format(__name__))

import mod1
from mod1 import mod1_global
from mod2 import mod2func
from mod3 import mod3func as myfunc
import pack1.moda
from pack1.modb import modbfunc
from pack2 import *


def main():
    log("function start")
    mod1.mod1func()
    mod2func()
    myfunc()
    pack1.moda.modafunc()
    modbfunc()
    modc.modcfunc()
    modd.moddfunc()
    importlib.reload(mod1)
    log("Imported global = {}".format(mod1_global))
    log("function end")


if __name__ == '__main__':
    main()

log('module __name__ = {} : end'.format(__name__))
