"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v2/allocation.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)sentinel/subscription/v2/allocation.proto\x12\x18sentinel.subscription.v2\x1a\x14gogoproto/gogo.proto"\x9e\x01\n\nAllocation\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x0f\n\x07address\x18\x02 \x01(\t\x124\n\rgranted_bytes\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x125\n\x0eutilised_bytes\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.IntBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v2.allocation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_ALLOCATION'].fields_by_name['id']._loaded_options = None
    _globals['_ALLOCATION'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_ALLOCATION'].fields_by_name['granted_bytes']._loaded_options = None
    _globals['_ALLOCATION'].fields_by_name['granted_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_ALLOCATION'].fields_by_name['utilised_bytes']._loaded_options = None
    _globals['_ALLOCATION'].fields_by_name['utilised_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_ALLOCATION']._serialized_start = 94
    _globals['_ALLOCATION']._serialized_end = 252