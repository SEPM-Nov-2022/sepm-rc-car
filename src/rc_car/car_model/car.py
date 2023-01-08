"""Race car model"""
from math import copysign, degrees, radians, sin
from datetime import datetime
from typing import Callable

from pygame import (K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_h, K_c)
from pygame.math import Vector2

from .audio_effect import AudioEffect
from .battery import Battery
from .constants import (BATTERY_USAGE, BRAKE_DECELERATION, CAR_LENGTH,
                        CAR_COLORS, DECELERATION, MAX_ACCELERATION, MAX_STEERING,
                        MAX_VELOCITY, STEERING_FACTOR)

class Car:
    """it models the rc car"""

    def __init__(self,
                position:Vector2,
                audio_handler: Callable[[AudioEffect], None],
                check_walls_handler: Callable[[Vector2],bool]):
        """initialisation"""
        self.status = {}
        self.status['position'] = position
        self.status['velocity'] = Vector2(0.0, 0.0)
        self.status['angle'] = 0.0
        self.status['acceleration'] = 0.0
        self.status['steering'] = 0.0
        self.status['color'] = 0
        self.status['color_change'] = datetime.now()

        self.audio_handler = audio_handler
        self.check_walls_handler = check_walls_handler
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

    @property
    def position(self):
        """returns the postion"""
        return self.status['position']

    @property
    def angle(self):
        """returns the angle"""
        return self.status['angle']

    @property
    def color(self):
        """returns the color"""
        return CAR_COLORS[self.status['color']]

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
        elif pressed[K_c]:
            self._cicle_color()

    def _update_battery(self):
        """use battery"""
        self.battery.consume(BATTERY_USAGE if self.status['velocity'].x != 0 else 0)
        if self.battery.is_alert():
            self._send_battery_alert()

    def _update(self, game_time):
        """merges all inputs"""
        self.status['velocity'] += (self.status['acceleration'] * game_time, 0)
        self.status['velocity'].x = max(-MAX_VELOCITY,
                              min(self.status['velocity'].x, MAX_VELOCITY))

        if self.status['steering']:
            turning_radius = CAR_LENGTH / sin(radians(self.status['steering']))
            angular_velocity = self.status['velocity'].x / turning_radius
        else:
            angular_velocity = 0

        position_change = self.status['velocity'].rotate(-self.status['angle']) * game_time
        if self.check_walls_handler(self.status['position'] + position_change):
            self.status['position'] += position_change
            self.status['angle'] += degrees(angular_velocity) * game_time
        else:
            self.status['velocity'] *= 0

    def _accelerate(self, game_time):
        """acceleration control"""
        self._update_acceleration(
            BRAKE_DECELERATION \
                if self.status['velocity'].x < 0 \
                    else self.status['acceleration'] + game_time)

    def _reverse(self, game_time):
        """acceleration in reverse"""
        self._update_acceleration(-BRAKE_DECELERATION if self.status['velocity'].x >
                                  0 else self.status['acceleration'] - game_time)

    def _brake(self, game_time):
        """brake control"""
        self._update_acceleration(
            -copysign(BRAKE_DECELERATION, self.status['velocity'].x)
            if abs(self.status['velocity'].x) > game_time * BRAKE_DECELERATION
            else -self.status['velocity'].x / game_time
        )

    def _play_the_horn(self):
        self.audio_handler(AudioEffect.HORN)

    def _send_battery_alert(self):
        self.audio_handler(AudioEffect.BATTERY_LOW)

    def _no_input(self, game_time):
        """the car will proceed by inertia"""
        self._update_acceleration(
            -copysign(DECELERATION, self.status['velocity'].x)
            if abs(self.status['velocity'].x) > game_time * DECELERATION
            else -self.status['velocity'].x / (game_time if game_time != 0 else 1)
        )

    def _update_acceleration(self, change):
        """limit the acceleration"""
        self.status['acceleration'] = max(-MAX_ACCELERATION,
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
        self.status['steering'] = self.status['steering'] + direction * \
            STEERING_FACTOR * game_time if direction != 0 else 0
        self.status['steering'] = max(-MAX_STEERING, min(self.status['steering'], MAX_STEERING))

    def _cicle_color(self):
        now = datetime.now()
        if (now - self.status['color_change']).seconds<1:
            return
        self.status['color_change'] = now
        self.status['color'] = self.status['color'] + 1 \
            if self.status['color'] + 1 < len(CAR_COLORS) else 0
