"""Unit tests for car.py file"""

import unittest

from pygame import Color
from pygame.math import Vector2

from rc_car.car import Car
from rc_car.remote import Remote

DUMMY_PRESSED_SEQUENCE = [True, False, True, False]
DUMMY_GAME_TIME = 1

LOG_MSG_REMOTE = 'The car is unreachable or out of battery'
remote_obj = Remote(print(LOG_MSG_REMOTE))

LOG_MSG_SOUND = 'Playing pop music'
CAR_POSITION = Vector2(23, 19)
remote_obj.car = Car(CAR_POSITION, LOG_MSG_SOUND, True)
remote_obj.notification_callback = print


class TestCar(unittest.TestCase):
    """Test class for the car.py file"""

    def test__steer(self):
        remote_obj.car._steer(DUMMY_GAME_TIME, 1)
        response_steering = remote_obj.car.status['steering']
        self.assertIsInstance(response_steering, int)
        self.assertEqual(response_steering, 64)

    def test__no_steering(self):
        remote_obj.car._no_steering(DUMMY_GAME_TIME)
        response_steering = remote_obj.car.status['steering']
        self.assertIsInstance(response_steering, int)
        self.assertEqual(response_steering, 0)

    def test__steer_left(self):
        remote_obj.car._steer_left(DUMMY_GAME_TIME)
        response_steering = remote_obj.car.status['steering']
        self.assertIsInstance(response_steering, int)
        self.assertEqual(response_steering, 100)

    def test__steer_right(self):
        remote_obj.car._steer_right(DUMMY_GAME_TIME)
        response_steering = remote_obj.car.status['steering']
        self.assertIsInstance(response_steering, int)
        self.assertEqual(response_steering, -100)

    def test__accelerate(self):
        remote_obj.car._accelerate(DUMMY_GAME_TIME)
        response_acceleration = remote_obj.car.status['acceleration']
        self.assertIsInstance(response_acceleration, float)
        self.assertEqual(response_acceleration, 1.)

    def test__update_acceleration(self):
        dummy_change = 0.25
        remote_obj.car._update_acceleration(dummy_change)
        response_acceleration = remote_obj.car.status['acceleration']
        self.assertIsInstance(response_acceleration, float)
        self.assertEqual(response_acceleration, dummy_change)

    def test_get_battery_level(self):
        """Test method to get the car's battery level."""
        expected_battery_level = 100.
        response_battery_level = remote_obj.car.get_battery_level()
        self.assertIsInstance(response_battery_level, float)
        self.assertEqual(response_battery_level, expected_battery_level)

    def test_handshake_remote(self):
        """Test method for the car's handshake remote."""
        expected_handshake = True
        response_handshake = remote_obj.car.handshake_remote()
        self.assertIsInstance(response_handshake, bool)
        self.assertEqual(response_handshake, expected_handshake)

    def test_position(self):
        """Test method for the car's position."""
        expected_car_position = CAR_POSITION
        response_car_position = remote_obj.car.position
        self.assertIsInstance(response_car_position, Vector2)
        self.assertEqual(response_car_position, expected_car_position)

    def test_angle(self):
        """Test method for the car's angle."""
        expected_car_angle = 0.
        response_car_angle = remote_obj.car.angle
        self.assertIsInstance(response_car_angle, float)
        self.assertEqual(response_car_angle, expected_car_angle)

    def test_color(self):
        """Test method for the car's color."""
        expected_car_color = Color(0xff, 0, 0)
        response_car_color = remote_obj.car.color
        self.assertIsInstance(response_car_color, Color)
        self.assertEqual(response_car_color, expected_car_color)
