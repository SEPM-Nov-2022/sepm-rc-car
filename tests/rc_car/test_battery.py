"""Unit tests for battery.py file"""

import unittest

from freezegun import freeze_time

from rc_car.battery import Battery

battery_1 = Battery()
# battery_2 instantiated too as the 'consume' method was
# tested with both positive (max = computed value = 100 - usage)
# and negative case (max = 0)
battery_2 = Battery()


class TestBattery(unittest.TestCase):
    """Test class for Battery class in battery.py file"""

    def test_consume_below_100(self):
        """Test method for battery consumption < 100%.
        In this case, the max b/w the computed value (100% - usage)
        and 0% is expected, i.e., the computed value as usage < 100%."""
        usage = 40.
        battery_1.consume(usage)
        self.assertEqual(battery_1.battery_level, 60.)

    def test_consume_above_100(self):
        """Test method for battery consumption > 100%.
        Zero battery is expected."""
        usage = 140.
        battery_2.consume(usage)
        self.assertEqual(battery_2.battery_level, 0.)

    def test_is_alert_false(self):
        """Method to test battery alert if false"""
        battery_1.battery_level = 30
        response_alert = battery_1.is_alert()
        self.assertIsInstance(response_alert, bool)
        self.assertEqual(response_alert, False)

    @freeze_time("2023-01-28")
    def test_is_alert_true(self):
        """Method to test battery alert if true"""
        battery_1.battery_level = 2
        response_alert = battery_1.is_alert()
        self.assertIsInstance(response_alert, bool)
        self.assertEqual(response_alert, True)
