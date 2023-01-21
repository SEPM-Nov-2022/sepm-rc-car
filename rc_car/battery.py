"""RC car's Battery"""
from datetime import datetime

from .logger import generate_logger

from .constants import ALERT_SECS, BATTERY_LEVEL_INIT, BATTERY_LOW_ALERT

log = generate_logger(name='Battery level')


class Battery:
    """it models the car's battery"""

    def __init__(self):
        """this builds the instance"""
        self._battery_level = BATTERY_LEVEL_INIT
        self._last_alert = datetime.now()

    @property
    def battery_level(self):
        """returns the battery level"""
        return self._battery_level

    def consume(self, usage: float):
        """consumes the battery"""
        self._battery_level = max(self._battery_level - usage, 0)

    def is_alert(self):
        """true, if the battery is low and enough time
        since the last alert has passed"""
        now = datetime.now()
        delta = now - self._last_alert

        time_elapsed = delta.seconds
        current_battery_level = self._battery_level
        if time_elapsed > ALERT_SECS and current_battery_level < BATTERY_LOW_ALERT:
            self._last_alert = now
            log.warning(
                'More than %s have passed (%s) and the battery level is %s below %s %%',
                ALERT_SECS, time_elapsed, current_battery_level, BATTERY_LOW_ALERT
            )
            return True
        return False
