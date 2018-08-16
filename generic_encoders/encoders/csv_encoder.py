import csv
import six
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from itertools import chain
try:
    from itertools import imap
except ImportError:
    # Python 3...
    imap=map

from datetime import date, datetime
from .encoder import Encoder


class CsvEncoder(Encoder):
  file_suffixes = ['csv']
  inputs = [list]
  outputs = str

  def __init__(self, write_header=True, fieldnames=None):
    self.fieldnames = fieldnames
    self.write_header = write_header

  def _encode(self, data):
    if self.fieldnames is None:
        fieldnames = set(chain.from_iterable(imap(lambda x: x.keys(), data)))
    else:
        fieldnames = self.fieldnames
    f = StringIO()
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    for record in data:
        writer.writerow(record)
    return f.getvalue()

  def _decode(self, data):
    f = StringIO(data)
    reader = csv.DictReader(f, self.fieldnames)
    return [x for x in reader]