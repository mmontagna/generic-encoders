import unittest
import six

from generic_encoders import gzip

class TestGzipEncoder(unittest.TestCase):

    def test_gzip_encoder_bytes(self):
        string = b"some string 123"
        self.assertEqual(string,
            gzip.decode(
                gzip.encode(string)
                ))

    def test_string_throws_exception_on_p3(self):
        string = "some string 123"
        if not six.PY2:
            with self.assertRaises(TypeError) as context:
                gzip.encode(string)
        else:
            gzip.encode(string)

    def test_throws_exception_when_encode_passed_bogus_type(self):
        string = 123
        with self.assertRaises(TypeError) as context:
            gzip.encode(string)


    def test_throws_exception_when_decode_passed_bogus_type(self):
        string = 123
        with self.assertRaises(TypeError) as context:
            gzip.decode(string)


if __name__ == '__main__':
    unittest.main()