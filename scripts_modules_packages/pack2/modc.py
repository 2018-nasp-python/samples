from log_setup import log

log('module __name__ = {} : start'.format(__name__))

def modcfunc():
    log("executing modcfunc")

log('module __name__ = {} : end'.format(__name__))
