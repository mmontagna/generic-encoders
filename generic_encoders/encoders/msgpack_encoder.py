import gc
import struct
import datetime

import msgpack
import six

from .encoder import Encoder

class MsgPackEncoder(Encoder):
  file_suffixes = ['msgpack', 'msgpk']
  inputs = [object]
  outputs = six.binary_type

  def __init__(self, use_list=False, raw=False, use_bin_type=False):
    """
    use_list = False converts tuples to lists for a speed improvement on unpacking.
    """
    self.use_list = use_list
    self.raw = raw
    self.use_bin_type = use_bin_type
    super(MsgPackEncoder, self)

  def _encode(self, data):
    return msgpack.packb(
      data,
      use_bin_type=True,
      default=self._default_packer
      )

  def _decode(self, data):
    try:
      if len(data) > 1000:
        gc.disable()
      return msgpack.unpackb(
        data,
        ext_hook=self._ext_hook,
        use_list=self.use_list,
        raw=self.raw
        )
    finally:
      if len(data) > 1000:
        gc.enable()

  def _default_packer(self, obj):
    if isinstance(obj, datetime.datetime):
      return msgpack.ExtType(100, struct.pack('L', int(obj.strftime("%s"))))
    elif isinstance(obj, datetime.date):
      return msgpack.ExtType(101, struct.pack('L', int(obj.strftime("%s"))))
    raise TypeError("Unknown type: {}".format(obj))

  def _ext_hook(self, code, data):
    if code == 100:
        return datetime.datetime.utcfromtimestamp(struct.unpack('L', data)[0])
    elif code == 101:
        return datetime.date.fromtimestamp(struct.unpack('L', data)[0])
    return msgpack.ExtType(code, data)

    use_bin_type=self.use_bin_type