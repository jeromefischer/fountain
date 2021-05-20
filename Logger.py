import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logFile = 'fountain.log'
my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=50*1024*1024,
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

logger = logging.getLogger('Fountain Logger')
logger.setLevel(logging.INFO)
logger.addHandler(my_handler)
