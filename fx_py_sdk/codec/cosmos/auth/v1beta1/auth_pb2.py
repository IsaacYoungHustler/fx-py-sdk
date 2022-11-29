# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/auth/v1beta1/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/auth/v1beta1/auth.proto',
  package='cosmos.auth.v1beta1',
  syntax='proto3',
  serialized_options=b'Z)github.com/cosmos/cosmos-sdk/x/auth/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63osmos/auth/v1beta1/auth.proto\x12\x13\x63osmos.auth.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"\xd3\x01\n\x0b\x42\x61seAccount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12T\n\x07pub_key\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB-\xea\xde\x1f\x14public_key,omitempty\xf2\xde\x1f\x11yaml:\"public_key\"\x12\x31\n\x0e\x61\x63\x63ount_number\x18\x03 \x01(\x04\x42\x19\xf2\xde\x1f\x15yaml:\"account_number\"\x12\x10\n\x08sequence\x18\x04 \x01(\x04:\x18\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xd2\xb4-\x08\x41\x63\x63ountI\"\xa3\x01\n\rModuleAccount\x12S\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x1b\xd0\xde\x1f\x01\xf2\xde\x1f\x13yaml:\"base_account\"\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t:\x1a\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xd2\xb4-\x0eModuleAccountI\"\xff\x02\n\x06Params\x12;\n\x13max_memo_characters\x18\x01 \x01(\x04\x42\x1e\xf2\xde\x1f\x1ayaml:\"max_memo_characters\"\x12-\n\x0ctx_sig_limit\x18\x02 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"tx_sig_limit\"\x12?\n\x15tx_size_cost_per_byte\x18\x03 \x01(\x04\x42 \xf2\xde\x1f\x1cyaml:\"tx_size_cost_per_byte\"\x12[\n\x17sig_verify_cost_ed25519\x18\x04 \x01(\x04\x42:\xe2\xde\x1f\x14SigVerifyCostED25519\xf2\xde\x1f\x1eyaml:\"sig_verify_cost_ed25519\"\x12\x61\n\x19sig_verify_cost_secp256k1\x18\x05 \x01(\x04\x42>\xe2\xde\x1f\x16SigVerifyCostSecp256k1\xf2\xde\x1f yaml:\"sig_verify_cost_secp256k1\":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\x42+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3'
  ,
  dependencies=[cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_BASEACCOUNT = _descriptor.Descriptor(
  name='BaseAccount',
  full_name='cosmos.auth.v1beta1.BaseAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.auth.v1beta1.BaseAccount.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='cosmos.auth.v1beta1.BaseAccount.pub_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\352\336\037\024public_key,omitempty\362\336\037\021yaml:\"public_key\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_number', full_name='cosmos.auth.v1beta1.BaseAccount.account_number', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\025yaml:\"account_number\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='cosmos.auth.v1beta1.BaseAccount.sequence', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_options=b'\210\240\037\000\230\240\037\000\350\240\037\000\322\264-\010AccountI',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=343,
)


_MODULEACCOUNT = _descriptor.Descriptor(
  name='ModuleAccount',
  full_name='cosmos.auth.v1beta1.ModuleAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_account', full_name='cosmos.auth.v1beta1.ModuleAccount.base_account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\320\336\037\001\362\336\037\023yaml:\"base_account\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cosmos.auth.v1beta1.ModuleAccount.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cosmos.auth.v1beta1.ModuleAccount.permissions', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_options=b'\210\240\037\000\230\240\037\000\322\264-\016ModuleAccountI',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=509,
)


_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='cosmos.auth.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_memo_characters', full_name='cosmos.auth.v1beta1.Params.max_memo_characters', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\032yaml:\"max_memo_characters\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_sig_limit', full_name='cosmos.auth.v1beta1.Params.tx_sig_limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"tx_sig_limit\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_size_cost_per_byte', full_name='cosmos.auth.v1beta1.Params.tx_size_cost_per_byte', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"tx_size_cost_per_byte\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sig_verify_cost_ed25519', full_name='cosmos.auth.v1beta1.Params.sig_verify_cost_ed25519', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\024SigVerifyCostED25519\362\336\037\036yaml:\"sig_verify_cost_ed25519\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sig_verify_cost_secp256k1', full_name='cosmos.auth.v1beta1.Params.sig_verify_cost_secp256k1', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\026SigVerifyCostSecp256k1\362\336\037 yaml:\"sig_verify_cost_secp256k1\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=895,
)

_BASEACCOUNT.fields_by_name['pub_key'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MODULEACCOUNT.fields_by_name['base_account'].message_type = _BASEACCOUNT
DESCRIPTOR.message_types_by_name['BaseAccount'] = _BASEACCOUNT
DESCRIPTOR.message_types_by_name['ModuleAccount'] = _MODULEACCOUNT
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BaseAccount = _reflection.GeneratedProtocolMessageType('BaseAccount', (_message.Message,), {
  'DESCRIPTOR' : _BASEACCOUNT,
  '__module__' : 'cosmos.auth.v1beta1.auth_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.BaseAccount)
  })
_sym_db.RegisterMessage(BaseAccount)

ModuleAccount = _reflection.GeneratedProtocolMessageType('ModuleAccount', (_message.Message,), {
  'DESCRIPTOR' : _MODULEACCOUNT,
  '__module__' : 'cosmos.auth.v1beta1.auth_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.ModuleAccount)
  })
_sym_db.RegisterMessage(ModuleAccount)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmos.auth.v1beta1.auth_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.auth.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_BASEACCOUNT.fields_by_name['pub_key']._options = None
_BASEACCOUNT.fields_by_name['account_number']._options = None
_BASEACCOUNT._options = None
_MODULEACCOUNT.fields_by_name['base_account']._options = None
_MODULEACCOUNT._options = None
_PARAMS.fields_by_name['max_memo_characters']._options = None
_PARAMS.fields_by_name['tx_sig_limit']._options = None
_PARAMS.fields_by_name['tx_size_cost_per_byte']._options = None
_PARAMS.fields_by_name['sig_verify_cost_ed25519']._options = None
_PARAMS.fields_by_name['sig_verify_cost_secp256k1']._options = None
_PARAMS._options = None
# @@protoc_insertion_point(module_scope)
