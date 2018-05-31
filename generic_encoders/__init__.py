from .encoders.gzip_encoder import GzipEncoder
from .encoders.base64_encoder import Base64Encoder
from .encoders.lz4_encoder import Lz4Encoder

base64 = Base64Encoder()
gzip = GzipEncoder()
lz4 = Lz4Encoder()
