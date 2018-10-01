import six
import types
try:
    from io import BytesIO
except ImportError:
    from io import BytesIO

from .encoder import Encoder

def _print_import_error():
  print("Unable to import fastavro dependencies please install generic-encoders[avro]")

class AvroEncoder(Encoder):
  file_suffixes = ['avro']
  inputs = [list, types.GeneratorType]
  outputs = six.binary_type

  def __init__(self, avro_schema = None, codec='null', sync_interval=16000):
    self.avro_schema = avro_schema
    if avro_schema:
      try:
          from fastavro import parse_schema
      except ImportError:
        _print_import_error()
        raise
      self.parsed_avro_schema = parse_schema(avro_schema)
    else:
      self.parsed_avro_schema = None

    self.codec = codec
    self.sync_interval = sync_interval

  def _encode(self, data):
    try:
        from fastavro import writer
    except ImportError:
        _print_import_error()
        raise
    out = BytesIO()
    writer(out, self.parsed_avro_schema, data, codec=self.codec, sync_interval=self.sync_interval)
    return out.getvalue()

  def _decode(self, data):
    try:
        from fastavro import reader
    except ImportError:
        _print_import_error()
        raise
    fo = BytesIO(data)
    for record in reader(fo):
      yield record
