# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/vo/futures/FuturesProductInfoVo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/vo/futures/FuturesProductInfoVo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n5com.huasheng.quant.open.sdk.protobuf.trade.vo.futuresB\031FuturesProductInfoVoProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+trade/vo/futures/FuturesProductInfoVo.proto\"\xb9\x01\n\x14\x46uturesProductInfoVo\x12\x10\n\x08prodCode\x18\x01 \x01(\t\x12\x10\n\x08instCode\x18\x02 \x01(\t\x12\x0f\n\x07lotSize\x18\x03 \x01(\x05\x12\x12\n\ndecInPrice\x18\x04 \x01(\x05\x12\x14\n\x0c\x63ontractSize\x18\x05 \x01(\t\x12\x19\n\x11priceDecimalPoint\x18\x06 \x01(\t\x12\x12\n\nexpiryDate\x18\x07 \x01(\t\x12\x13\n\x0bisSupportT1\x18\x08 \x01(\x05\x42R\n5com.huasheng.quant.open.sdk.protobuf.trade.vo.futuresB\x19\x46uturesProductInfoVoProtob\x06proto3'
)




_FUTURESPRODUCTINFOVO = _descriptor.Descriptor(
  name='FuturesProductInfoVo',
  full_name='FuturesProductInfoVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prodCode', full_name='FuturesProductInfoVo.prodCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instCode', full_name='FuturesProductInfoVo.instCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lotSize', full_name='FuturesProductInfoVo.lotSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decInPrice', full_name='FuturesProductInfoVo.decInPrice', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractSize', full_name='FuturesProductInfoVo.contractSize', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priceDecimalPoint', full_name='FuturesProductInfoVo.priceDecimalPoint', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiryDate', full_name='FuturesProductInfoVo.expiryDate', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isSupportT1', full_name='FuturesProductInfoVo.isSupportT1', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=48,
  serialized_end=233,
)

DESCRIPTOR.message_types_by_name['FuturesProductInfoVo'] = _FUTURESPRODUCTINFOVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FuturesProductInfoVo = _reflection.GeneratedProtocolMessageType('FuturesProductInfoVo', (_message.Message,), {
  'DESCRIPTOR' : _FUTURESPRODUCTINFOVO,
  '__module__' : 'trade.vo.futures.FuturesProductInfoVo_pb2'
  # @@protoc_insertion_point(class_scope:FuturesProductInfoVo)
  })
_sym_db.RegisterMessage(FuturesProductInfoVo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)