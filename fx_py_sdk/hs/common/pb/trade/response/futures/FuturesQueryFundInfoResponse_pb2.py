# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/response/futures/FuturesQueryFundInfoResponse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hs.common.pb.trade.vo.futures import FuturesFundInfoVo_pb2 as trade_dot_vo_dot_futures_dot_FuturesFundInfoVo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/response/futures/FuturesQueryFundInfoResponse.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n;com.huasheng.quant.open.sdk.protobuf.trade.response.futuresB!FuturesQueryFundInfoResponseProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9trade/response/futures/FuturesQueryFundInfoResponse.proto\x1a(trade/vo/futures/FuturesFundInfoVo.proto\"D\n\x1c\x46uturesQueryFundInfoResponse\x12$\n\x08\x66undInfo\x18\x01 \x01(\x0b\x32\x12.FuturesFundInfoVoB`\n;com.huasheng.quant.open.sdk.protobuf.trade.response.futuresB!FuturesQueryFundInfoResponseProtob\x06proto3'
  ,
  dependencies=[trade_dot_vo_dot_futures_dot_FuturesFundInfoVo__pb2.DESCRIPTOR,])




_FUTURESQUERYFUNDINFORESPONSE = _descriptor.Descriptor(
  name='FuturesQueryFundInfoResponse',
  full_name='FuturesQueryFundInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fundInfo', full_name='FuturesQueryFundInfoResponse.fundInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=103,
  serialized_end=171,
)

_FUTURESQUERYFUNDINFORESPONSE.fields_by_name['fundInfo'].message_type = trade_dot_vo_dot_futures_dot_FuturesFundInfoVo__pb2._FUTURESFUNDINFOVO
DESCRIPTOR.message_types_by_name['FuturesQueryFundInfoResponse'] = _FUTURESQUERYFUNDINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FuturesQueryFundInfoResponse = _reflection.GeneratedProtocolMessageType('FuturesQueryFundInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _FUTURESQUERYFUNDINFORESPONSE,
  '__module__' : 'trade.response.futures.FuturesQueryFundInfoResponse_pb2'
  # @@protoc_insertion_point(class_scope:FuturesQueryFundInfoResponse)
  })
_sym_db.RegisterMessage(FuturesQueryFundInfoResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
