"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'ibc/lightclients/localhost/v2/localhost.proto')
_sym_db = _symbol_database.Default()
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-ibc/lightclients/localhost/v2/localhost.proto\x12\x1dibc.lightclients.localhost.v2\x1a\x1fibc/core/client/v1/client.proto\x1a\x14gogoproto/gogo.proto"L\n\x0bClientState\x127\n\rlatest_height\x18\x01 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00BJZHgithub.com/cosmos/ibc-go/v7/modules/light-clients/09-localhost;localhostb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.localhost.v2.localhost_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZHgithub.com/cosmos/ibc-go/v7/modules/light-clients/09-localhost;localhost'
    _globals['_CLIENTSTATE'].fields_by_name['latest_height']._loaded_options = None
    _globals['_CLIENTSTATE'].fields_by_name['latest_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_CLIENTSTATE']._loaded_options = None
    _globals['_CLIENTSTATE']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_CLIENTSTATE']._serialized_start = 135
    _globals['_CLIENTSTATE']._serialized_end = 211