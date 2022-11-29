# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/vo/futures/FuturesFundInfoVo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/vo/futures/FuturesFundInfoVo.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n5com.huasheng.quant.open.sdk.protobuf.trade.vo.futuresB\026FuturesFundInfoVoProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(trade/vo/futures/FuturesFundInfoVo.proto\"\xa8\x03\n\x11\x46uturesFundInfoVo\x12\x14\n\x0c\x61ssetBalance\x18\x01 \x01(\t\x12\x15\n\renableBalance\x18\x02 \x01(\t\x12\x12\n\nmarginCall\x18\x03 \x01(\t\x12\x15\n\rincomeBalance\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61shBal\x18\x05 \x01(\t\x12\x0f\n\x07iMargin\x18\x06 \x01(\t\x12\x0f\n\x07mMargin\x18\x07 \x01(\t\x12\x13\n\x0bmarginLevel\x18\x08 \x01(\t\x12\x11\n\tmaxMargin\x18\t \x01(\t\x12\x13\n\x0b\x63reditLimit\x18\n \x01(\t\x12\x11\n\tctrlLevel\x18\x0b \x01(\t\x12\x13\n\x0bmarginClass\x18\x0c \x01(\t\x12\x0c\n\x04\x61\x65Id\x18\r \x01(\t\x12\x12\n\ncashBalHKD\x18\x0e \x01(\t\x12\x12\n\ncashBalUSD\x18\x0f \x01(\t\x12\x17\n\x0f\x63ycRateUSDtoHSD\x18\x10 \x01(\t\x12\x14\n\x0cmarginStatus\x18\x11 \x01(\t\x12\x15\n\rstatusPercent\x18\x12 \x01(\t\x12\x13\n\x0b\x63loseProfit\x18\x13 \x01(\t\x12\x12\n\ncashBalCNH\x18\x14 \x01(\tBO\n5com.huasheng.quant.open.sdk.protobuf.trade.vo.futuresB\x16\x46uturesFundInfoVoProtob\x06proto3'
)




_FUTURESFUNDINFOVO = _descriptor.Descriptor(
  name='FuturesFundInfoVo',
  full_name='FuturesFundInfoVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assetBalance', full_name='FuturesFundInfoVo.assetBalance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enableBalance', full_name='FuturesFundInfoVo.enableBalance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marginCall', full_name='FuturesFundInfoVo.marginCall', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='incomeBalance', full_name='FuturesFundInfoVo.incomeBalance', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cashBal', full_name='FuturesFundInfoVo.cashBal', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iMargin', full_name='FuturesFundInfoVo.iMargin', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mMargin', full_name='FuturesFundInfoVo.mMargin', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marginLevel', full_name='FuturesFundInfoVo.marginLevel', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxMargin', full_name='FuturesFundInfoVo.maxMargin', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creditLimit', full_name='FuturesFundInfoVo.creditLimit', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ctrlLevel', full_name='FuturesFundInfoVo.ctrlLevel', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marginClass', full_name='FuturesFundInfoVo.marginClass', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aeId', full_name='FuturesFundInfoVo.aeId', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cashBalHKD', full_name='FuturesFundInfoVo.cashBalHKD', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cashBalUSD', full_name='FuturesFundInfoVo.cashBalUSD', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cycRateUSDtoHSD', full_name='FuturesFundInfoVo.cycRateUSDtoHSD', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marginStatus', full_name='FuturesFundInfoVo.marginStatus', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statusPercent', full_name='FuturesFundInfoVo.statusPercent', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='closeProfit', full_name='FuturesFundInfoVo.closeProfit', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cashBalCNH', full_name='FuturesFundInfoVo.cashBalCNH', index=19,
      number=20, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=469,
)

DESCRIPTOR.message_types_by_name['FuturesFundInfoVo'] = _FUTURESFUNDINFOVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FuturesFundInfoVo = _reflection.GeneratedProtocolMessageType('FuturesFundInfoVo', (_message.Message,), {
  'DESCRIPTOR' : _FUTURESFUNDINFOVO,
  '__module__' : 'trade.vo.futures.FuturesFundInfoVo_pb2'
  # @@protoc_insertion_point(class_scope:FuturesFundInfoVo)
  })
_sym_db.RegisterMessage(FuturesFundInfoVo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
