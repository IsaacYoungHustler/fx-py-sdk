# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/response/TradeQueryHistoryCondOrderListResponse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hs.common.pb.trade.vo import CondOrderVo_pb2 as trade_dot_vo_dot_CondOrderVo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/response/TradeQueryHistoryCondOrderListResponse.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n3com.huasheng.quant.open.sdk.protobuf.trade.responseB+TradeQueryHistoryCondOrderListResponseProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;trade/response/TradeQueryHistoryCondOrderListResponse.proto\x1a\x1atrade/vo/CondOrderVo.proto\"\x80\x01\n&TradeQueryHistoryCondOrderListResponse\x12\x1a\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0c.CondOrderVo\x12\x11\n\tcurPageNo\x18\x02 \x01(\x05\x12\x13\n\x0b\x63urPageSize\x18\x03 \x01(\x05\x12\x12\n\ntotalPages\x18\x04 \x01(\x03\x42\x62\n3com.huasheng.quant.open.sdk.protobuf.trade.responseB+TradeQueryHistoryCondOrderListResponseProtob\x06proto3'
  ,
  dependencies=[trade_dot_vo_dot_CondOrderVo__pb2.DESCRIPTOR,])




_TRADEQUERYHISTORYCONDORDERLISTRESPONSE = _descriptor.Descriptor(
  name='TradeQueryHistoryCondOrderListResponse',
  full_name='TradeQueryHistoryCondOrderListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TradeQueryHistoryCondOrderListResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curPageNo', full_name='TradeQueryHistoryCondOrderListResponse.curPageNo', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curPageSize', full_name='TradeQueryHistoryCondOrderListResponse.curPageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalPages', full_name='TradeQueryHistoryCondOrderListResponse.totalPages', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=92,
  serialized_end=220,
)

_TRADEQUERYHISTORYCONDORDERLISTRESPONSE.fields_by_name['data'].message_type = trade_dot_vo_dot_CondOrderVo__pb2._CONDORDERVO
DESCRIPTOR.message_types_by_name['TradeQueryHistoryCondOrderListResponse'] = _TRADEQUERYHISTORYCONDORDERLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradeQueryHistoryCondOrderListResponse = _reflection.GeneratedProtocolMessageType('TradeQueryHistoryCondOrderListResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRADEQUERYHISTORYCONDORDERLISTRESPONSE,
  '__module__' : 'trade.response.TradeQueryHistoryCondOrderListResponse_pb2'
  # @@protoc_insertion_point(class_scope:TradeQueryHistoryCondOrderListResponse)
  })
_sym_db.RegisterMessage(TradeQueryHistoryCondOrderListResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
