import logging
import unittest

from mock import patch

from rc_car.car import Car
from rc_car.remote import Remote

DUMMY_PRESSED_SEQUENCE = [True, False, True, False]
DUMMY_GAME_TIME = 1

LOG_MSG = 'The car is unreachable or out of battery'
remote_obj = Remote(print(LOG_MSG))
remote_obj.car = Car
remote_obj.notification_callback = print


class TestRemote(unittest.TestCase):
    """Test class for the remote.py file"""

    @patch('rc_car.car.Car.handshake_remote', return_value=False)
    def test_command_false(self, _):
        expected_bool = False
        with self.assertLogs(level='ERROR') as log_msg:
            logging.getLogger().error(LOG_MSG)
            response_bool = remote_obj.command(DUMMY_PRESSED_SEQUENCE, DUMMY_GAME_TIME)
            self.assertEqual(log_msg.output, [f'ERROR:root:{LOG_MSG}'])
            self.assertIsInstance(response_bool, bool)
            self.assertEqual(response_bool, expected_bool)

    @patch('rc_car.car.Car.handshake_remote', return_value=True)
    @patch('rc_car.car.Car.command', return_value=True)
    @patch('rc_car.remote.Remote._store_analytics', return_value=True)
    def test_command_true(self, *_):
        expected_bool = True
        response_bool = remote_obj.command(DUMMY_PRESSED_SEQUENCE, DUMMY_GAME_TIME)
        self.assertIsInstance(response_bool, bool)
        self.assertEqual(response_bool, expected_bool)
