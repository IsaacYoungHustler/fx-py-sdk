# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from fx_py_sdk.codec.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from fx_py_sdk.codec.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/core/client/v1/query.proto',
  package='ibc.core.client.v1',
  syntax='proto3',
  serialized_options=b'Z7github.com/cosmos/cosmos-sdk/x/ibc/core/02-client/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eibc/core/client/v1/query.proto\x12\x12ibc.core.client.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\",\n\x17QueryClientStateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x8d\x01\n\x18QueryClientStateResponse\x12*\n\x0c\x63lient_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"V\n\x18QueryClientStatesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xba\x01\n\x19QueryClientStatesResponse\x12`\n\rclient_states\x18\x01 \x03(\x0b\x32).ibc.core.client.v1.IdentifiedClientStateB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"x\n\x1aQueryConsensusStateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x17\n\x0frevision_number\x18\x02 \x01(\x04\x12\x17\n\x0frevision_height\x18\x03 \x01(\x04\x12\x15\n\rlatest_height\x18\x04 \x01(\x08\"\x93\x01\n\x1bQueryConsensusStateResponse\x12-\n\x0f\x63onsensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"l\n\x1bQueryConsensusStatesRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa9\x01\n\x1cQueryConsensusStatesResponse\x12L\n\x10\x63onsensus_states\x18\x01 \x03(\x0b\x32,.ibc.core.client.v1.ConsensusStateWithHeightB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1a\n\x18QueryClientParamsRequest\"G\n\x19QueryClientParamsResponse\x12*\n\x06params\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.Params2\xfb\x06\n\x05Query\x12\xa4\x01\n\x0b\x43lientState\x12+.ibc.core.client.v1.QueryClientStateRequest\x1a,.ibc.core.client.v1.QueryClientStateResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/ibc/core/client/v1beta1/client_states/{client_id}\x12\x9b\x01\n\x0c\x43lientStates\x12,.ibc.core.client.v1.QueryClientStatesRequest\x1a-.ibc.core.client.v1.QueryClientStatesResponse\".\x82\xd3\xe4\x93\x02(\x12&/ibc/core/client/v1beta1/client_states\x12\xe4\x01\n\x0e\x43onsensusState\x12..ibc.core.client.v1.QueryConsensusStateRequest\x1a/.ibc.core.client.v1.QueryConsensusStateResponse\"q\x82\xd3\xe4\x93\x02k\x12i/ibc/core/client/v1beta1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}\x12\xb3\x01\n\x0f\x43onsensusStates\x12/.ibc.core.client.v1.QueryConsensusStatesRequest\x1a\x30.ibc.core.client.v1.QueryConsensusStatesResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/ibc/core/client/v1beta1/consensus_states/{client_id}\x12\x8f\x01\n\x0c\x43lientParams\x12,.ibc.core.client.v1.QueryClientParamsRequest\x1a-.ibc.core.client.v1.QueryClientParamsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/ibc/client/v1beta1/paramsB9Z7github.com/cosmos/cosmos-sdk/x/ibc/core/02-client/typesb\x06proto3'
  ,
  dependencies=[cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_QUERYCLIENTSTATEREQUEST = _descriptor.Descriptor(
  name='QueryClientStateRequest',
  full_name='ibc.core.client.v1.QueryClientStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.client.v1.QueryClientStateRequest.client_id', index=0,
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
  serialized_start=210,
  serialized_end=254,
)


_QUERYCLIENTSTATERESPONSE = _descriptor.Descriptor(
  name='QueryClientStateResponse',
  full_name='ibc.core.client.v1.QueryClientStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_state', full_name='ibc.core.client.v1.QueryClientStateResponse.client_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof', full_name='ibc.core.client.v1.QueryClientStateResponse.proof', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_height', full_name='ibc.core.client.v1.QueryClientStateResponse.proof_height', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=257,
  serialized_end=398,
)


_QUERYCLIENTSTATESREQUEST = _descriptor.Descriptor(
  name='QueryClientStatesRequest',
  full_name='ibc.core.client.v1.QueryClientStatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ibc.core.client.v1.QueryClientStatesRequest.pagination', index=0,
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
  serialized_start=400,
  serialized_end=486,
)


_QUERYCLIENTSTATESRESPONSE = _descriptor.Descriptor(
  name='QueryClientStatesResponse',
  full_name='ibc.core.client.v1.QueryClientStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_states', full_name='ibc.core.client.v1.QueryClientStatesResponse.client_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037\026IdentifiedClientStates', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ibc.core.client.v1.QueryClientStatesResponse.pagination', index=1,
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
  serialized_start=489,
  serialized_end=675,
)


_QUERYCONSENSUSSTATEREQUEST = _descriptor.Descriptor(
  name='QueryConsensusStateRequest',
  full_name='ibc.core.client.v1.QueryConsensusStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.client.v1.QueryConsensusStateRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_number', full_name='ibc.core.client.v1.QueryConsensusStateRequest.revision_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_height', full_name='ibc.core.client.v1.QueryConsensusStateRequest.revision_height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_height', full_name='ibc.core.client.v1.QueryConsensusStateRequest.latest_height', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=677,
  serialized_end=797,
)


_QUERYCONSENSUSSTATERESPONSE = _descriptor.Descriptor(
  name='QueryConsensusStateResponse',
  full_name='ibc.core.client.v1.QueryConsensusStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='consensus_state', full_name='ibc.core.client.v1.QueryConsensusStateResponse.consensus_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof', full_name='ibc.core.client.v1.QueryConsensusStateResponse.proof', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proof_height', full_name='ibc.core.client.v1.QueryConsensusStateResponse.proof_height', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=800,
  serialized_end=947,
)


_QUERYCONSENSUSSTATESREQUEST = _descriptor.Descriptor(
  name='QueryConsensusStatesRequest',
  full_name='ibc.core.client.v1.QueryConsensusStatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.client.v1.QueryConsensusStatesRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ibc.core.client.v1.QueryConsensusStatesRequest.pagination', index=1,
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
  serialized_start=949,
  serialized_end=1057,
)


_QUERYCONSENSUSSTATESRESPONSE = _descriptor.Descriptor(
  name='QueryConsensusStatesResponse',
  full_name='ibc.core.client.v1.QueryConsensusStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='consensus_states', full_name='ibc.core.client.v1.QueryConsensusStatesResponse.consensus_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ibc.core.client.v1.QueryConsensusStatesResponse.pagination', index=1,
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
  serialized_start=1060,
  serialized_end=1229,
)


_QUERYCLIENTPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryClientParamsRequest',
  full_name='ibc.core.client.v1.QueryClientParamsRequest',
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
  serialized_start=1231,
  serialized_end=1257,
)


_QUERYCLIENTPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryClientParamsResponse',
  full_name='ibc.core.client.v1.QueryClientParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='ibc.core.client.v1.QueryClientParamsResponse.params', index=0,
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
  serialized_start=1259,
  serialized_end=1330,
)

_QUERYCLIENTSTATERESPONSE.fields_by_name['client_state'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_QUERYCLIENTSTATERESPONSE.fields_by_name['proof_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_QUERYCLIENTSTATESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYCLIENTSTATESRESPONSE.fields_by_name['client_states'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._IDENTIFIEDCLIENTSTATE
_QUERYCLIENTSTATESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYCONSENSUSSTATERESPONSE.fields_by_name['consensus_state'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_QUERYCONSENSUSSTATERESPONSE.fields_by_name['proof_height'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._HEIGHT
_QUERYCONSENSUSSTATESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYCONSENSUSSTATESRESPONSE.fields_by_name['consensus_states'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._CONSENSUSSTATEWITHHEIGHT
_QUERYCONSENSUSSTATESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYCLIENTPARAMSRESPONSE.fields_by_name['params'].message_type = ibc_dot_core_dot_client_dot_v1_dot_client__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryClientStateRequest'] = _QUERYCLIENTSTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryClientStateResponse'] = _QUERYCLIENTSTATERESPONSE
DESCRIPTOR.message_types_by_name['QueryClientStatesRequest'] = _QUERYCLIENTSTATESREQUEST
DESCRIPTOR.message_types_by_name['QueryClientStatesResponse'] = _QUERYCLIENTSTATESRESPONSE
DESCRIPTOR.message_types_by_name['QueryConsensusStateRequest'] = _QUERYCONSENSUSSTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryConsensusStateResponse'] = _QUERYCONSENSUSSTATERESPONSE
DESCRIPTOR.message_types_by_name['QueryConsensusStatesRequest'] = _QUERYCONSENSUSSTATESREQUEST
DESCRIPTOR.message_types_by_name['QueryConsensusStatesResponse'] = _QUERYCONSENSUSSTATESRESPONSE
DESCRIPTOR.message_types_by_name['QueryClientParamsRequest'] = _QUERYCLIENTPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryClientParamsResponse'] = _QUERYCLIENTPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryClientStateRequest = _reflection.GeneratedProtocolMessageType('QueryClientStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATEREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStateRequest)
  })
_sym_db.RegisterMessage(QueryClientStateRequest)

QueryClientStateResponse = _reflection.GeneratedProtocolMessageType('QueryClientStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATERESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStateResponse)
  })
