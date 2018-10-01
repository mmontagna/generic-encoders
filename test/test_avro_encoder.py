import unittest
import six

from generic_encoders import avro_encoder, AvroEncoder

class TestAvroEncoder(unittest.TestCase):

    def setUp(self):
        self.schema = {
            'doc': 'A weather reading.',
            'name': 'Weather',
            'namespace': 'test',
            'type': 'record',
            'fields': [
                {'name': 'station', 'type': 'string'},
                {'name': 'time', 'type': 'long'},
                {'name': 'temp', 'type': 'int'},
            ],
        }
        self.records = [
            {u'station': u'011990-99999', u'temp': 0, u'time': 1433269388},
            {u'station': u'011990-99999', u'temp': 22, u'time': 1433270389},
            {u'station': u'011990-99999', u'temp': -11, u'time': 1433273379},
            {u'station': u'012650-99999', u'temp': 111, u'time': 1433275478},
        ]


    def test_avro_encode_decode(self):
        encoder = AvroEncoder(self.schema)
        data = encoder.encode(self.records)
        self.assertEqual(self.records, list(encoder.decode(data)))

    def test_avro_encode_decode_with_snappy(self):
        encoder = AvroEncoder(self.schema, codec='snappy')
        data = encoder.encode(self.records)
        self.assertEqual(self.records, list(encoder.decode(data)))

    def test_avro_encode_decode_with_deflate(self):
        encoder = AvroEncoder(self.schema, codec='deflate')
        data = encoder.encode(self.records)
        self.assertEqual(self.records, list(encoder.decode(data)))

    def test_avro_decoder_doesnt_need_schema(self):
        encoder = AvroEncoder(self.schema)
        data = encoder.encode(self.records)
        self.assertEqual(self.records, list(avro_encoder.decode(data)))


if __name__ == '__main__':
    unittest.main()