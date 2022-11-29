# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/request/futures/FuturesEntrustRequest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/request/futures/FuturesEntrustRequest.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n:com.huasheng.quant.open.sdk.protobuf.trade.request.futuresB\032FuturesEntrustRequestProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1trade/request/futures/FuturesEntrustRequest.proto\"\xbf\x01\n\x15\x46uturesEntrustRequest\x12\x11\n\tstockCode\x18\x01 \x01(\t\x12\x13\n\x0b\x65ntrustType\x18\x02 \x01(\t\x12\x14\n\x0c\x65ntrustPrice\x18\x03 \x01(\t\x12\x15\n\rentrustAmount\x18\x04 \x01(\t\x12\x11\n\tentrustBs\x18\x05 \x01(\t\x12\x15\n\rvalidTimeType\x18\x06 \x01(\t\x12\x11\n\tvalidTime\x18\x07 \x01(\t\x12\x14\n\x0corderOptions\x18\x08 \x01(\tBX\n:com.huasheng.quant.open.sdk.protobuf.trade.request.futuresB\x1a\x46uturesEntrustRequestProtob\x06proto3'
)




_FUTURESENTRUSTREQUEST = _descriptor.Descriptor(
  name='FuturesEntrustRequest',
  full_name='FuturesEntrustRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stockCode', full_name='FuturesEntrustRequest.stockCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustType', full_name='FuturesEntrustRequest.entrustType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustPrice', full_name='FuturesEntrustRequest.entrustPrice', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustAmount', full_name='FuturesEntrustRequest.entrustAmount', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustBs', full_name='FuturesEntrustRequest.entrustBs', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validTimeType', full_name='FuturesEntrustRequest.validTimeType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validTime', full_name='FuturesEntrustRequest.validTime', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orderOptions', full_name='FuturesEntrustRequest.orderOptions', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=54,
  serialized_end=245,
)

DESCRIPTOR.message_types_by_name['FuturesEntrustRequest'] = _FUTURESENTRUSTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FuturesEntrustRequest = _reflection.GeneratedProtocolMessageType('FuturesEntrustRequest', (_message.Message,), {
  'DESCRIPTOR' : _FUTURESENTRUSTREQUEST,
  '__module__' : 'trade.request.futures.FuturesEntrustRequest_pb2'
  # @@protoc_insertion_point(class_scope:FuturesEntrustRequest)
  })
_sym_db.RegisterMessage(FuturesEntrustRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
