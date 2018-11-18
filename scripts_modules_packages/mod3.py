from log_setup import log

log('module __name__ = {} : start'.format(__name__))

def mod3func():
    log("executing mod3func")

log('module __name__ = {} : end'.format(__name__))