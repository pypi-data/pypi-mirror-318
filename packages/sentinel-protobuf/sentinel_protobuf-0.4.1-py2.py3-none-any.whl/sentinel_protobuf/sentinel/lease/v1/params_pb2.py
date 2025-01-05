"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/lease/v1/params.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/lease/v1/params.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto"v\n\x06Params\x12\x17\n\x0fmax_lease_hours\x18\x01 \x01(\x03\x12\x17\n\x0fmin_lease_hours\x18\x02 \x01(\x03\x12:\n\rstaking_share\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDecB?Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_PARAMS'].fields_by_name['staking_share']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['staking_share']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec'
    _globals['_PARAMS']._serialized_start = 75
    _globals['_PARAMS']._serialized_end = 193