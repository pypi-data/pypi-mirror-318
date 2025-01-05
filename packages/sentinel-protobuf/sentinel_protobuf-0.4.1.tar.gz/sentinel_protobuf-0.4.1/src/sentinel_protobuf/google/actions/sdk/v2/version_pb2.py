"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/actions/sdk/v2/version.proto\x12\x15google.actions.sdk.v2\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x99\x04\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12B\n\rversion_state\x18\x02 \x01(\x0b2+.google.actions.sdk.v2.Version.VersionState\x12\x0f\n\x07creator\x18\x03 \x01(\t\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\xad\x02\n\x0cVersionState\x12@\n\x05state\x18\x01 \x01(\x0e21.google.actions.sdk.v2.Version.VersionState.State\x12\x0f\n\x07message\x18\x02 \x01(\t"\xc9\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14CREATION_IN_PROGRESS\x10\x01\x12\x13\n\x0fCREATION_FAILED\x10\x02\x12\x0b\n\x07CREATED\x10\x03\x12\x16\n\x12REVIEW_IN_PROGRESS\x10\x04\x12\x0c\n\x08APPROVED\x10\x05\x12\x1a\n\x16CONDITIONALLY_APPROVED\x10\x06\x12\n\n\x06DENIED\x10\x07\x12\x12\n\x0eUNDER_TAKEDOWN\x10\x08\x12\x0b\n\x07DELETED\x10\t:J\xeaAG\n\x1eactions.googleapis.com/Version\x12%projects/{project}/versions/{version}Be\n\x19com.google.actions.sdk.v2B\x0cVersionProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x0cVersionProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_VERSION']._loaded_options = None
    _globals['_VERSION']._serialized_options = b'\xeaAG\n\x1eactions.googleapis.com/Version\x12%projects/{project}/versions/{version}'
    _globals['_VERSION']._serialized_start = 123
    _globals['_VERSION']._serialized_end = 660
    _globals['_VERSION_VERSIONSTATE']._serialized_start = 283
    _globals['_VERSION_VERSIONSTATE']._serialized_end = 584
    _globals['_VERSION_VERSIONSTATE_STATE']._serialized_start = 383
    _globals['_VERSION_VERSIONSTATE_STATE']._serialized_end = 584