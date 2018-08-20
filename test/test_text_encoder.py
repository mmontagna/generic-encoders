# -*- coding: utf-8 -*-
import unittest

from generic_encoders import (
    text_utf8_encoder,
    text_ascii_encoder,
    text_latin_1_encoder
    )

class TestTextEncoder(unittest.TestCase):

    def test_ascii_encoder(self):
        self.assertEqual(
            'abc',
            text_ascii_encoder.decode(text_ascii_encoder.encode('abc'))
            )

    def test_utf8_encoder(self):
        self.assertEqual(
            u'русский язык',
            text_utf8_encoder.decode(text_utf8_encoder.encode(u'русский язык'))
            )



if __name__ == '__main__':
    unittest.main()