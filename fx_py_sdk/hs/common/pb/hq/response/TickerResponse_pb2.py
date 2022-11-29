# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hq/response/TickerResponse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hs.common.pb.hq.dto import Security_pb2 as hq_dot_dto_dot_Security__pb2
from hs.common.pb.hq.dto import Ticker_pb2 as hq_dot_dto_dot_Ticker__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hq/response/TickerResponse.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n0com.huasheng.quant.open.sdk.protobuf.hq.responseB\023TickerResponseProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n hq/response/TickerResponse.proto\x1a\x15hq/dto/Security.proto\x1a\x13hq/dto/Ticker.proto\"F\n\x0eTickerResponse\x12\x1b\n\x08security\x18\x01 \x01(\x0b\x32\t.Security\x12\x17\n\x06ticker\x18\x02 \x03(\x0b\x32\x07.TickerBG\n0com.huasheng.quant.open.sdk.protobuf.hq.responseB\x13TickerResponseProtob\x06proto3'
  ,
  dependencies=[hq_dot_dto_dot_Security__pb2.DESCRIPTOR,hq_dot_dto_dot_Ticker__pb2.DESCRIPTOR,])




_TICKERRESPONSE = _descriptor.Descriptor(
  name='TickerResponse',
  full_name='TickerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='TickerResponse.security', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ticker', full_name='TickerResponse.ticker', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=80,
  serialized_end=150,
)

_TICKERRESPONSE.fields_by_name['security'].message_type = hq_dot_dto_dot_Security__pb2._SECURITY
_TICKERRESPONSE.fields_by_name['ticker'].message_type = hq_dot_dto_dot_Ticker__pb2._TICKER
DESCRIPTOR.message_types_by_name['TickerResponse'] = _TICKERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TickerResponse = _reflection.GeneratedProtocolMessageType('TickerResponse', (_message.Message,), {
  'DESCRIPTOR' : _TICKERRESPONSE,
  '__module__' : 'hq.response.TickerResponse_pb2'
  # @@protoc_insertion_point(class_scope:TickerResponse)
  })
_sym_db.RegisterMessage(TickerResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)