"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v3/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.node.v3 import node_pb2 as sentinel_dot_node_dot_v3_dot_node__pb2
from ....sentinel.node.v3 import params_pb2 as sentinel_dot_node_dot_v3_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/node/v3/genesis.proto\x12\x10sentinel.node.v3\x1a\x14gogoproto/gogo.proto\x1a\x1bsentinel/node/v3/node.proto\x1a\x1dsentinel/node/v3/params.proto"k\n\x0cGenesisState\x12+\n\x05nodes\x18\x01 \x03(\x0b2\x16.sentinel.node.v3.NodeB\x04\xc8\xde\x1f\x00\x12.\n\x06params\x18\x03 \x01(\x0b2\x18.sentinel.node.v3.ParamsB\x04\xc8\xde\x1f\x00B>Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSTATE'].fields_by_name['nodes']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['nodes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 134
    _globals['_GENESISSTATE']._serialized_end = 241