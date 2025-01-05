"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v1/proof.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.types.v1 import bandwidth_pb2 as sentinel_dot_types_dot_v1_dot_bandwidth__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsentinel/session/v1/proof.proto\x12\x13sentinel.session.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a!sentinel/types/v1/bandwidth.proto"\x81\x01\n\x05Proof\x12\n\n\x02id\x18\x01 \x01(\x04\x125\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x125\n\tbandwidth\x18\x03 \x01(\x0b2\x1c.sentinel.types.v1.BandwidthB\x04\xc8\xde\x1f\x00BAZ7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v1.proof_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_PROOF'].fields_by_name['duration']._loaded_options = None
    _globals['_PROOF'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PROOF'].fields_by_name['bandwidth']._loaded_options = None
    _globals['_PROOF'].fields_by_name['bandwidth']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PROOF']._serialized_start = 146
    _globals['_PROOF']._serialized_end = 275