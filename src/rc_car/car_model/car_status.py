"""Car Status"""
from pygame.math import Vector2

class CarStatus:
    """holds the car's status"""

    def __init__(self, position:Vector2):
        self._position = position
        self._velocity = Vector2(0.0, 0.0)
        self._angle = 0.0
        self._acceleration = 0.0
        self._steering = 0.0

    @property
    def position(self):
        """return the position"""
        return self._position

    @position.setter
    def position(self, position):
        """set the position"""
        self._position = position


    @property
    def velocity(self):
        """return the velocity"""
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """set the velocity"""
        self._velocity = velocity

    @property
    def angle(self):
        """return the angle"""
        return self._angle

    @angle.setter
    def angle(self, angle):
        """set the angle"""
        self._angle = angle

    @property
    def acceleration(self):
        """return the acceleration"""
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        """set the acceleration"""
        self._acceleration = acceleration

    @property
    def steering(self):
        """return the steering"""
        return self._steering

    @steering.setter
    def steering(self, steering):
        """set the steering"""
        self._steering = steering
