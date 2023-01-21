import json
import unittest
from rc_car.analytics import Analytics, AnalyticsInput, AnalyticsStorage, ANALYTICS_FOLDER

class MockOutput:
    def __init__(self):
        self.log=[]

    def write(self, string):
        self.log.append(string)

class TestAnalytics(unittest.TestCase):

    def test_store_input(self):
        output = MockOutput()
        audit = Analytics(output)

        audit.store_input(AnalyticsInput.steer)
        self.assertEqual(1, len(output.log))
        entry = json.loads(output.log[0])
        self.assertEqual('123e4567-e89b-12d3-a456-426614174000', entry['deviceId'])
        self.assertTrue(entry['startSession'] is not None)
        self.assertTrue(entry['endSession'] is not None)
        self.assertTrue(entry['sessionDuration'] is not None)
        self.assertTrue(entry['sessionDuration']['amount'] is not None)
        self.assertEqual('second', entry['sessionDuration']['unit'])
