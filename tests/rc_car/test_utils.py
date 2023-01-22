"""Unit tests for utils.py file"""

import unittest

import os
from pathlib import PosixPath

from rc_car.utils import get_env


class TestUtils(unittest.TestCase):
    """Test class for utils.py file"""

    def test_get_env(self):
        """Test method to ensure the project root is retrieved correctly"""
        self.assertEqual('prod', get_env('ENV'))
        self.assertEqual('123e4567-e89b-12d3-a456-426614174000', get_env('DEVICE_UUID'))
