# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade/request/TradeQueryBeforeAndAfterSupportRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trade/request/TradeQueryBeforeAndAfterSupportRequest.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n:trade/request/TradeQueryBeforeAndAfterSupportRequest.proto\"Q\n&TradeQueryBeforeAndAfterSupportRequest\x12\x11\n\tstockCode\x18\x01 \x01(\t\x12\x14\n\x0c\x65xchangeType\x18\x02 \x01(\tBa\n2com.huasheng.quant.open.sdk.protobuf.trade.requestB+TradeQueryBeforeAndAfterSupportRequestProtob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRADEQUERYBEFOREANDAFTERSUPPORTREQUEST = _descriptor.Descriptor(
  name='TradeQueryBeforeAndAfterSupportRequest',
  full_name='TradeQueryBeforeAndAfterSupportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stockCode', full_name='TradeQueryBeforeAndAfterSupportRequest.stockCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchangeType', full_name='TradeQueryBeforeAndAfterSupportRequest.exchangeType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['TradeQueryBeforeAndAfterSupportRequest'] = _TRADEQUERYBEFOREANDAFTERSUPPORTREQUEST

TradeQueryBeforeAndAfterSupportRequest = _reflection.GeneratedProtocolMessageType('TradeQueryBeforeAndAfterSupportRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRADEQUERYBEFOREANDAFTERSUPPORTREQUEST,
  __module__ = 'trade.request.TradeQueryBeforeAndAfterSupportRequest_pb2'
  # @@protoc_insertion_point(class_scope:TradeQueryBeforeAndAfterSupportRequest)
  ))
_sym_db.RegisterMessage(TradeQueryBeforeAndAfterSupportRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n2com.huasheng.quant.open.sdk.protobuf.trade.requestB+TradeQueryBeforeAndAfterSupportRequestProto'))
# @@protoc_insertion_point(module_scope)