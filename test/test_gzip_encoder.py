import unittest
import six

from generic_encoders import gzip_encoder

class TestGzipEncoder(unittest.TestCase):

    def test_gzip_encoder_bytes(self):
        string = b"some string 123"
        self.assertEqual(string,
            gzip_encoder.decode(
                gzip_encoder.encode(string)
                ))

    def test_string_throws_exception_on_p3(self):
        string = "some string 123"
        if not six.PY2:
            with self.assertRaises(TypeError) as context:
                gzip_encoder.encode(string)
        else:
            gzip_encoder.encode(string)

    def test_throws_exception_when_encode_passed_bogus_type(self):
        string = 123
        with self.assertRaises(TypeError) as context:
            gzip_encoder.encode(string)


    def test_throws_exception_when_decode_passed_bogus_type(self):
        string = 123
        with self.assertRaises(TypeError) as context:
            gzip_encoder.decode(string)


if __name__ == '__main__':
    unittest.main()