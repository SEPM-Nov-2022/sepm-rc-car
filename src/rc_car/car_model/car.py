"""Race car model"""
from math import copysign, degrees, radians, sin
from typing import Callable

from pygame import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_h
from pygame.math import Vector2

from .audio_effect import AudioEffect
from .battery import Battery
from .constants import (BATTERY_USAGE, BRAKE_DECELERATION, CAR_LENGTH,
                        DECELERATION, MAX_ACCELERATION, MAX_STEERING,
                        MAX_VELOCITY, STEERING_FACTOR)


class Car:
    """it models the rc car"""

    def __init__(self, position:Vector2, audio_handler: Callable[[AudioEffect], None]):
        """initialisation"""
        self.position = position
        self.velocity = Vector2(0.0, 0.0)
        self.angle = 0.0
        self.acceleration = 0.0
        self.steering = 0.0
        self.audio_handler = audio_handler
        self.battery = Battery()

    def command(self, pressed, game_time):
        """interacts with the remote controller"""
        self._update_speed(pressed, game_time)
        self._update_direction(pressed, game_time)
        self._update_misc(pressed)
        self._update(game_time)
        self._update_battery()

    def get_battery_level(self):
        """return the percentage of the battery"""
        return self.battery.battery_level

    def handshake_remote(self):
        """returns True if successful"""
        return self.battery.battery_level > 0

    def _update_speed(self, pressed, game_time):
        """updates the speed"""
        if pressed[K_UP] and self.battery.battery_level > 0:
            self._accelerate(game_time)
        elif pressed[K_DOWN] and self.battery.battery_level > 0:
            self._reverse(game_time)
        elif pressed[K_SPACE]:
            self._brake(game_time)
        else:
            self._no_input(game_time)

    def _update_direction(self, pressed, game_time):
        """updates the direction"""
        if pressed[K_RIGHT]:
            self._steer_right(game_time)
        elif pressed[K_LEFT]:
            self._steer_left(game_time)
        else:
            self._no_steering(game_time)

    def _update_misc(self, pressed):
        if pressed[K_h]:
            self._play_the_horn()

    def _update_battery(self):
        """use battery"""
        self.battery.consume(BATTERY_USAGE if self.velocity.x != 0 else 0)
        if self.battery.is_alert():
            self._send_battery_alert()

    def _update(self, game_time):
        """merges all inputs"""
        self.velocity += (self.acceleration * game_time, 0)
        self.velocity.x = max(-MAX_VELOCITY,
                              min(self.velocity.x, MAX_VELOCITY))

        if self.steering:
            turning_radius = CAR_LENGTH / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * game_time
        self.angle += degrees(angular_velocity) * game_time

    def _accelerate(self, game_time):
        """acceleration control"""
        self._update_acceleration(
            BRAKE_DECELERATION if self.velocity.x < 0 else self.acceleration + game_time)

    def _reverse(self, game_time):
        """acceleration in reverse"""
        self._update_acceleration(-BRAKE_DECELERATION if self.velocity.x >
                                  0 else self.acceleration - game_time)

    def _brake(self, game_time):
        """brake control"""
        self._update_acceleration(
            -copysign(BRAKE_DECELERATION, self.velocity.x)
            if abs(self.velocity.x) > game_time * BRAKE_DECELERATION
            else -self.velocity.x / game_time
        )

    def _play_the_horn(self):
        self.audio_handler(AudioEffect.HORN)

    def _send_battery_alert(self):
        self.audio_handler(AudioEffect.BATTERY_LOW)

    def _no_input(self, game_time):
        """the car will proceed by inertia"""
        self._update_acceleration(
            -copysign(DECELERATION, self.velocity.x)
            if abs(self.velocity.x) > game_time * DECELERATION
            else -self.velocity.x / (game_time if game_time != 0 else 1)
        )

    def _update_acceleration(self, change):
        """limit the acceleration"""
        self.acceleration = max(-MAX_ACCELERATION,
                                min(change, MAX_ACCELERATION))

    def _steer_right(self, game_time):
        """steer right"""
        self._steer(game_time, -1)

    def _steer_left(self, game_time):
        """steer left"""
        self._steer(game_time, 1)

    def _no_steering(self, game_time):
        """no steering"""
        self._steer(game_time, 0)

    def _steer(self, game_time, direction):
        """updates the steering control"""
        self.steering = self.steering + direction * \
            STEERING_FACTOR * game_time if direction != 0 else 0
        self.steering = max(-MAX_STEERING, min(self.steering, MAX_STEERING))
