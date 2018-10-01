import six

from .encoder import Encoder


def _print_import_error():
  print("Unable to import snappy please install generic-encoders[snappy] & snappy system packages.")

class SnappyEncoder(Encoder):
  file_suffixes = ['snappy']
  inputs = [six.binary_type]
  outputs = six.binary_type

  def __init__(self):
    super(SnappyEncoder, self)

  def _encode(self, data):
    try:
        import snappy
    except ImportError:
        _print_import_error()
        raise
    return snappy.compress(data)

  def _decode(self, data):
    try:
        import snappy
    except ImportError:
        _print_import_error()
        raise
    return snappy.decompress(data)