"""Car"""
from math import sin, radians, degrees, copysign
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE, K_h
from pygame.math import Vector2
from audio_effect import AudioEffect

STEERING_FACTOR = 32
MAX_VELOCITY = 20
BRAKE_DECELERATION = 10
DECELERATION = 2
CAR_LENGTH = 2
MAX_STEERING = 30
MAX_ACCELERATION = 10.0

class Car:
    """it models the rc car"""

    def __init__(self, pos_x, pos_y, audio_handler):
        """initialisation"""
        self.position = Vector2(pos_x, pos_y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = 0.0
        self.acceleration = 0.0
        self.steering = 0.0
        self.audio_handler = audio_handler

    def command(self, pressed, game_time):
        """interacts with the remote controller"""
        self._update_speed(pressed, game_time)
        self._update_direction(pressed, game_time)
        self._update_misc(pressed, game_time)
        self._update(game_time)

    def get_battery_level(self):
        """return the percentage of the battery"""
        return 100.0

    def _update_speed(self, pressed, game_time):
        """updates the speed"""
        if pressed[K_UP]:
            self._accelerate(game_time)
        elif pressed[K_DOWN]:
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

    def _update_misc(self, pressed, game_time):
        if pressed[K_h]:
            self.audio_handler(AudioEffect.HORN)

    def _update(self, game_time):
        """merges all inputs"""
        self.velocity += (self.acceleration * game_time, 0)
        self.velocity.x = max(-MAX_VELOCITY, min(self.velocity.x, MAX_VELOCITY))

        if self.steering:
            turning_radius = CAR_LENGTH / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * game_time
        self.angle += degrees(angular_velocity) * game_time

    def _accelerate(self, game_time):
        """acceleration control"""
        self._update_acceleration(BRAKE_DECELERATION
            if self.velocity.x < 0
            else self.acceleration + game_time)

    def _reverse(self, game_time):
        """acceleration in reverse"""
        self._update_acceleration(-BRAKE_DECELERATION
            if self.velocity.x > 0
            else self.acceleration - game_time)

    def _brake(self, game_time):
        """brake control"""
        self._update_acceleration(-copysign(BRAKE_DECELERATION, self.velocity.x)
            if abs(self.velocity.x) > game_time * BRAKE_DECELERATION
            else -self.velocity.x / game_time)

    def _no_input(self, game_time):
        """the car will proceed by inertia"""
        self._update_acceleration(-copysign(DECELERATION, self.velocity.x)
            if abs(self.velocity.x) > game_time * DECELERATION
            else -self.velocity.x / (game_time if game_time!=0 else 1))

    def _update_acceleration(self, change):
        """limit the acceleration"""
        self.acceleration = max(-MAX_ACCELERATION, min(change, MAX_ACCELERATION))

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
        self.steering = self.steering + direction * STEERING_FACTOR * game_time if direction!=0 else 0
        self.steering = max(-MAX_STEERING, min(self.steering, MAX_STEERING))
