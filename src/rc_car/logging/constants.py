"""
The purpose of this file is to maintain constants used for logging.
"""
DATE_TIME_FMT = '%Y-%m-%d %H:%M:%S'

EMPTY_STRING = ''

# The format of each log message includes the timestamp, the
# logger's name or purpose, the filename,
# the line number at which the log occurs, the log level
# (e.g., debug/info/warning/error/critical), and
# the log message.
FORMAT_OF_LOG_MSG = \
    '[%(asctime)s %(name)s] (%(filename)s %(lineno)d): ' \
    '%(levelname)s %(message)s'
