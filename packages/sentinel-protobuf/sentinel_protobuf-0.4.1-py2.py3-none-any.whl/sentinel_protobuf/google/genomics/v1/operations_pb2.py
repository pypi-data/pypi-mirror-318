"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/operations.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/genomics/v1/operations.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc6\x03\n\x11OperationMetadata\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12%\n\x07request\x18\x05 \x01(\x0b2\x14.google.protobuf.Any\x122\n\x06events\x18\x06 \x03(\x0b2".google.genomics.v1.OperationEvent\x12\x11\n\tclient_id\x18\x07 \x01(\t\x12.\n\x10runtime_metadata\x18\x08 \x01(\x0b2\x14.google.protobuf.Any\x12A\n\x06labels\x18\t \x03(\x0b21.google.genomics.v1.OperationMetadata.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x83\x01\n\x0eOperationEvent\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0bdescription\x18\x03 \x01(\tBj\n\x16com.google.genomics.v1B\x0fOperationsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\x0fOperationsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_OPERATIONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_OPERATIONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_OPERATIONMETADATA']._serialized_start = 150
    _globals['_OPERATIONMETADATA']._serialized_end = 604
    _globals['_OPERATIONMETADATA_LABELSENTRY']._serialized_start = 559
    _globals['_OPERATIONMETADATA_LABELSENTRY']._serialized_end = 604
    _globals['_OPERATIONEVENT']._serialized_start = 607
    _globals['_OPERATIONEVENT']._serialized_end = 738