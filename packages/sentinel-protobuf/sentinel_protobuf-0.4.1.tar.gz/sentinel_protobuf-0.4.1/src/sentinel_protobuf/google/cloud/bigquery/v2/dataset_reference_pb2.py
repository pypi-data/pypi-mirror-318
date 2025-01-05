"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/dataset_reference.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/bigquery/v2/dataset_reference.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"D\n\x10DatasetReference\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nproject_id\x18\x02 \x01(\tB\x03\xe0A\x01Bo\n\x1ccom.google.cloud.bigquery.v2B\x15DatasetReferenceProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.dataset_reference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x15DatasetReferenceProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_DATASETREFERENCE'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_DATASETREFERENCE'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_DATASETREFERENCE'].fields_by_name['project_id']._loaded_options = None
    _globals['_DATASETREFERENCE'].fields_by_name['project_id']._serialized_options = b'\xe0A\x01'
    _globals['_DATASETREFERENCE']._serialized_start = 111
    _globals['_DATASETREFERENCE']._serialized_end = 179