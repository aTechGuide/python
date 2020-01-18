import logging

logging.basicConfig(
  level=logging.DEBUG, 
  format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
  filename='logs.txt'
  )

logger = logging.getLogger('books')
logger.info('Info Message')


# Child logger
## Any configuration we've got on the books logger, will be inherited by the database logger,
logger = logging.getLogger('books.database') 