import unittest

from generic_encoders import base64_encoder, url_base64_encoder

class Testbase64_encoderEncoder(unittest.TestCase):

    def test_base64_encoder_encoder(self):
        string = b"some string 123"
        self.assertEqual(string,
            base64_encoder.decode(
                base64_encoder.encode(string)
                ))

    def test_base64_encoder_decode(self):
        string = b"Hello"
        self.assertEqual(string,
            base64_encoder.decode(
                b'SGVsbG8='
                ))

    def test_url_base64_encoder_encode_decode(self):
        string = b"Hello"
        self.assertEqual(string,
            url_base64_encoder.decode(url_base64_encoder.encode(string)))




if __name__ == '__main__':
    unittest.main()