_sym_db.RegisterMessage(QueryClientStateResponse)

QueryClientStatesRequest = _reflection.GeneratedProtocolMessageType('QueryClientStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATESREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStatesRequest)
  })
_sym_db.RegisterMessage(QueryClientStatesRequest)

QueryClientStatesResponse = _reflection.GeneratedProtocolMessageType('QueryClientStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTSTATESRESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientStatesResponse)
  })
_sym_db.RegisterMessage(QueryClientStatesResponse)

QueryConsensusStateRequest = _reflection.GeneratedProtocolMessageType('QueryConsensusStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATEREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStateRequest)
  })
_sym_db.RegisterMessage(QueryConsensusStateRequest)

QueryConsensusStateResponse = _reflection.GeneratedProtocolMessageType('QueryConsensusStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATERESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStateResponse)
  })
_sym_db.RegisterMessage(QueryConsensusStateResponse)

QueryConsensusStatesRequest = _reflection.GeneratedProtocolMessageType('QueryConsensusStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATESREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStatesRequest)
  })
_sym_db.RegisterMessage(QueryConsensusStatesRequest)

QueryConsensusStatesResponse = _reflection.GeneratedProtocolMessageType('QueryConsensusStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONSENSUSSTATESRESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryConsensusStatesResponse)
  })
_sym_db.RegisterMessage(QueryConsensusStatesResponse)

QueryClientParamsRequest = _reflection.GeneratedProtocolMessageType('QueryClientParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTPARAMSREQUEST,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientParamsRequest)
  })
_sym_db.RegisterMessage(QueryClientParamsRequest)

QueryClientParamsResponse = _reflection.GeneratedProtocolMessageType('QueryClientParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLIENTPARAMSRESPONSE,
  '__module__' : 'ibc.core.client.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.client.v1.QueryClientParamsResponse)
  })
_sym_db.RegisterMessage(QueryClientParamsResponse)


DESCRIPTOR._options = None
_QUERYCLIENTSTATERESPONSE.fields_by_name['proof_height']._options = None
_QUERYCLIENTSTATESRESPONSE.fields_by_name['client_states']._options = None
_QUERYCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._options = None
_QUERYCONSENSUSSTATESRESPONSE.fields_by_name['consensus_states']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='ibc.core.client.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1333,
  serialized_end=2224,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClientState',
    full_name='ibc.core.client.v1.Query.ClientState',
    index=0,
    containing_service=None,
    input_type=_QUERYCLIENTSTATEREQUEST,
    output_type=_QUERYCLIENTSTATERESPONSE,
    serialized_options=b'\202\323\344\223\0024\0222/ibc/core/client/v1beta1/client_states/{client_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClientStates',
    full_name='ibc.core.client.v1.Query.ClientStates',
    index=1,
    containing_service=None,
    input_type=_QUERYCLIENTSTATESREQUEST,
    output_type=_QUERYCLIENTSTATESRESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/ibc/core/client/v1beta1/client_states',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConsensusState',
    full_name='ibc.core.client.v1.Query.ConsensusState',
    index=2,
    containing_service=None,
    input_type=_QUERYCONSENSUSSTATEREQUEST,
    output_type=_QUERYCONSENSUSSTATERESPONSE,
    serialized_options=b'\202\323\344\223\002k\022i/ibc/core/client/v1beta1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConsensusStates',
    full_name='ibc.core.client.v1.Query.ConsensusStates',
    index=3,
    containing_service=None,
    input_type=_QUERYCONSENSUSSTATESREQUEST,
    output_type=_QUERYCONSENSUSSTATESRESPONSE,
    serialized_options=b'\202\323\344\223\0027\0225/ibc/core/client/v1beta1/consensus_states/{client_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClientParams',
    full_name='ibc.core.client.v1.Query.ClientParams',
    index=4,
    containing_service=None,
    input_type=_QUERYCLIENTPARAMSREQUEST,
    output_type=_QUERYCLIENTPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\034\022\032/ibc/client/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)