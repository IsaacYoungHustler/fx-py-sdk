# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hq/dto/TimeShare.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hs.common.pb.hq.dto import Security_pb2 as hq_dot_dto_dot_Security__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hq/dto/TimeShare.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n2com.huasheng.quant.open.sdk.protobuf.hq.common.dtoB\016TimeShareProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16hq/dto/TimeShare.proto\x1a\x15hq/dto/Security.proto\"t\n\tTimeShare\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x16\n\x0elastClosePrice\x18\x03 \x01(\x01\x12\x10\n\x08\x61vgPrice\x18\x04 \x01(\x01\x12\x0e\n\x06volume\x18\x05 \x01(\x03\x12\x10\n\x08turnover\x18\x06 \x01(\x01\x42\x44\n2com.huasheng.quant.open.sdk.protobuf.hq.common.dtoB\x0eTimeShareProtob\x06proto3'
  ,
  dependencies=[hq_dot_dto_dot_Security__pb2.DESCRIPTOR,])




_TIMESHARE = _descriptor.Descriptor(
  name='TimeShare',
  full_name='TimeShare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='TimeShare.time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='TimeShare.price', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastClosePrice', full_name='TimeShare.lastClosePrice', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avgPrice', full_name='TimeShare.avgPrice', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='TimeShare.volume', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='turnover', full_name='TimeShare.turnover', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=49,
  serialized_end=165,
)

DESCRIPTOR.message_types_by_name['TimeShare'] = _TIMESHARE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeShare = _reflection.GeneratedProtocolMessageType('TimeShare', (_message.Message,), {
  'DESCRIPTOR' : _TIMESHARE,
  '__module__' : 'hq.dto.TimeShare_pb2'
  # @@protoc_insertion_point(class_scope:TimeShare)
  })
_sym_db.RegisterMessage(TimeShare)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)