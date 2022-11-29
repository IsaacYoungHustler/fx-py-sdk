# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/request/TradeChangeEntrustRequest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/request/TradeChangeEntrustRequest.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n2com.huasheng.quant.open.sdk.protobuf.trade.requestB\036TradeChangeEntrustRequestProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-trade/request/TradeChangeEntrustRequest.proto\"\xeb\x01\n\x19TradeChangeEntrustRequest\x12\x14\n\x0c\x65xchangeType\x18\x01 \x01(\t\x12\x15\n\rentrustAmount\x18\x02 \x01(\t\x12\x14\n\x0c\x65ntrustPrice\x18\x03 \x01(\t\x12\x11\n\tentrustId\x18\x04 \x01(\t\x12\x11\n\tstockCode\x18\x05 \x01(\t\x12\x13\n\x0b\x65ntrustType\x18\x06 \x01(\t\x12\x13\n\x0bsessionType\x18\x07 \x01(\t\x12\x11\n\tvalidDays\x18\x08 \x01(\t\x12\x11\n\tcondValue\x18\t \x01(\t\x12\x15\n\rcondTrackType\x18\n \x01(\tBT\n2com.huasheng.quant.open.sdk.protobuf.trade.requestB\x1eTradeChangeEntrustRequestProtob\x06proto3'
)




_TRADECHANGEENTRUSTREQUEST = _descriptor.Descriptor(
  name='TradeChangeEntrustRequest',
  full_name='TradeChangeEntrustRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchangeType', full_name='TradeChangeEntrustRequest.exchangeType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustAmount', full_name='TradeChangeEntrustRequest.entrustAmount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustPrice', full_name='TradeChangeEntrustRequest.entrustPrice', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustId', full_name='TradeChangeEntrustRequest.entrustId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stockCode', full_name='TradeChangeEntrustRequest.stockCode', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustType', full_name='TradeChangeEntrustRequest.entrustType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionType', full_name='TradeChangeEntrustRequest.sessionType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validDays', full_name='TradeChangeEntrustRequest.validDays', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='condValue', full_name='TradeChangeEntrustRequest.condValue', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='condTrackType', full_name='TradeChangeEntrustRequest.condTrackType', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=50,
  serialized_end=285,
)

DESCRIPTOR.message_types_by_name['TradeChangeEntrustRequest'] = _TRADECHANGEENTRUSTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradeChangeEntrustRequest = _reflection.GeneratedProtocolMessageType('TradeChangeEntrustRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRADECHANGEENTRUSTREQUEST,
  '__module__' : 'trade.request.TradeChangeEntrustRequest_pb2'
  # @@protoc_insertion_point(class_scope:TradeChangeEntrustRequest)
  })
_sym_db.RegisterMessage(TradeChangeEntrustRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
