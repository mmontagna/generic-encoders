import six

from .encoder import Encoder

class TextEncoder(Encoder):
  file_suffixes = ['txt']
  inputs = six.string_types
  outputs = six.binary_type

  def __init__(self, encoding='utf-8'):
    self.encoding = encoding
    #self.file_suffixes = [encoding.replace('-', '')]
    super(TextEncoder, self)

  def _encode(self, data):
    return data.encode(self.encoding)

  def _decode(self, data):
    return data.decode(self.encoding)
