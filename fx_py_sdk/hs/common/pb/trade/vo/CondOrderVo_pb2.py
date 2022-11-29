# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/vo/CondOrderVo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/vo/CondOrderVo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n-com.huasheng.quant.open.sdk.protobuf.trade.voB\020CondOrderVoProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1atrade/vo/CondOrderVo.proto\"\xc2\x03\n\x0b\x43ondOrderVo\x12\x13\n\x0b\x63ondOrderId\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x02 \x01(\t\x12\x11\n\tstockCode\x18\x03 \x01(\t\x12\x11\n\tstockName\x18\x04 \x01(\t\x12\x13\n\x0bstockNameTc\x18\x05 \x01(\t\x12\x13\n\x0bstockNameEn\x18\x06 \x01(\t\x12\x14\n\x0c\x65xchangeType\x18\x07 \x01(\t\x12\x13\n\x0b\x65ntrustType\x18\x08 \x01(\t\x12\x13\n\x0bsessionType\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x13\n\x0b\x63\x61nBeCancel\x18\x0b \x01(\t\x12\x13\n\x0b\x63\x61nBeModify\x18\x0c \x01(\t\x12\x11\n\tentrustBs\x18\r \x01(\t\x12\x15\n\rentrustAmount\x18\x0e \x01(\t\x12\x12\n\ncreateTime\x18\x0f \x01(\t\x12\x11\n\tstartTime\x18\x10 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x11 \x01(\t\x12\x11\n\terrorCode\x18\x12 \x01(\t\x12\x10\n\x08\x65rrorMsg\x18\x13 \x01(\t\x12\x11\n\tcondValue\x18\x14 \x01(\t\x12\x11\n\tcondPrice\x18\x15 \x01(\t\x12\x15\n\rcondTrackType\x18\x16 \x01(\tBA\n-com.huasheng.quant.open.sdk.protobuf.trade.voB\x10\x43ondOrderVoProtob\x06proto3'
)




_CONDORDERVO = _descriptor.Descriptor(
  name='CondOrderVo',
  full_name='CondOrderVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='condOrderId', full_name='CondOrderVo.condOrderId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='CondOrderVo.dataType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stockCode', full_name='CondOrderVo.stockCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stockName', full_name='CondOrderVo.stockName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stockNameTc', full_name='CondOrderVo.stockNameTc', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stockNameEn', full_name='CondOrderVo.stockNameEn', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchangeType', full_name='CondOrderVo.exchangeType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustType', full_name='CondOrderVo.entrustType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sessionType', full_name='CondOrderVo.sessionType', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='CondOrderVo.status', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canBeCancel', full_name='CondOrderVo.canBeCancel', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canBeModify', full_name='CondOrderVo.canBeModify', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustBs', full_name='CondOrderVo.entrustBs', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entrustAmount', full_name='CondOrderVo.entrustAmount', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='CondOrderVo.createTime', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='CondOrderVo.startTime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='CondOrderVo.endTime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='CondOrderVo.errorCode', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errorMsg', full_name='CondOrderVo.errorMsg', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='condValue', full_name='CondOrderVo.condValue', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='condPrice', full_name='CondOrderVo.condPrice', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='condTrackType', full_name='CondOrderVo.condTrackType', index=21,
      number=22, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=481,
)

DESCRIPTOR.message_types_by_name['CondOrderVo'] = _CONDORDERVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CondOrderVo = _reflection.GeneratedProtocolMessageType('CondOrderVo', (_message.Message,), {
  'DESCRIPTOR' : _CONDORDERVO,
  '__module__' : 'trade.vo.CondOrderVo_pb2'
  # @@protoc_insertion_point(class_scope:CondOrderVo)
  })
_sym_db.RegisterMessage(CondOrderVo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)