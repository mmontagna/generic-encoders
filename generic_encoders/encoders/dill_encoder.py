import dill
import six

from .encoder import Encoder

class DillEncoder(Encoder):
  file_suffixes = ['dill', 'pkl']
  inputs = [object]
  outputs = six.binary_type

  def __init__(self):
    super(DillEncoder, self)

  def encode(self, data):
    return dill.dumps(data)

  def decode(self, data):
    return dill.loads(data)
