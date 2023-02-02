"""Unit tests for utils.py file"""

import unittest
import yaml

from mock import patch

from rc_car.utils import get_env

ENV_NAME = 'ENV'


class TestUtils(unittest.TestCase):
    """Test class for utils.py file"""

    def test_get_env(self):
        """Test method to ensure the project root is retrieved correctly"""
        self.assertEqual('prod', get_env(ENV_NAME))
        self.assertEqual('123e4567-e89b-12d3-a456-426614174000',
                         get_env('DEVICE_UUID'))

    @patch('rc_car.utils.yaml.safe_load', side_effect=yaml.YAMLError)
    def test_get_env_yaml_error(self, _):
        """Test method to simulate yaml error when reading the env file"""
        with self.assertRaises(yaml.YAMLError):
            get_env(ENV_NAME)
