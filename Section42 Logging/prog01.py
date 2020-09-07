import logging

logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(level=logging.DEBUG)

logging.debug('This is adebug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
logging.critical('This is a critical message.')
