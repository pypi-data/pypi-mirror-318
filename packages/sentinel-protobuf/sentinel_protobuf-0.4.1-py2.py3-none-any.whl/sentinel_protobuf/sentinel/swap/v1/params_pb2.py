"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/swap/v1/params.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/swap/v1/params.proto\x12\x10sentinel.swap.v1\x1a\x14gogoproto/gogo.proto"F\n\x06Params\x12\x14\n\x0cswap_enabled\x18\x01 \x01(\x08\x12\x12\n\nswap_denom\x18\x02 \x01(\t\x12\x12\n\napprove_by\x18\x03 \x01(\tB>Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.swap.v1.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_PARAMS']._serialized_start = 73
    _globals['_PARAMS']._serialized_end = 143