"""Remote control"""
from typing import Callable, Sequence
from .car import Car

from src.rc_car.logging.logger import generate_logger

log = generate_logger(name='Remote')


class Remote:
    """Remote controller for a Car"""

    def __init__(self, notification_callback: Callable[[str], None]):
        """creates the instance"""
        self.notification_callback = notification_callback
        self.car = None
        self._filter_key = []

    def connect_to(self, car: Car):
        """connects to a car"""
        self.car = car

    def command(self, pressed: Sequence[bool], game_time):
        """interacts with the remote controller"""
        if self.car.handshake_remote():
            if pressed not in self._filter_key:
                self.car.command(pressed, game_time)
            return True
        msg = 'The car is unreachable or out of battery'
        self.notification_callback(msg)
        log.warning(msg)
        return False
