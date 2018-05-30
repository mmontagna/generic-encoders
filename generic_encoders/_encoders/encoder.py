
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

  def __init__(self):
    if not hasattr(self, 'inputs'):
      raise NotImplementedError('Encoders must set inputs')

    if not hasattr(self, 'outputs'):
      raise NotImplementedError('Encoders must set outputs')

  def _encode(self, data):
    raise NotImplementedError('encode')

  def _decode(self, data):
    raise NotImplementedError('decode')

  def type_matches(self, data, inputs):
    for _type in inputs:
      if isinstance(data, _type):
        return True
    return False

  def encode(self, data):
    if not self.type_matches(data, self.inputs):
      raise TypeError('''
        {} cannot encode type '{}' acceptable types are ({})
        '''.strip().format(
          self.__class__.__name__,
          type(data).__name__,
          ','.join(["'{}'".format(x.__name__) for x in self.inputs])
          ))
    return self._encode(data)

  def decode(self, data):
    if not self.type_matches(data, [self.outputs]):
      raise TypeError('''
        {} cannot decode type '{}' acceptable type is '{}'
        '''.strip().format(
          self.__class__.__name__,
          type(data).__name__,
          self.outputs.__name__
          ))
    return self._decode(data)

