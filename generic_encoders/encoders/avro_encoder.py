import six
import types
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from fastavro import writer, reader, parse_schema
except ImportError:
    print("Unable to import fastavro dependencies please install generic-encoders[avro]")
    raise

from .encoder import Encoder


class AvroEncoder(Encoder):
  file_suffixes = ['avro']
  inputs = [list, types.GeneratorType]
  outputs = six.binary_type

  def __init__(self, avro_schema):
    self.avro_schema = avro_schema
    self.parsed_avro_schema = parse_schema(avro_schema)

  def _encode(self, data):
    out = StringIO()
    writer(out, self.parsed_avro_schema, data)
    return out.getvalue()

  def _decode(self, data):
    fo = StringIO(data)
    for record in reader(fo):
      yield record
