"""test for the analytics"""
import json
import unittest
from rc_car.analytics import Analytics, AnalyticsInput


class MockOutput:
    """mock of the storage"""

    def __init__(self):
        """builds a log"""
        self.log = []
        self._called_write = 0

    def write(self, string):
        """mock the write method"""
        self.log.append(string)
        self._called_write += 1

    @property
    def called_write(self):
        """returns the number of calls to method write"""
        return self._called_write


class TestAnalytics(unittest.TestCase):
    """test suite"""

    def test_store_input(self):
        """test the analytics with a mocked storage"""
        output = MockOutput()
        audit = Analytics(output)

        audit.store_input(AnalyticsInput.STEER)
        self.assertEqual(1, len(output.log))
        entry = json.loads(output.log[0])
        self.assertEqual(
            '123e4567-e89b-12d3-a456-426614174000', entry['deviceId'])
        self.assertTrue(entry['startSession'] is not None)
        self.assertTrue(entry['endSession'] is not None)
        self.assertTrue(entry['sessionDuration'] is not None)
        self.assertTrue(entry['sessionDuration']['amount'] is not None)
        self.assertEqual('second', entry['sessionDuration']['unit'])

    def test_flush(self):
        """test the flush method"""
        output = MockOutput()
        output.write("test")
        audit = Analytics(output)
        calls = output.called_write

        audit.flush()

        self.assertEqual(calls + 1, output.called_write)
