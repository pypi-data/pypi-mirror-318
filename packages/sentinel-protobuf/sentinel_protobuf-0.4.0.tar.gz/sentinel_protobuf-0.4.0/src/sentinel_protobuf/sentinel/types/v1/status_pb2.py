
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n\x1esentinel/types/v1/status.proto\x12\x11sentinel.types.v1\x1a\x14gogoproto/gogo.proto*\xbd\x01\n\x06Status\x12-\n\x12STATUS_UNSPECIFIED\x10\x00\x1a\x15\x8a\x9d \x11StatusUnspecified\x12#\n\rSTATUS_ACTIVE\x10\x01\x1a\x10\x8a\x9d \x0cStatusActive\x126\n\x17STATUS_INACTIVE_PENDING\x10\x02\x1a\x19\x8a\x9d \x15StatusInactivePending\x12'\n\x0fSTATUS_INACTIVE\x10\x03\x1a\x12\x8a\x9d \x0eStatusInactiveB;Z-github.com/sentinel-official/hub/v12/types/v1\xd0\xe1\x1e\x00\xe8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3")
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.types.v1.status_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/sentinel-official/hub/v12/types/v1\xd0\xe1\x1e\x00\xe8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _STATUS.values_by_name['STATUS_UNSPECIFIED']._options = None
    _STATUS.values_by_name['STATUS_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x11StatusUnspecified'
    _STATUS.values_by_name['STATUS_ACTIVE']._options = None
    _STATUS.values_by_name['STATUS_ACTIVE']._serialized_options = b'\x8a\x9d \x0cStatusActive'
    _STATUS.values_by_name['STATUS_INACTIVE_PENDING']._options = None
    _STATUS.values_by_name['STATUS_INACTIVE_PENDING']._serialized_options = b'\x8a\x9d \x15StatusInactivePending'
    _STATUS.values_by_name['STATUS_INACTIVE']._options = None
    _STATUS.values_by_name['STATUS_INACTIVE']._serialized_options = b'\x8a\x9d \x0eStatusInactive'
    _STATUS._serialized_start = 76
    _STATUS._serialized_end = 265
