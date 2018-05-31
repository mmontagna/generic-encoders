import unittest
import six
from datetime import datetime

from generic_encoders import json
from generic_encoders.encoders.json_encoder import JsonEncoder

class TestJsonEncoder(unittest.TestCase):

    def test_json_encoder_mixed_type(self):
        string = {'a': 123, 'b': [1,2,{'c': 3}]}
        self.assertEqual(
          string,
          json.decode(
            json.encode(string)))

    def test_json_encoder_handles_datetimes(self):
        now = datetime.utcnow()
        self.assertEqual(
          now.isoformat(),
          json.decode(json.encode(now)))

    def test_json_encoder_handles_dates(self):
        now = datetime.utcnow().date()
        self.assertEqual(
          now.isoformat(),
          json.decode(json.encode(now)))

    def test_json_encoder_handles_dates(self):
        now = datetime.utcnow().date()
        self.assertEqual(
          now.isoformat(),
          json.decode(json.encode(now)))

    def test_json_encoder_throws_exception_when_passed_bogus(self):
        encoder = JsonEncoder(skip_errors=False)
        with self.assertRaises(TypeError) as context:
            encoder.encode(six)

    def test_json_encoder_can_skip_errors(self):
        encoder = JsonEncoder(skip_errors=True)
        encoder.encode(six)


if __name__ == '__main__':
    unittest.main()