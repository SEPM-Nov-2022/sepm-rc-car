"""audit utility"""
import json
from enum import Enum
from datetime import datetime

from utils import get_env

class AuditInput(Enum):
    steer = 1
    accelerate = 2
    brake = 3
    reverse = 4
    honk = 5

class CustomEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime):
            return (str(z))
        else:
            return super().default(z)

class Audit:
    """audit utility class"""

    def __init__(self, output):
        self.input={}
        self.output = output
        self.input['deviceId'] = get_env('DEVICE_UUID')
        self.input['startSession'] = datetime.now()
        self.input['endSession'] = datetime.now()
        self.input['sessionDuration'] = {}
        self.input['sessionDuration']['amount'] = 0
        self.input['sessionDuration']['unit'] = 'second'

    def store_input(self, input:AuditInput):
        if input.name not in self.input:
            self.input[input.name] = 0
        else:
            self.input[input.name] += 1
        self.input['endSession'] = datetime.now()
        self.input['sessionDuration']['amount'] = \
            (self.input['endSession'] - self.input['endSession']).total_seconds()
        self._flush()

    def _flush(self):
        self.output.write(json.dumps(self.input, cls=CustomEncoder))
