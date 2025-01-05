"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/job_creation_reason.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/bigquery/v2/job_creation_reason.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\xb5\x01\n\x11JobCreationReason\x12C\n\x04code\x18\x01 \x01(\x0e20.google.cloud.bigquery.v2.JobCreationReason.CodeB\x03\xe0A\x03"[\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\r\n\tREQUESTED\x10\x01\x12\x10\n\x0cLONG_RUNNING\x10\x02\x12\x11\n\rLARGE_RESULTS\x10\x03\x12\t\n\x05OTHER\x10\x04Br\n\x1ccom.google.cloud.bigquery.v2B\x16JobCreationReasonProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.job_creation_reason_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x16JobCreationReasonProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_JOBCREATIONREASON'].fields_by_name['code']._loaded_options = None
    _globals['_JOBCREATIONREASON'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_JOBCREATIONREASON']._serialized_start = 114
    _globals['_JOBCREATIONREASON']._serialized_end = 295
    _globals['_JOBCREATIONREASON_CODE']._serialized_start = 204
    _globals['_JOBCREATIONREASON_CODE']._serialized_end = 295