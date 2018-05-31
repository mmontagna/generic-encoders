from .encoders.gzip_encoder import GzipEncoder
from .encoders.base64_encoder import Base64Encoder
from .encoders.lz4_encoder import Lz4Encoder
from .encoders.json_encoder import JsonEncoder
from .encoders.dill_encoder import DillEncoder

base64 = Base64Encoder()
gzip = GzipEncoder()
lz4 = Lz4Encoder()
json = JsonEncoder()
dill = DillEncoder()
