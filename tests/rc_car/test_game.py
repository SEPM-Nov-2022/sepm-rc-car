"""Unit tests for logger.py file"""
import unittest
import pygame
from pygame import Vector2
from mock import patch

from rc_car.game import Game
from rc_car import constants


class MockPygameEvent:
    """Mock of a Pygame Event"""
    # pylint: disable=R0903
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class TestGame(unittest.TestCase):
    """Test class for game.py file"""

    def __init__(self, args):
        super().__init__(args)

        self.called_quit = 0

    @patch('rc_car.game.Game._get_event', return_value=[
        MockPygameEvent(pygame.QUIT, None)])
    @patch('rc_car.game.Game._init_pygame', return_value=None)
    @patch('rc_car.game.Game._init_driver_buttons', return_value=[])
    @patch('rc_car.game.Game._get_pressed', return_value=None)
    @patch('rc_car.game.Game._draw', return_value=None)
    @patch('rc_car.remote.Remote.command', return_value=True)
    def test_quit(self, *_):
        # pylint: disable=W0212
        """test the basic flow and quitting"""
        def mock_quit():
            self.called_quit += 1
        game = Game()
        game._quit = mock_quit

        game.run()

        self.assertEqual(1, self.called_quit)

    @patch('rc_car.game.Game.__init__', return_value=None)
    def test_check_walls(self, *_):
        """block the car in the screen"""
        game = Game()

        self.assertTrue(game.check_walls(Vector2(constants.MAP_MIN_X,
                                                 constants.MAP_MIN_Y)))
        self.assertFalse(game.check_walls(Vector2(constants.MAP_MIN_X-1,
                                                  constants.MAP_MIN_Y)))
        self.assertFalse(game.check_walls(Vector2(constants.MAP_MAX_X+1,
                                                  constants.MAP_MAX_Y)))
        self.assertTrue(game.check_walls(Vector2(constants.MAP_MAX_X-1,
                                                 constants.MAP_MAX_Y)))
