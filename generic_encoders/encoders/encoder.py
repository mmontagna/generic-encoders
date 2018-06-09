
class Encoder(object):
  """
  Encoder is an abstract class which defines an interface
  for encoding data.

  Subclasses must provide a inputs class variable which lists acceptable
  input types.

  Subclasses must also provide an outputs class variable which specifies the
  output type produced.

  Subclasses may optionally provide a file_suffixes class variable which
  lists the possible suffixes files encoded via this encoder may be stored as.
  """

  file_suffixes = []
  all_file_suffixes = {}

  @classmethod
  def add_encoder(cls, encoder):
    for file_suffix in encoder.file_suffixes:
      cls.all_file_suffixes[file_suffix] = encoder

  def __init__(self):
    if not hasattr(self, 'inputs'):
      raise NotImplementedError('Encoders must set inputs')

    if not hasattr(self, 'outputs'):
      raise NotImplementedError('Encoders must set outputs')

  @property
  def inverted(self):
    return InvertedEncoder(self)

  def _encode(self, data):
    raise NotImplementedError('encode')

  def _decode(self, data):
    raise NotImplementedError('decode')

  def type_matches(self, data, inputs):
    for _type in inputs:
      if isinstance(data, _type):
        return True
    return False

  @property
  def name(self):
    return self.__class__.__name__

  def encode(self, data):
    if not self.type_matches(data, self.inputs):
      raise TypeError('''
        {} cannot encode type '{}' acceptable types are ({})
        '''.strip().format(
          self.name,
          type(data).__name__,
          ','.join(["'{}'".format(x.__name__) for x in self.inputs])
          ))
    return self._encode(data)

  def decode(self, data):
    if not self.type_matches(data, [self.outputs]):
      raise TypeError('''
        {} cannot decode type '{}' acceptable type is '{}'
        '''.strip().format(
          self.name,
          type(data).__name__,
          self.outputs.__name__
          ))
    return self._decode(data)


class InvertedEncoder(Encoder):

  def __init__(self, encoder):
    self.encoder = encoder
    self.file_suffixes = []
    for suffix in encoder.file_suffixes:
      self.file_suffixes.append('invert' + suffix)
    self.inputs = [encoder.outputs]
    self.outputs = encoder.inputs[0]

  def encode(self, data):
    return self.encoder.decode(data)

  def decode(self, data):
    return self.encoder.encode(data)
