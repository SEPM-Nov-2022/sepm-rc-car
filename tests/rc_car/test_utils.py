import unittest

import os
from pathlib import PosixPath

from rc_car.utils import get_project_root


class TestUtils(unittest.TestCase):

    def test_get_project_root(self):
        root_path = get_project_root()

        self.assertIsInstance(root_path, PosixPath)
        self.assertEqual(root_path, PosixPath(os.getcwd().split('tests/rc_car')[0]))
