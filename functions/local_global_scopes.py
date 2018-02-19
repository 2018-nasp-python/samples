# use logging to avoid reinventing wheel
import logging

# Setup Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='{lineno:>3} {funcName:<20} : {message}',
    style='{')  # Use new style string formater


# Alias log to logging.debug for brevity
log = logging.debug

# global scope
log('Assigning outside_global')
outside_global = "assigned in global scope"


def modify_global():
    # outline use of the global keyword
    global outside_global
    global inside_global

    log('outside_global = {}'.format(outside_global))
    log('Assigning outside_global')
    outside_global = "assigned in modify_global"
    log('outside_global = {}'.format(outside_global))

    log('Assigning inside_global')
    inside_global = "assigned in modify_global"
    log("inside_global  = {}".format(inside_global))


def modify_local():
    # the global variables can't be accessed before being assigned as python
    # assumes you want to define it locally because its name exists inside the
    # function

    log('Assigning outside_global')
    outside_global = "assigned in modify_local"
    log('outside_global = {}'.format(outside_global))

    inside_global = "assigned in modify_local"
    log('Assigning inside_global')
    log('inside_global  = {}'.format(inside_global))


def use_global():
    # global variables be accessed immediately since they are never redefined
    log('Assigning outside_global')
    log('outside_global = {}'.format(outside_global))
    log('Assigning inside_global')
    log('inside_global  = {}'.format(inside_global))


log('outside_global = {}'.format(outside_global))
modify_global()
log('outside_global = {}'.format(outside_global))
log('inside_global  = {}'.format(inside_global))
modify_local()
log('outside_global = {}'.format(outside_global))
log('inside_global  = {}'.format(inside_global))
use_global()
