import unittest

from generic_encoders import base64, url_base64

class TestBase64Encoder(unittest.TestCase):

    def test_base64_encoder(self):
        string = b"some string 123"
        self.assertEqual(string,
            base64.decode(
                base64.encode(string)
                ))

    def test_base64_decode(self):
        string = b"Hello"
        self.assertEqual(string,
            base64.decode(
                b'SGVsbG8='
                ))

    def test_url_base64_encode_decode(self):
        string = b"Hello"
        self.assertEqual(string,
            url_base64.decode(url_base64.encode(string)))




if __name__ == '__main__':
    unittest.main()