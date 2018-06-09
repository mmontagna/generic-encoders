import unittest
import six

from generic_encoders import lz4

class TestLz4Encoder(unittest.TestCase):

    def test_lz4_encoders_bytes(self):
        string = b"some string 123"
        self.assertEqual(string,
            lz4.decode(
                lz4.encode(string)
                ))

    def test_throws_exception_when_encode_passed_bogus_type(self):
        string = 123
        with self.assertRaises(TypeError) as context:
            lz4.encode(string)

    def test_throws_exception_when_decode_passed_bogus_type(self):
        string = 123
        with self.assertRaises(TypeError) as context:
            lz4.decode(string)

    def test_lz4_decode(self):
        string = b"asdaaaaaaaaaaaaaaaaasdasd\n"
        self.assertEqual(string,
            lz4.decode(
                b'\x04"M\x18d@\xa7\x0e\x00\x00\x00Lasda\x01\x00`sdasd\n\x00\x00\x00\x00+6\x98\xaf'
                ))

if __name__ == '__main__':
    unittest.main()