import gzip
from io import BytesIO
import six

from .encoder import Encoder

class GzipEncoder(Encoder):
  file_suffixes = ['gz', 'gzip']
  inputs = [six.binary_type]
  outputs = six.binary_type

  def __init__(self):
    super(GzipEncoder, self)

  def _encode(self, data):
    fgz = BytesIO()
    gzip_obj = gzip.GzipFile(mode='wb', fileobj=fgz)
    gzip_obj.write(data)
    gzip_obj.close()
    return fgz.getvalue()

  def _decode(self, data):
    fgz = BytesIO(data)
    gzip_obj = gzip.GzipFile(mode='r', fileobj=fgz)
    return gzip_obj.read()
