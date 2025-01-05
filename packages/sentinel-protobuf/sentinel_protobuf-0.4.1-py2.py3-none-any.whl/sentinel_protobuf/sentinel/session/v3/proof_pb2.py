"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v3/proof.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsentinel/session/v3/proof.proto\x12\x13sentinel.session.v3\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"\xbe\x01\n\x05Proof\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x125\n\x0edownload_bytes\x18\x02 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x123\n\x0cupload_bytes\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x125\n\x08duration\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01BAZ7github.com/sentinel-official/hub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v3.proof_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_PROOF'].fields_by_name['id']._loaded_options = None
    _globals['_PROOF'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_PROOF'].fields_by_name['download_bytes']._loaded_options = None
    _globals['_PROOF'].fields_by_name['download_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_PROOF'].fields_by_name['upload_bytes']._loaded_options = None
    _globals['_PROOF'].fields_by_name['upload_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_PROOF'].fields_by_name['duration']._loaded_options = None
    _globals['_PROOF'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PROOF']._serialized_start = 111
    _globals['_PROOF']._serialized_end = 301