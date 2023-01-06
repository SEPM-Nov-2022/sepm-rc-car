"""Define sounds"""
from enum import Enum

ASSET_HORN = 'horn.mp3'
ASSET_BATTERY_LOW = 'battery_low.mp3'

class AudioEffectDef:
    """List of sounds"""
    def __init__(self, channel:int, path:str):
        self._channel = channel
        self._path = path

    @property
    def channel(self):
        return self._channel

    @property
    def path(self):
        return self._path

class AudioEffect(Enum):
    HORN = AudioEffectDef(0, ASSET_HORN)
    BATTERY_LOW = AudioEffectDef(1, ASSET_BATTERY_LOW)
