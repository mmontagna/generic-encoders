from generic_encoders.encoders.gzip_encoder import Encoder
from generic_encoders.encoders.gzip_encoder import GzipEncoder
from generic_encoders.encoders.base64_encoder import Base64Encoder, UrlBase64Encoder
from generic_encoders.encoders.lz4_encoder import Lz4Encoder
from generic_encoders.encoders.json_encoder import JsonEncoder
from generic_encoders.encoders.dill_encoder import DillEncoder
from generic_encoders.encoders.msgpack_encoder import MsgPackEncoder
from generic_encoders.encoders.text_encoder import TextEncoder
from generic_encoders.encoders.composed_encoder import ComposedEncoder

base64 = Base64Encoder()
url_base64 = UrlBase64Encoder()
gzip = GzipEncoder()
lz4 = Lz4Encoder()
json = JsonEncoder()
dill = DillEncoder()
msgpack = MsgPackEncoder()

text_utf8 = TextEncoder(encoding='utf-8')
text_ascii = TextEncoder(encoding='ascii')
text_latin_1 = TextEncoder(encoding='latin-1')

Encoder.add_encoder(base64)
Encoder.add_encoder(gzip)
Encoder.add_encoder(lz4)
Encoder.add_encoder(json)
Encoder.add_encoder(dill)
Encoder.add_encoder(msgpack)
Encoder.add_encoder(text_utf8)
Encoder.add_encoder(text_ascii)
Encoder.add_encoder(text_latin_1)
