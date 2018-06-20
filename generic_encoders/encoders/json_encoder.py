import simplejson as json
import six

from datetime import date, datetime
from .encoder import Encoder


class JsonEncoder(Encoder):
  file_suffixes = ['json']
  inputs = [object]
  outputs = six.string_types[0]

  def __init__(self, sort_keys=True, skip_errors=False, default=None):
    self.sort_keys = sort_keys
    self.default = default
    if self.default and skip_errors:
      raise ValueError("Only one of skip_errors and default may be passed.")
    if not self.default:
      if skip_errors:
        self.default = self._json_serial_force
      else:
        self.default = self._json_serial
    super(JsonEncoder, self)

  def _encode(self, data):
    return json.dumps(
      data,
      sort_keys=self.sort_keys,
      default=self.default
      )

  def _decode(self, data):
    return json.loads(data)

  def _json_serial(self, obj):
      if isinstance(obj, (datetime, date)):
          return obj.isoformat()
      raise TypeError("Type {} not serializable".format(type(obj)))

  def _json_serial_force(self, obj):
      if isinstance(obj, (datetime, date)):
          return obj.isoformat()
      return str(obj)
