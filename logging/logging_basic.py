"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger('test_logger')

logger.debug('Debug Message')
logger.info('Info Message')
logger.warning('Warning Message')
logger.error('Error Message')