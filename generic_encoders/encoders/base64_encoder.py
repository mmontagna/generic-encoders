import base64
import six
from .encoder import Encoder

class Base64Encoder(Encoder):
  file_suffixes = ['b64', 'base64']
  inputs = [six.binary_type]
  outputs = six.binary_type
  def __init__(self):
    super(Base64Encoder, self)

  _encode = staticmethod(base64.b64encode)
  _decode = staticmethod(base64.b64decode)

class UrlBase64Encoder(Encoder):
  file_suffixes = ['b64', 'base64']
  inputs = [six.binary_type]
  outputs = six.binary_type
  def __init__(self):
    super(UrlBase64Encoder, self)

  _encode = staticmethod(base64.urlsafe_b64encode)
  _decode = staticmethod(base64.urlsafe_b64decode)
