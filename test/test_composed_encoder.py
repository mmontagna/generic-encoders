import unittest
import six

from generic_encoders import *
from generic_encoders.encoders.composed_encoder import EncoderLinkError

class TestComposedEncoder(unittest.TestCase):

    def test_ascii_gzip_base64_encode_decode(self):
      encoder = ComposedEncoder(text_ascii_encoder, gzip_encoder, base64_encoder)
      self.assertEqual('abcdefg', encoder.decode(encoder.encode('abcdefg')))

    def test_ascii_gzip_base64_ascii_encode(self):
      encoder = ComposedEncoder(
        text_ascii_encoder,
        gzip_encoder,
        base64_encoder,
        text_ascii_encoder.inverted)
      self.assertEqual('abcdefg', encoder.decode(encoder.encode('abcdefg')))

    def test_ascii_msgpack_base64_ascii_encode(self):
      encoder = ComposedEncoder(
        text_ascii_encoder,
        msgpack_encoder,
        base64_encoder,
        text_ascii_encoder.inverted)
      self.assertEqual('abcdefg', encoder.decode(encoder.encode('abcdefg')))

    def test_connecting_incompatible_encoders_fails(self):
        if not six.PY2:
          with self.assertRaises(EncoderLinkError) as context:
            encoder = ComposedEncoder(base64_encoder, text_ascii_encoder)

if __name__ == '__main__':
    unittest.main()