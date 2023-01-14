"""This file includes the key constants used in the race car game."""

from src.rc_car.utils import get_project_root

ASSET_DIR = 'assets'
ASSET_CAR = 'car.png'
ASSET_DRIVER = 'driver.png'
ASSET_BATTERY = 'battery.png'
ASSET_BACKGROUND = 'background.png'

CAR_GAME_CAPTION = 'RC Car'
CAR_GAME_DIR = '/src/rc_car'

ENV_FILE_NAME = 'environment.yml'

ROOT_DIRECTORY = get_project_root()
LOG_PATH_AND_FILE = f"{ROOT_DIRECTORY}/rc-car.log"

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
