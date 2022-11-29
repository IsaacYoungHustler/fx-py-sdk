# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/v1/params.proto',
  package='fx.dex.v1',
  syntax='proto3',
  serialized_options=b'Z(github.com/marginxio/marginx/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x66x/dex/v1/params.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xbf\x02\n\x06Params\x12@\n\x08\x66\x65\x65_rate\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12/\n\'force_liquidation_margin_rate_threshold\x18\x02 \x01(\x03\x12\x1b\n\x13order_expire_blocks\x18\x03 \x01(\x03\x12\x1b\n\x13max_deals_per_block\x18\x04 \x01(\x03\x12\x1e\n\x16max_orders_per_account\x18\x05 \x01(\x03\x12\x1e\n\x16permitted_max_leverage\x18\x06 \x01(\x03\x12H\n\x10lock_coin_factor\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xac\x03\n\x07Reserve\x12\x65\n\x10\x61\x63\x63umulative_fee\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\x12\x44\n\x0crisk_reserve\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x61\n\x0clocked_funds\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\x12H\n\x10short_pay_margin\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12G\n\x0flong_pay_margin\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42*Z(github.com/marginxio/marginx/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='fx.dex.v1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fee_rate', full_name='fx.dex.v1.Params.fee_rate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force_liquidation_margin_rate_threshold', full_name='fx.dex.v1.Params.force_liquidation_margin_rate_threshold', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_expire_blocks', full_name='fx.dex.v1.Params.order_expire_blocks', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_deals_per_block', full_name='fx.dex.v1.Params.max_deals_per_block', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_orders_per_account', full_name='fx.dex.v1.Params.max_orders_per_account', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permitted_max_leverage', full_name='fx.dex.v1.Params.permitted_max_leverage', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lock_coin_factor', full_name='fx.dex.v1.Params.lock_coin_factor', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=411,
)


_RESERVE = _descriptor.Descriptor(
  name='Reserve',
  full_name='fx.dex.v1.Reserve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accumulative_fee', full_name='fx.dex.v1.Reserve.accumulative_fee', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='risk_reserve', full_name='fx.dex.v1.Reserve.risk_reserve', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locked_funds', full_name='fx.dex.v1.Reserve.locked_funds', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='short_pay_margin', full_name='fx.dex.v1.Reserve.short_pay_margin', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='long_pay_margin', full_name='fx.dex.v1.Reserve.long_pay_margin', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=414,
  serialized_end=842,
)

_RESERVE.fields_by_name['accumulative_fee'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_RESERVE.fields_by_name['locked_funds'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['Reserve'] = _RESERVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'fx.dex.v1.params_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Params)
  })
_sym_db.RegisterMessage(Params)

Reserve = _reflection.GeneratedProtocolMessageType('Reserve', (_message.Message,), {
  'DESCRIPTOR' : _RESERVE,
  '__module__' : 'fx.dex.v1.params_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Reserve)
  })
_sym_db.RegisterMessage(Reserve)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['fee_rate']._options = None
_PARAMS.fields_by_name['lock_coin_factor']._options = None
_RESERVE.fields_by_name['accumulative_fee']._options = None
_RESERVE.fields_by_name['risk_reserve']._options = None
_RESERVE.fields_by_name['locked_funds']._options = None
_RESERVE.fields_by_name['short_pay_margin']._options = None
_RESERVE.fields_by_name['long_pay_margin']._options = None
# @@protoc_insertion_point(module_scope)
