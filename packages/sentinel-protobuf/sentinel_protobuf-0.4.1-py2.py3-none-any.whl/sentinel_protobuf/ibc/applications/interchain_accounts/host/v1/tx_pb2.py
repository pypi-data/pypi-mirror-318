"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'ibc/applications/interchain_accounts/host/v1/tx.proto')
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ......cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ......ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ibc/applications/interchain_accounts/host/v1/tx.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a7ibc/applications/interchain_accounts/host/v1/host.proto"\x83\x01\n\x12MsgModuleQuerySafe\x12\x0e\n\x06signer\x18\x01 \x01(\t\x12L\n\x08requests\x18\x02 \x03(\x0b2:.ibc.applications.interchain_accounts.host.v1.QueryRequest:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer"?\n\x1aMsgModuleQuerySafeResponse\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x11\n\tresponses\x18\x02 \x03(\x0c2\xac\x01\n\x03Msg\x12\x9d\x01\n\x0fModuleQuerySafe\x12@.ibc.applications.interchain_accounts.host.v1.MsgModuleQuerySafe\x1aH.ibc.applications.interchain_accounts.host.v1.MsgModuleQuerySafeResponse\x1a\x05\x80\xe7\xb0*\x01BLZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/types'
    _globals['_MSGMODULEQUERYSAFE']._loaded_options = None
    _globals['_MSGMODULEQUERYSAFE']._serialized_options = b'\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer'
    _globals['_MSG']._loaded_options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGMODULEQUERYSAFE']._serialized_start = 208
    _globals['_MSGMODULEQUERYSAFE']._serialized_end = 339
    _globals['_MSGMODULEQUERYSAFERESPONSE']._serialized_start = 341
    _globals['_MSGMODULEQUERYSAFERESPONSE']._serialized_end = 404
    _globals['_MSG']._serialized_start = 407
    _globals['_MSG']._serialized_end = 579