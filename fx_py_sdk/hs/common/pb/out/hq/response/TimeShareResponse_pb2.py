# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hq/response/TimeShareResponse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hq.dto import Security_pb2 as hq_dot_dto_dot_Security__pb2
from hq.dto import TimeShare_pb2 as hq_dot_dto_dot_TimeShare__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hq/response/TimeShareResponse.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n0com.huasheng.quant.open.sdk.protobuf.hq.responseB\026TimeShareResponseProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#hq/response/TimeShareResponse.proto\x1a\x15hq/dto/Security.proto\x1a\x16hq/dto/TimeShare.proto\"O\n\x11TimeShareResponse\x12\x1b\n\x08security\x18\x01 \x01(\x0b\x32\t.Security\x12\x1d\n\ttimeShare\x18\x02 \x03(\x0b\x32\n.TimeShareBJ\n0com.huasheng.quant.open.sdk.protobuf.hq.responseB\x16TimeShareResponseProtob\x06proto3'
  ,
  dependencies=[hq_dot_dto_dot_Security__pb2.DESCRIPTOR,hq_dot_dto_dot_TimeShare__pb2.DESCRIPTOR,])




_TIMESHARERESPONSE = _descriptor.Descriptor(
  name='TimeShareResponse',
  full_name='TimeShareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='TimeShareResponse.security', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeShare', full_name='TimeShareResponse.timeShare', index=1,
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
  serialized_start=86,
  serialized_end=165,
)

_TIMESHARERESPONSE.fields_by_name['security'].message_type = hq_dot_dto_dot_Security__pb2._SECURITY
_TIMESHARERESPONSE.fields_by_name['timeShare'].message_type = hq_dot_dto_dot_TimeShare__pb2._TIMESHARE
DESCRIPTOR.message_types_by_name['TimeShareResponse'] = _TIMESHARERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeShareResponse = _reflection.GeneratedProtocolMessageType('TimeShareResponse', (_message.Message,), {
  'DESCRIPTOR' : _TIMESHARERESPONSE,
  '__module__' : 'hq.response.TimeShareResponse_pb2'
  # @@protoc_insertion_point(class_scope:TimeShareResponse)
  })
_sym_db.RegisterMessage(TimeShareResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)