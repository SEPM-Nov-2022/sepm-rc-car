"""analytics utility"""
import json
import os
import time
from datetime import datetime
from enum import Enum

import requests

from .constants import (ANALYTICS_BASE_FILENAME, ANALYTICS_FOLDER,
                        ANALYTICS_SERVER_URL, ANALYTICS_SYNC_TIME_DELTA)
from .utils import get_env


class AnalyticsInput(Enum):
    """Enum listing the input types"""
    STEER = 1
    ACCELERATE = 2
    BRAKE = 3
    REVERSE = 4
    HONK = 5


class AnalyticsStorage:
    """utility class abstracting the storage"""

    def __init__(self):
        """builds the instance"""
        if not os.path.exists(ANALYTICS_FOLDER):
            os.mkdir(ANALYTICS_FOLDER)
        filename = ANALYTICS_BASE_FILENAME.format(time.time())
        self.full_filename = os.path.join(ANALYTICS_FOLDER, filename)
        self.last_sync = 0

    def write(self, string):
        """writes the string to the log file"""
        with open(self.full_filename, "w", encoding='UTF-8') as file_handle:
            file_handle.write(string)
        if time.time() - self.last_sync > ANALYTICS_SYNC_TIME_DELTA:
            self.sync_logs()
            self.last_sync = time.time()

    def sync_logs(self):
        """transfers logs to the remote server"""
        file_names = [os.path.join(ANALYTICS_FOLDER, f) for f in os.listdir(ANALYTICS_FOLDER)
                      if os.path.isfile(os.path.join(ANALYTICS_FOLDER, f))]
        for file_name in file_names:
            with open(file_name, 'r', encoding='UTF-8') as file_handler:
                data = file_handler.readline()
                device_id = json.loads(data)['deviceId']
                url = f'{ANALYTICS_SERVER_URL}{device_id}/'
                response = requests.post(url, json=data, timeout=30)
                if response.ok:
                    os.unlink(file_name)
                else:
                    print(f'error transfering file {file_name}')


class CustomEncoder(json.JSONEncoder):
    """custom encoder to handle datetime"""

    def default(self, o):
        """handles custom types"""
        if isinstance(o, datetime):
            return str(o)
        return super().default(o)


class Analytics:
    """analytics utility class"""

    def __init__(self, output):
        self.output = output
        self.log = {
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

    def store_input(self, analytics_input: AnalyticsInput):
        """storese the current log in the data structure"""
        if analytics_input is None:
            return
        input_name = analytics_input.name.lower()
        if input_name not in self.log['inputs']:
            self.log['inputs'][input_name] = 0
        else:
            self.log['inputs'][input_name] += 1
        self.log['endSession'] = datetime.now()
        self.log['sessionDuration']['amount'] = \
            (self.log['endSession'] - self.log['startSession']).total_seconds()
        self.flush()

    def flush(self):
        """flushes the logs on disk"""
        string = json.dumps(self.log, cls=CustomEncoder)
        self.output.write(string)
