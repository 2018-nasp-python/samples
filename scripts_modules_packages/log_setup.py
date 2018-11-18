"""
Simple logging setup module

Configures logging and creates global alias to debug logger called: log
"""
# Setup Logging
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='{filename:<25} {module:<25} {funcName:<15} : {message}',
    style='{')  # Use new style string formatter

log = logging.getLogger(__name__).debug
