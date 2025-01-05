"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/functions/v1/operations.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/functions/v1/operations.proto\x12\x19google.cloud.functions.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x85\x02\n\x13OperationMetadataV1\x12\x0e\n\x06target\x18\x01 \x01(\t\x126\n\x04type\x18\x02 \x01(\x0e2(.google.cloud.functions.v1.OperationType\x12%\n\x07request\x18\x03 \x01(\x0b2\x14.google.protobuf.Any\x12\x12\n\nversion_id\x18\x04 \x01(\x03\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08build_id\x18\x06 \x01(\t\x12\x14\n\x0csource_token\x18\x07 \x01(\t\x12\x12\n\nbuild_name\x18\x08 \x01(\t*i\n\rOperationType\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0fCREATE_FUNCTION\x10\x01\x12\x13\n\x0fUPDATE_FUNCTION\x10\x02\x12\x13\n\x0fDELETE_FUNCTION\x10\x03Bx\n\x1dcom.google.cloud.functions.v1B\x18FunctionsOperationsProtoP\x01Z;cloud.google.com/go/functions/apiv1/functionspb;functionspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.functions.v1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.functions.v1B\x18FunctionsOperationsProtoP\x01Z;cloud.google.com/go/functions/apiv1/functionspb;functionspb'
    _globals['_OPERATIONTYPE']._serialized_start = 397
    _globals['_OPERATIONTYPE']._serialized_end = 502
    _globals['_OPERATIONMETADATAV1']._serialized_start = 134
    _globals['_OPERATIONMETADATAV1']._serialized_end = 395