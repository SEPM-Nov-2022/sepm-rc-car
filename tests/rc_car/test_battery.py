import unittest

from rc_car.battery import Battery

battery_1 = Battery()
# battery_2 instantiated too as the 'consume' method was tested with both positive (max = computed value = 100 - usage)
# and negative case (max = 0)
battery_2 = Battery()


class TestBattery(unittest.TestCase):

    def test_consume_below_100(self):
        usage = 40.
        battery_1.consume(usage)
        self.assertEqual(battery_1.battery_level, 60.)

    def test_consume_above_100(self):
        usage = 140.
        battery_2.consume(usage)
        self.assertEqual(battery_2.battery_level, 0.)

    def test_is_alert(self):
        battery_1._battery_level = 30
        response_alert = battery_1.is_alert()
        self.assertIsInstance(response_alert, bool)
        self.assertEqual(response_alert, False)
