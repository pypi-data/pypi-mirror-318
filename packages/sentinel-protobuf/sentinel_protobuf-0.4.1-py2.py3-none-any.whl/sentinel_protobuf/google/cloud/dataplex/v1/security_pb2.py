"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataplex/v1/security.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/dataplex/v1/security.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto"U\n\x12ResourceAccessSpec\x12\x14\n\x07readers\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x14\n\x07writers\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x13\n\x06owners\x18\x03 \x03(\tB\x03\xe0A\x01"&\n\x0eDataAccessSpec\x12\x14\n\x07readers\x18\x01 \x03(\tB\x03\xe0A\x01Bi\n\x1ccom.google.cloud.dataplex.v1B\rSecurityProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.security_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\rSecurityProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_RESOURCEACCESSSPEC'].fields_by_name['readers']._loaded_options = None
    _globals['_RESOURCEACCESSSPEC'].fields_by_name['readers']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEACCESSSPEC'].fields_by_name['writers']._loaded_options = None
    _globals['_RESOURCEACCESSSPEC'].fields_by_name['writers']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEACCESSSPEC'].fields_by_name['owners']._loaded_options = None
    _globals['_RESOURCEACCESSSPEC'].fields_by_name['owners']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSSPEC'].fields_by_name['readers']._loaded_options = None
    _globals['_DATAACCESSSPEC'].fields_by_name['readers']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEACCESSSPEC']._serialized_start = 102
    _globals['_RESOURCEACCESSSPEC']._serialized_end = 187
    _globals['_DATAACCESSSPEC']._serialized_start = 189
    _globals['_DATAACCESSSPEC']._serialized_end = 227