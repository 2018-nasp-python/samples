from log_setup import log

log('module __name__ = {} : start'.format(__name__))

import mod1

def mod2func():
    log("executing mod2func")
    mod1.mod1func()

log('module __name__ = {} : end'.format(__name__))