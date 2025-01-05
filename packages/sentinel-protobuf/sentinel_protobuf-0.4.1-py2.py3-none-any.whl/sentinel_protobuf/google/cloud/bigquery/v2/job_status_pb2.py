"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/job_status.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import error_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/bigquery/v2/job_status.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a$google/cloud/bigquery/v2/error.proto"\x9b\x01\n\tJobStatus\x12?\n\x0cerror_result\x18\x01 \x01(\x0b2$.google.cloud.bigquery.v2.ErrorProtoB\x03\xe0A\x03\x129\n\x06errors\x18\x02 \x03(\x0b2$.google.cloud.bigquery.v2.ErrorProtoB\x03\xe0A\x03\x12\x12\n\x05state\x18\x03 \x01(\tB\x03\xe0A\x03Bh\n\x1ccom.google.cloud.bigquery.v2B\x0eJobStatusProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.job_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x0eJobStatusProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_JOBSTATUS'].fields_by_name['error_result']._loaded_options = None
    _globals['_JOBSTATUS'].fields_by_name['error_result']._serialized_options = b'\xe0A\x03'
    _globals['_JOBSTATUS'].fields_by_name['errors']._loaded_options = None
    _globals['_JOBSTATUS'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_JOBSTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_JOBSTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_JOBSTATUS']._serialized_start = 143
    _globals['_JOBSTATUS']._serialized_end = 298