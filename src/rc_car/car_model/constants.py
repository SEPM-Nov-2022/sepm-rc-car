"""This file includes the key constants used in modelling a race car."""

from pygame import Color

ALERT_SECS = 5

BATTERY_LEVEL_INIT = 100.0
BATTERY_USAGE = 0.01
BATTERY_LOW_ALERT = 20

BRAKE_DECELERATION = 10
DECELERATION = 2

CAR_LENGTH = 2

MAX_VELOCITY = 20
MAX_STEERING = 30
MAX_ACCELERATION = 10.0

STEERING_FACTOR = 32
ASSET_HORN = 'horn.mp3'
ASSET_BATTERY_LOW = 'battery_low.mp3'

CAR_COLORS = [Color(0xff,0,0), Color(0,0xff,0), Color(0,0,0xff)]
