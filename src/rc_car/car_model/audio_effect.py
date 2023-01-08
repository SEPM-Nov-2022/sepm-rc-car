"""Define sounds"""
from enum import Enum

from .constants import ASSET_BATTERY_LOW, ASSET_HORN


class AudioEffectDef:
    """List of sounds"""

    def __init__(self, channel: int, path: str):
        """builds the enum"""
        self._channel = channel
        self._path = path

    @property
    def channel(self):
        """returns the audio channel for the mixer"""
        return self._channel

    @property
    def path(self):
        """returns the path of the audio file"""
        return self._path


class AudioEffect(Enum):
    """enum defining all the effects"""
    HORN = AudioEffectDef(0, ASSET_HORN)
    BATTERY_LOW = AudioEffectDef(1, ASSET_BATTERY_LOW)
