"""Unit tests for logger.py file"""
from typing import Sequence
import unittest
import pygame
from pygame import Color, Vector2

from rc_car.game import Game


class MockCar:
    
    @property
    def color(self):
        return Color(0, 0, 0)

    @property
    def angle(self):
        return 0

    @property
    def position(self):
        return Vector2(0,0)

    def get_battery_level(self):
        return 100

class MockRemote:
    def command(self, pressed: Sequence[bool], game_time) -> bool:
        pass

class MockClockEvent:

    def get_time(self):
        return 1

    def tick(self, _):
        pass

class MockPygameEvent:

    def __init__(self, type, key):
        self.type = type
        self.key = key

class MockMenuItem:
    def is_selected(self):
        return True

    @property
    def filename(self):
        return 'user_3.png'

class TestGame(unittest.TestCase):
    """Test class for game.py file"""

    def __init__(self, args):
        super().__init__(args)
        self.mock_car = MockCar()
        self.mock_remote = MockRemote()
        self.next_event = MockPygameEvent(None, None)
        self.next_key_presssed = 'key'
        
        self.called_quit = 0

    def test_quit(self):
        game = self._create_instance()
        quits = self.called_quit
        self.next_event = MockPygameEvent(pygame.QUIT, None)

        game.run()

        self.assertEqual(quits + 1, self.called_quit)

    def _create_instance(self):
        def mock_get_event():
            return [self.next_event]

        def mock_get_clock():
            return MockClockEvent()

        def mock_get_key_pressed():
            return self.next_key_presssed

        def mock_quit():
            self.called_quit += 1

        game = Game()

        game.car = self.mock_car
        game.remote = self.mock_remote
        game._get_event = mock_get_event
        game._get_clock = mock_get_clock
        game._get_key_pressed = mock_get_key_pressed
        game._quit = mock_quit

        return game