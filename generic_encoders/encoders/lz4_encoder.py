import lz4.frame
import six

from .encoder import Encoder

class Lz4Encoder(Encoder):
  file_suffixes = ['lz4']
  inputs = [six.binary_type]
  outputs = six.binary_type

  def __init__(self):
    super(Lz4Encoder, self)

  def _encode(self, data):
    return lz4.frame.compress(data)

  def _decode(self, data):
    return lz4.frame.decompress(data)
