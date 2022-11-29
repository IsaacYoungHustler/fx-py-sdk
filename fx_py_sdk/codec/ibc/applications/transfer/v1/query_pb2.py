# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from fx_py_sdk.codec.ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from fx_py_sdk.codec.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/applications/transfer/v1/query.proto',
  package='ibc.applications.transfer.v1',
  syntax='proto3',
  serialized_options=b'Z>github.com/cosmos/cosmos-sdk/x/ibc/applications/transfer/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(ibc/applications/transfer/v1/query.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x1cgoogle/api/annotations.proto\"&\n\x16QueryDenomTraceRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"X\n\x17QueryDenomTraceResponse\x12=\n\x0b\x64\x65nom_trace\x18\x01 \x01(\x0b\x32(.ibc.applications.transfer.v1.DenomTrace\"U\n\x17QueryDenomTracesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa7\x01\n\x18QueryDenomTracesResponse\x12N\n\x0c\x64\x65nom_traces\x18\x01 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB\x0e\xaa\xdf\x1f\x06Traces\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x14\n\x12QueryParamsRequest\"K\n\x13QueryParamsResponse\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32$.ibc.applications.transfer.v1.Params2\x9e\x04\n\x05Query\x12\xb9\x01\n\nDenomTrace\x12\x34.ibc.applications.transfer.v1.QueryDenomTraceRequest\x1a\x35.ibc.applications.transfer.v1.QueryDenomTraceResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/ibc/applications/transfer/v1beta1/denom_traces/{hash}\x12\xb5\x01\n\x0b\x44\x65nomTraces\x12\x35.ibc.applications.transfer.v1.QueryDenomTracesRequest\x1a\x36.ibc.applications.transfer.v1.QueryDenomTracesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//ibc/applications/transfer/v1beta1/denom_traces\x12\xa0\x01\n\x06Params\x12\x30.ibc.applications.transfer.v1.QueryParamsRequest\x1a\x31.ibc.applications.transfer.v1.QueryParamsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/ibc/applications/transfer/v1beta1/paramsB@Z>github.com/cosmos/cosmos-sdk/x/ibc/applications/transfer/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_QUERYDENOMTRACEREQUEST = _descriptor.Descriptor(
  name='QueryDenomTraceRequest',
  full_name='ibc.applications.transfer.v1.QueryDenomTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ibc.applications.transfer.v1.QueryDenomTraceRequest.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=215,
  serialized_end=253,
)


_QUERYDENOMTRACERESPONSE = _descriptor.Descriptor(
  name='QueryDenomTraceResponse',
  full_name='ibc.applications.transfer.v1.QueryDenomTraceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom_trace', full_name='ibc.applications.transfer.v1.QueryDenomTraceResponse.denom_trace', index=0,
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
  serialized_start=255,
  serialized_end=343,
)


_QUERYDENOMTRACESREQUEST = _descriptor.Descriptor(
  name='QueryDenomTracesRequest',
  full_name='ibc.applications.transfer.v1.QueryDenomTracesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ibc.applications.transfer.v1.QueryDenomTracesRequest.pagination', index=0,
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
  serialized_start=345,
  serialized_end=430,
)


_QUERYDENOMTRACESRESPONSE = _descriptor.Descriptor(
  name='QueryDenomTracesResponse',
  full_name='ibc.applications.transfer.v1.QueryDenomTracesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom_traces', full_name='ibc.applications.transfer.v1.QueryDenomTracesResponse.denom_traces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037\006Traces\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ibc.applications.transfer.v1.QueryDenomTracesResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=433,
  serialized_end=600,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='ibc.applications.transfer.v1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=602,
  serialized_end=622,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='ibc.applications.transfer.v1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='ibc.applications.transfer.v1.QueryParamsResponse.params', index=0,
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
  serialized_start=624,
  serialized_end=699,
)

_QUERYDENOMTRACERESPONSE.fields_by_name['denom_trace'].message_type = ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2._DENOMTRACE
_QUERYDENOMTRACESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYDENOMTRACESRESPONSE.fields_by_name['denom_traces'].message_type = ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2._DENOMTRACE
_QUERYDENOMTRACESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryDenomTraceRequest'] = _QUERYDENOMTRACEREQUEST
DESCRIPTOR.message_types_by_name['QueryDenomTraceResponse'] = _QUERYDENOMTRACERESPONSE
DESCRIPTOR.message_types_by_name['QueryDenomTracesRequest'] = _QUERYDENOMTRACESREQUEST
DESCRIPTOR.message_types_by_name['QueryDenomTracesResponse'] = _QUERYDENOMTRACESRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryDenomTraceRequest = _reflection.GeneratedProtocolMessageType('QueryDenomTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACEREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTraceRequest)
  })
_sym_db.RegisterMessage(QueryDenomTraceRequest)

QueryDenomTraceResponse = _reflection.GeneratedProtocolMessageType('QueryDenomTraceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACERESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTraceResponse)
  })
_sym_db.RegisterMessage(QueryDenomTraceResponse)

QueryDenomTracesRequest = _reflection.GeneratedProtocolMessageType('QueryDenomTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACESREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTracesRequest)
  })
_sym_db.RegisterMessage(QueryDenomTracesRequest)

QueryDenomTracesResponse = _reflection.GeneratedProtocolMessageType('QueryDenomTracesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACESRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTracesResponse)
  })
_sym_db.RegisterMessage(QueryDenomTracesResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR._options = None
_QUERYDENOMTRACESRESPONSE.fields_by_name['denom_traces']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='ibc.applications.transfer.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=702,
  serialized_end=1244,
  methods=[
  _descriptor.MethodDescriptor(
    name='DenomTrace',
    full_name='ibc.applications.transfer.v1.Query.DenomTrace',
    index=0,
    containing_service=None,
    input_type=_QUERYDENOMTRACEREQUEST,
    output_type=_QUERYDENOMTRACERESPONSE,
    serialized_options=b'\202\323\344\223\0028\0226/ibc/applications/transfer/v1beta1/denom_traces/{hash}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DenomTraces',
    full_name='ibc.applications.transfer.v1.Query.DenomTraces',
    index=1,
    containing_service=None,
    input_type=_QUERYDENOMTRACESREQUEST,
    output_type=_QUERYDENOMTRACESRESPONSE,
    serialized_options=b'\202\323\344\223\0021\022//ibc/applications/transfer/v1beta1/denom_traces',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='ibc.applications.transfer.v1.Query.Params',
    index=2,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/ibc/applications/transfer/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
