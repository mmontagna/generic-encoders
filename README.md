[![CircleCI](https://circleci.com/gh/mmontagna/generic-encoders/tree/master.svg?style=svg)](https://circleci.com/gh/mmontagna/generic-encoders/tree/master) [![PyPI version](https://badge.fury.io/py/generic-encoders.svg)](https://badge.fury.io/py/generic-encoders)

# Generic encoders for data in python

This package contains an assortment of encoders, serializers, packers, etc...which I've found useful over the years, many of them are composable. 

## Installation

```
$ pip install generic-encoders
```

## Usage 

### Basic Example
```
>>> from generic_encoders import ComposedEncoder, GzipEncoder, Base64Encoder, TextEncoder

>>> print(ComposedEncoder(TextEncoder(), GzipEncoder(), Base64Encoder()).encode('Hello world'))
b'H4sIAI0PKlsC//NIzcnJVyjPL8pJAQBSntaLCwAAAA=='
```

### Combining Encoders

Encoders can be composed via the ComposedEncoder class. A favorite of mine is the MessagePack, lz4, base64, ascii encoder which can be constructed like so:

```
>>> from generic_encoders import ComposedEncoder, MsgPackEncoder, Lz4Encoder, Base64Encoder, TextEncoder

>>> encoder = ComposedEncoder(MsgPackEncoder(), Lz4Encoder(), Base64Encoder(), TextEncoder().inverted)
```

If an encoder is not capable of accepting the output/input of a parent encoder an EncoderLinkError exception will be raised. 

### Inverting Encoders

Encoders can be inverted, so that their input becomes thier output and their output their input via the `inverted` property, this can be particularly useful when dealing with text encoders.

```
>>> TextEncoder().inverted
```

## Supported Encoders

### Binary Data Encoders

* [gzip](#gzip-encoder)
* [lz4](#lz4-encoder)
* [bas64](#base64-encoders)

### Object Encoders

* [dill](#dill-encoder)
* [json](#json-encoder)
* [messagepack](#messagepack-encoder)

### Text Encoders

* [utf8](#utf8-encoder)
* [ascii](#ascii-encoder)
* [latin-1](#latin-1-encoder)


## Binary Data Encoders

### Gzip Encoder

The gzip encoder accepts binary data compresses it and outputs binary data. See https://en.wikipedia.org/wiki/Gzip for more info.

Example:
```
>>> from generic_encoders import GzipEncoder
>>> encoder = GzipEncoder()
>>> print(encoder.decode(encoder.encode(b'hello world')))
b'hello world'
```

### Lz4 Encoder

The lz4 encoder accepts binary data and outputs binary data. It typically takes less time to compress and decompress data than the gzip encoder, at the cost of slightly increased output sizes (around 30%). See https://en.wikipedia.org/wiki/LZ4_(compression_algorithm) for more info.

Example:
```
>>> from generic_encoders import Base64Encoder, UrlBase64Encoder
>>> encoder = Base64Encoder()
>>> print(encoder.decode(encoder.encode(b'hello world')))
b'hello world'
```

### Base64 Encoders

The base64 encoder module provides two base64 encoders a urlsafe base64 encoder `Base64Encoder` and a standard base64 encoder `UrlBase64Encoder`, both of which rely on the implementations in the python base64 module https://docs.python.org/3/library/base64.html

These encoders accept binary data and produce binary data, but not that as these encoders are typically used to produce ascii encoded text it's recommended to combine them with the [text_ascii](#text-ascii) encoder.

Example:
```
>>> from generic_encoders import Base64Encoder
>>> from generic_encoders import ComposedEncoder
>>> from generic_encoders import TextEncoder
>>> encoder = ComposedEncoder(Base64Encoder(), TextEncoder(encoding='ascii').inverted)
>>> print(encoder.decode(encoder.encode(b'hello world')))
b'hello world'
```

## Object Encoders

### Json Encoder

The json encoder accepts any json encodable type and outputs a string type.

By default the encoder serializes all types simplejson can encode + it formats date and datetime objects as  [iso8601](https://en.wikipedia.org/wiki/ISO_8601) the types it can encode can be configured by passing in a default encoder function via the `default` constructor argument.

It can also be configued to skip encoding errors instead reverting to calling str() on unknown objects, which can be useful for in some circumstances where precise serialization is not required (eg serializating an exception/stack trace).

See https://en.wikipedia.org/wiki/JSON for more info.

Example:
```
>>> from generic_encoders import JsonEncoder
>>> encoder = JsonEncoder()
>>> print(encoder.decode(encoder.encode({'message': 'hello world'})))
{'message': 'hello world'}
```


### MessagePack Encoder

The MessagePack encoder encodes python objects as packed bytes, it's like a binary json. This encode extends the messagepack format to serialize/deserialize dates and datetimes via messagepack extensions. See https://en.wikipedia.org/wiki/MessagePack for more info.

Example:
```
>>> from generic_encoders import MsgPackEncoder
>>> encoder = MsgPackEncoder()
>>> print(encoder.decode(encoder.encode({'message': 'hello world'})))
{'message': 'hello world'}

```

### Dill Encoder

The dill encoder accepts any picklable python type and outputs bytes all the usual warnings about using dill/picke apply see https://docs.python.org/3/library/pickle.html and https://github.com/uqfoundation/dill for more info.

Example:
```
>>> from generic_encoders import DillEncoder
>>> encoder = DillEncoder()
>>> def i_am_a_teapot():
...   print("Whistle! Whistle!")
... 
>>> encoder.decode(encoder.encode(i_am_a_teapot))()
Whistle! Whistle!
```

## Text Encoders

Text encoders accept string types encode the represented text as binary. 

### utf8 Encoder

Example:
```
>>> from generic_encoders import TextEncoder
>>> encoder = TextEncoder(encoding='utf-8')
>>> encoder.decode(encoder.encode("asd"))
'asd'
```

### ascii Encoder

Example:
```
>>> from generic_encoders import TextEncoder
>>> encoder = TextEncoder(encoding='ascii')
>>> encoder.decode(encoder.encode("asd"))
'asd'
```

### latin-1 Encoder

Example:
```
>>> from generic_encoders import TextEncoder
>>> encoder = TextEncoder(encoding='latin-1')
>>> encoder.decode(encoder.encode("asd"))
'asd'
```
