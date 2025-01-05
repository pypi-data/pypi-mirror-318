"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'ibc/applications/transfer/v1/authz.proto')
_sym_db = _symbol_database.Default()
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ibc/applications/transfer/v1/authz.proto\x12\x1cibc.applications.transfer.v1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xff\x01\n\nAllocation\x12+\n\x0bsource_port\x18\x01 \x01(\tB\x16\xf2\xde\x1f\x12yaml:"source_port"\x121\n\x0esource_channel\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"source_channel"\x12`\n\x0bspend_limit\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x12\n\nallow_list\x18\x04 \x03(\t\x12\x1b\n\x13allowed_packet_data\x18\x05 \x03(\t"\x84\x01\n\x15TransferAuthorization\x12C\n\x0ballocations\x18\x01 \x03(\x0b2(.ibc.applications.transfer.v1.AllocationB\x04\xc8\xde\x1f\x00:&\xca\xb4-"cosmos.authz.v1beta1.AuthorizationB9Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.authz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
    _globals['_ALLOCATION'].fields_by_name['source_port']._loaded_options = None
    _globals['_ALLOCATION'].fields_by_name['source_port']._serialized_options = b'\xf2\xde\x1f\x12yaml:"source_port"'
    _globals['_ALLOCATION'].fields_by_name['source_channel']._loaded_options = None
    _globals['_ALLOCATION'].fields_by_name['source_channel']._serialized_options = b'\xf2\xde\x1f\x15yaml:"source_channel"'
    _globals['_ALLOCATION'].fields_by_name['spend_limit']._loaded_options = None
    _globals['_ALLOCATION'].fields_by_name['spend_limit']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_TRANSFERAUTHORIZATION'].fields_by_name['allocations']._loaded_options = None
    _globals['_TRANSFERAUTHORIZATION'].fields_by_name['allocations']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_TRANSFERAUTHORIZATION']._loaded_options = None
    _globals['_TRANSFERAUTHORIZATION']._serialized_options = b'\xca\xb4-"cosmos.authz.v1beta1.Authorization'
    _globals['_ALLOCATION']._serialized_start = 156
    _globals['_ALLOCATION']._serialized_end = 411
    _globals['_TRANSFERAUTHORIZATION']._serialized_start = 414
    _globals['_TRANSFERAUTHORIZATION']._serialized_end = 546