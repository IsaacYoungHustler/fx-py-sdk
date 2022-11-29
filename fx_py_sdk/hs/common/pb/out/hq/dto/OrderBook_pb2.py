# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hq/dto/OrderBook.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hq/dto/OrderBook.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n2com.huasheng.quant.open.sdk.protobuf.hq.common.dtoB\016OrderBookProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16hq/dto/OrderBook.proto\"N\n\tOrderBook\x12\r\n\x05level\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0e\n\x06volume\x18\x03 \x01(\x03\x12\x13\n\x0borederCount\x18\x04 \x01(\x05\x42\x44\n2com.huasheng.quant.open.sdk.protobuf.hq.common.dtoB\x0eOrderBookProtob\x06proto3'
)




_ORDERBOOK = _descriptor.Descriptor(
  name='OrderBook',
  full_name='OrderBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='OrderBook.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='OrderBook.price', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='OrderBook.volume', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orederCount', full_name='OrderBook.orederCount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['OrderBook'] = _ORDERBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderBook = _reflection.GeneratedProtocolMessageType('OrderBook', (_message.Message,), {
  'DESCRIPTOR' : _ORDERBOOK,
  '__module__' : 'hq.dto.OrderBook_pb2'
  # @@protoc_insertion_point(class_scope:OrderBook)
  })
_sym_db.RegisterMessage(OrderBook)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
