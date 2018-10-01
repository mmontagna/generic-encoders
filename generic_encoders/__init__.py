from generic_encoders.encoders.gzip_encoder import Encoder
from generic_encoders.encoders.gzip_encoder import GzipEncoder
from generic_encoders.encoders.base64_encoder import Base64Encoder, UrlBase64Encoder
from generic_encoders.encoders.lz4_encoder import Lz4Encoder
from generic_encoders.encoders.json_encoder import JsonEncoder
from generic_encoders.encoders.dill_encoder import DillEncoder
from generic_encoders.encoders.msgpack_encoder import MsgPackEncoder
from generic_encoders.encoders.text_encoder import TextEncoder
from generic_encoders.encoders.csv_encoder import CsvEncoder
from generic_encoders.encoders.composed_encoder import ComposedEncoder
from generic_encoders.encoders.avro_encoder import AvroEncoder
from generic_encoders.encoders.snappy_encoder import SnappyEncoder


base64_encoder = Base64Encoder()
url_base64_encoder = UrlBase64Encoder()
gzip_encoder = GzipEncoder()
lz4_encoder = Lz4Encoder()
json_encoder = JsonEncoder()
dill_encoder = DillEncoder()
msgpack_encoder = MsgPackEncoder()
csv_encoder = CsvEncoder()
avro_encoder = AvroEncoder()
snappy_encoder = SnappyEncoder()

text_utf8_encoder = TextEncoder(encoding='utf-8')
text_ascii_encoder = TextEncoder(encoding='ascii')
text_latin_1_encoder = TextEncoder(encoding='latin-1')

Encoder.add_encoder(base64_encoder)
Encoder.add_encoder(gzip_encoder)
Encoder.add_encoder(lz4_encoder)
Encoder.add_encoder(json_encoder)
Encoder.add_encoder(dill_encoder)
Encoder.add_encoder(msgpack_encoder)
Encoder.add_encoder(text_utf8_encoder)
Encoder.add_encoder(text_ascii_encoder)
Encoder.add_encoder(text_latin_1_encoder)
Encoder.add_encoder(csv_encoder)
Encoder.add_encoder(avro_encoder)
Encoder.add_encoder(snappy_encoder)
