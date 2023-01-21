import unittest

import logging

from rc_car.logger import generate_logger
from rc_car.constants import DATE_TIME_FMT, FORMAT_OF_LOG_MSG

NUM_HANDLERS = 2


class TestLogger(unittest.TestCase):

    def common_logger_checks(self, logger: logging.Logger):
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.handlers[0].formatter._fmt, FORMAT_OF_LOG_MSG)
        self.assertEqual(logger.handlers[0].formatter.datefmt, DATE_TIME_FMT)

    def test_generate_logger_dev(self):
        custom_logger = generate_logger(env='dev')
        self.assertEqual(custom_logger.level, logging.DEBUG)
        self.common_logger_checks(custom_logger)

    def test_generate_logger_test(self):
        custom_logger = generate_logger(env='test')
        self.assertEqual(custom_logger.level, logging.INFO)
        self.common_logger_checks(custom_logger)

    def test_generate_logger_uat(self):
        custom_logger = generate_logger(env='uat')
        self.assertEqual(custom_logger.level, logging.WARNING)
        self.common_logger_checks(custom_logger)

    def test_generate_logger_prod(self):
        custom_logger = generate_logger(env='prod')
        self.assertEqual(custom_logger.level, logging.ERROR)
        self.common_logger_checks(custom_logger)
