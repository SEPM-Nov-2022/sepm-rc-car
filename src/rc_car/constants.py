"""This file includes the key constants used in the race car game."""

ASSET_DIR = 'assets'
ASSET_CAR = 'car.png'
ASSET_DRIVER = 'driver.png'
ASSET_BATTERY = 'battery.png'

CAR_GAME_CAPTION = 'RC Car'
CAR_GAME_DIR = '/src/rc_car'

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
