"""Remote control"""
from typing import Callable, Sequence
from pygame import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_h
from logger import generate_logger

from car import Car
from analytics import Analytics,AnalyticsInput,AnalyticsStorage

log = generate_logger(name='Remote')

class Remote:
    """Remote controller for a Car"""

    def __init__(self, notification_callback: Callable[[str], None]):
        """creates the instance"""
        self.notification_callback = notification_callback
        self.car = None
        self._filter_key = []
        self.analytics = Analytics(AnalyticsStorage())

    def connect_to(self, car: Car):
        """connects to a car"""
        self.car = car

    def command(self, pressed: Sequence[bool], game_time):
        """interacts with the remote controller"""
        if self.car.handshake_remote():
            if pressed not in self._filter_key:
                self.car.command(pressed, game_time)
                self._store_analytics(pressed)
            return True
        msg = 'The car is unreachable or out of battery'
        self.notification_callback(msg)
        log.error(msg)
        return False

    def _store_analytics(self, pressed):
        if pressed[K_LEFT] or pressed[K_RIGHT]:
            self.analytics.store_input(AnalyticsInput.STEER)
        if pressed[K_UP]:
            self.analytics.store_input(AnalyticsInput.ACCELERATE)
        if pressed[K_SPACE]:
            self.analytics.store_input(AnalyticsInput.BRAKE)
        if pressed[K_DOWN]:
            self.analytics.store_input(AnalyticsInput.REVERSE)
        if pressed[K_h]:
            self.analytics.store_input(AnalyticsInput.HONK)
