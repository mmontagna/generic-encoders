import unittest
import six

from generic_encoders import msgpack, MsgPackEncoder

class TestMsgpackEncoder(unittest.TestCase):

    def test_msgpack_encoder_mixed_type(self):
        obj = {'a': 123, 'b': (1,2,{'c': 3})}
        self.assertEqual(
          obj,
          msgpack.decode(
            msgpack.encode(obj)))

    def test_msgpack_encoder_converts_lists_to_tuples_by_default(self):
        l = [1,2,3]
        self.assertEqual(
          (1,2,3),
          msgpack.decode(
            msgpack.encode(l)))

    def test_msgpack_encoder_use_list(self):
        l = [1,2,3]
        encoder = MsgPackEncoder(use_list=True)
        self.assertEqual(
          l,
          encoder.decode(
            encoder.encode(l)))

    def test_msgpack_accepts_utf8_strings(self):
        string = '\xd1\x80\xd1\x83\xcc\x81\xd1\x81\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9'
        encoder = MsgPackEncoder()
        self.assertEqual(
          string,
          encoder.decode(
            encoder.encode(string)))

    def test_msgpack_accepts_binary_data(self):
        string = b'\xc3\x83'
        encoder = MsgPackEncoder(raw=True, use_bin_type=True)
        self.assertEqual(
          string,
          encoder.decode(
            encoder.encode(string)))


if __name__ == '__main__':
    unittest.main()