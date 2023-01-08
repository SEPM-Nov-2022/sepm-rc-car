"""Remote control"""
from typing import Callable
from .car import Car

class Remote:
    """Remote controller for a Car"""

    def __init__(self, notification_callback:Callable[[str], None]):
        """creates the instance"""
        self.notification_callback = notification_callback
        self.car = None

    def connect_to(self, car:Car):
        """connects to a car"""
        self.car = car

    def command(self, pressed, game_time):
        """interacts with the remote controller"""
        if self.car.handshake_remote():
            self.car.command(pressed, game_time)
            return True
        self.notification_callback("the car is unreachable or out of battery")
        return False
