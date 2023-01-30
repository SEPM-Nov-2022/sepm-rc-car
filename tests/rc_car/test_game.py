"""Unit tests for logger.py file"""
from typing import Sequence
import unittest
import pygame
from pygame import Color, Vector2
from mock import patch

from rc_car.game import Game




class MockClockEvent:

    def get_time(self):
        return 1

    def tick(self, _):
        pass

class MockPygameEvent:

    def __init__(self, type, key):
        self.type = type
        self.key = key

class TestGame(unittest.TestCase):
    """Test class for game.py file"""

    def __init__(self, args):
        super().__init__(args)
        
        self.called_quit = 0

    @patch('rc_car.game.Game._get_clock', return_value=MockClockEvent())
    @patch('rc_car.game.Game._get_event', return_value=[MockPygameEvent(pygame.QUIT, None)])
    @patch('rc_car.game.Game._get_key_pressed', return_value='some key')
    @patch('rc_car.remote.Remote.command', return_value=True)
    # @patch('rc_car.car.Car.color', return_value=Color(0, 0, 0))
    # @patch('rc_car.car.Car.angle', return_value=0)
    # @patch('rc_car.car.Car.position', return_value=Vector2(0,0))
    # @patch('rc_car.car.Car.get_battery_level', return_value=100)
    def test_quit(self, *_):
        def mock_quit():
            self.called_quit += 1
        game = Game()
        game._quit = mock_quit

        game.run()

        self.assertEqual(1, self.called_quit)
