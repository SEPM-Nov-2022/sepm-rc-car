"""analytics utility"""
import json
from enum import Enum
import os
import time

from datetime import datetime

from constants import ANALYTICS_FOLDER, ANALYTICS_BASE_FILENAME
from utils import get_env

class AnalyticsInput(Enum):
    steer = 1
    accelerate = 2
    brake = 3
    reverse = 4
    honk = 5

class AnalyticsStorage:

    def __init__(self):
        if not os.path.exists(ANALYTICS_FOLDER):
            os.mkdir(ANALYTICS_FOLDER)
        self._sync_old_logs()
        filename = ANALYTICS_BASE_FILENAME.format(time.time())
        self.full_filename = os.path.join(ANALYTICS_FOLDER, filename)

    def write(self, string):
        with open(self.full_filename, "w") as f:
            f.write(string)

    def _sync_old_logs(self):
        pass

class CustomEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime):
            return (str(z))
        else:
            return super().default(z)

class Analytics:
    """analytics utility class"""

    def __init__(self, output):
        self.output = output
        self.input={
            'deviceId': get_env('DEVICE_UUID'),
            'startSession': datetime.now(),
            'endSession': datetime.now(),
            'sessionDuration': {
                'amount': 0,
                'unit': 'second'
            },
            'inputs': {
                'steer': 0,
                'accelerate': 0,
                'brake': 0,
                'reverse': 0,
                'honk': 0
            }
        }

    def store_input(self, input:AnalyticsInput):
        if input is None:
            return
        if input.name not in self.input:
            self.input[input.name] = 0
        else:
            self.input[input.name] += 1
        self.input['endSession'] = datetime.now()
        self.input['sessionDuration']['amount'] = \
            (self.input['endSession'] - self.input['startSession']).total_seconds()
        self._flush()

    def _flush(self):
        string = json.dumps(self.input, cls=CustomEncoder)
        self.output.write(string)
