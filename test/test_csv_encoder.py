import unittest
import six

from generic_encoders import csv_encoder

class TestCsvEncoder(unittest.TestCase):

    def test_csv_encoder_basic_dicts(self):
        dicts = [{"a": "1"}, {"a": "2"}, {"a": "3"}]
        self.assertEqual(
          dicts,
          csv_encoder.decode(
            csv_encoder.encode(dicts)))

    def test_csv_encoder_numbers_are_decoded_as_strings(self):
        dicts = [{"a":  1}, {"a": 2.2}]
        self.assertEqual(
          [{"a":  "1"}, {"a": "2.2"}],
          csv_encoder.decode(
            csv_encoder.encode(dicts)))




if __name__ == '__main__':
    unittest.main()