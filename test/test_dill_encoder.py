import unittest
import six

from generic_encoders import dill_encoder

class TestDillEncoder(unittest.TestCase):

    def test_dill_encoder_mixed_type(self):
        string = {'a': 123, 'b': [1,2,{'c': 3}]}
        self.assertEqual(
          string,
          dill_encoder.decode(
            dill_encoder.encode(string)))

    def test_dill_handles_modules(self):
        self.assertEqual(
          123,
          dill_encoder.decode(dill_encoder.encode(dill_encoder)).decode(dill_encoder.encode(123))
          )

    def test_dill_handles_modules(self):
        self.assertEqual(
          123,
          dill_encoder.decode(dill_encoder.encode(dill_encoder)).decode(dill_encoder.encode(123))
          )


if __name__ == '__main__':
    unittest.main()