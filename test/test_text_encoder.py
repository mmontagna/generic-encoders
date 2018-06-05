# -*- coding: utf-8 -*-
import unittest

from generic_encoders import (
    text_utf8,
    text_ascii,
    text_latin_1
    )

class TestTextEncoder(unittest.TestCase):

    def test_ascii_encoder(self):
        self.assertEqual(
            'abc',
            text_ascii.decode(text_ascii.encode('abc'))
            )

    def test_utf8_encoder(self):
        self.assertEqual(
            u'русский язык',
            text_utf8.decode(text_utf8.encode(u'русский язык'))
            )



if __name__ == '__main__':
    unittest.main()