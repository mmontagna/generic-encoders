import six

from .encoder import Encoder

class UnknownFormatException(Exception): pass
class EncoderLinkError(Exception): pass

class ComposedEncoder(Encoder):
  encoder_cache = {}

  def validate_encoder_connections(self, encoder, next_encoder):
    if not any([issubclass(encoder.outputs, x) for x in next_encoder.inputs]):
      raise EncoderLinkError(
        "Cannot connect {} which outputs ({}) to {} which accepts ({})".format(
          encoder,
          encoder.outputs,
          next_encoder,
          next_encoder.inputs
          ))

  def __init__(self, *args, **kwargs):
    self.encoders = args
    self.include_header = kwargs.get('include_header', False)
    self.check_for_headers = kwargs.get('check_for_headers', True)
    self.file_suffixes = []
    self.inputs = self.encoders[0].inputs
    self.outputs = self.encoders[-1].outputs
    last_encoder = None
    for encoder in self.encoders:
      if last_encoder:
        self.validate_encoder_connections(last_encoder, encoder)
      last_encoder = encoder
      self.file_suffixes.append(encoder.file_suffixes[0])

    self.header_prefix = kwargs.get('header_prefix', 'gpak') + '[' 
    self.header = '{}{}]'.format(
      self.header_prefix,
      '.'.join(self.file_suffixes))

  def has_header(self, data):
    if isinstance(data, six.string_types):
      return data.startswith(self.header_prefix)
    elif isinstance(data, six.binary_type):
      return data.startswith(self.header_prefix.encode('utf8'))
    return False

  @property
  def name(self):
    return ".".join([x.name for x in self.encoders])

  def split_header(self, data):
    header = self.header_prefix
    i = data.index('[')
    j = data.index(']')
    return data[i+1:j], data[j+1:]

  def _encode(self, data):
    for encoder in self.encoders:
      data = encoder.encode(data)
    if self.include_header:
      return self.header + data
    else:
      return data

  @classmethod
  def build_encoder_from_header(self, header):
    if header not in self.encoder_cache:
      parts = header.split('.')
      encoders = []
      for part in parts:
        if part not in self.all_file_suffixes:
          raise UnknownFormatException(part)
        encoders.append(self.all_file_suffixes[part])
      self.encoder_cache[header] = ComposedEncoder(*encoders)
    return self.encoder_cache[header]

  def _decode(self, data):
    if self.check_for_headers and self.has_header(data):
      header, data = self.split_header(data)
      encoder = self.build_encoder_from_header(header)
      return encoder.decode(data)

    for encoder in self.encoders[::-1]:
      data = encoder.decode(data)
    return data
