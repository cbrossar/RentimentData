import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create file handlers
debug_fh = logging.FileHandler('logs/debug.log')
debug_fh.setLevel(logging.DEBUG)
info_fh = logging.FileHandler('logs/info.log')
info_fh.setLevel(logging.INFO)
error_fh = logging.FileHandler('logs/error.log')
error_fh.setLevel(logging.ERROR)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
debug_fh.setFormatter(formatter)
info_fh.setFormatter(formatter)
error_fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(debug_fh)
logger.addHandler(info_fh)
logger.addHandler(error_fh)
