"""This file includes the key constants used in the race car game."""
import os
from pathlib import Path

from pygame import Color

# General constants
ASSET_DIR = '../assets'
ASSET_CAR = 'car.png'
ASSET_DRIVER = 'driver.png'
ASSET_BATTERY = 'battery.png'
ASSET_BACKGROUND = 'background.png'
ENCODING = 'UTF-8'

# User profile pictures
USER_1 = 'user_1.png'
USER_2 = 'user_2.png'
USER_3 = 'user_3.png'
USER_4 = 'user_4.png'

# Menu constants
MENU_HEADLINE = 'Choose your profile picture'
MENU_BACKGROUND_COLOUR = (255, 255, 255)
MENU_BG_LEFT = 440
MENU_BG_TOP = 70
MENU_WIDTH = 400
MENU_HEIGHT = 500
MENU_X = 490
MENU_Y = 80
MENU_ITEM_IMAGE_SIZE = 50
MENU_FONT = 'arialblack'
MENU_FONT_SIZE = 20

CAR_GAME_CAPTION = 'RC Car'

ENV_FILE_NAME = 'environment.yml'

# Get app's root directory
ROOT_DIR = str(Path(__file__).parent.parent)

# Get the environment's file's directory
ENV_FILE_DIR = os.path.join(ROOT_DIR, ENV_FILE_NAME)

LOG_PATH_AND_FILE = f"{ROOT_DIR}/rc-car.log"

WIDTH = 1280
HEIGHT = 720

BATTERY_WIDTH = 100
BATTERY_HEIGHT = 20

BATTERY_X = WIDTH - BATTERY_WIDTH - 100
BATTERY_Y = 25

DRIVER_SIZE = 50
DRIVER_X = BATTERY_X + BATTERY_WIDTH + 20
DRIVER_Y = 10

TICKS = 60

PPU = 32

MAP_MIN_X = 1
MAP_MIN_Y = 1
MAP_MAX_X = 38
MAP_MAX_Y = 21

# Constants used for logging
DATE_TIME_FMT = '%H:%M:%S'

EMPTY_STRING = ''

# The format of each log message includes the timestamp, the
# logger's name or purpose, the filename,
# the line number at which the log occurs, the log level
# (e.g., debug/info/warning/error/critical), and
# the log message.
FORMAT_OF_LOG_MSG = \
    '%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s'

# Constants for the race car
ALERT_SECS = 5

BATTERY_LEVEL_INIT = 100.0
BATTERY_USAGE = 0.01
BATTERY_LOW_ALERT = 20

BRAKE_DECELERATION = 10
DECELERATION = 4

CAR_LENGTH = 2

MAX_VELOCITY = 4
MAX_STEERING = 100
MAX_ACCELERATION = 3.0

STEERING_FACTOR = 64
ASSET_HORN = 'horn.mp3'
ASSET_BATTERY_LOW = 'battery_low.mp3'

CAR_COLORS = [Color(0xff, 0, 0), Color(0, 0xff, 0), Color(0, 0, 0xff)]

# Constants for analytics
ANALYTICS_SERVER_URL = 'http://127.0.0.1:5000/toy/'
ANALYTICS_FOLDER = 'analytics'
ANALYTICS_BASE_FILENAME = 'session_{:10.0f}.log'
ANALYTICS_SYNC_TIME_DELTA = 60
