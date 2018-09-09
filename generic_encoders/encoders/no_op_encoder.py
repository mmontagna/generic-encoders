from .encoder import Encoder


class NoOpEncoder(object):
  file_suffixes = []
  inputs = [object]
  outputs = object

  def encode(self, data):
    return data

  def decode(self, data):
    return data
