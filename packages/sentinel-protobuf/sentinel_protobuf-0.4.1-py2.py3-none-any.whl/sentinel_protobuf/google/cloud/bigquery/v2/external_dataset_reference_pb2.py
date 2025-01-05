"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/external_dataset_reference.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/bigquery/v2/external_dataset_reference.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x82\x01\n\x18ExternalDatasetReference\x12\x1c\n\x0fexternal_source\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\nconnection\x18\x03 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/ConnectionB\xec\x01\n\x1ccom.google.cloud.bigquery.v2B\x1dExternalDatasetReferenceProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.external_dataset_reference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x1dExternalDatasetReferenceProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}'
    _globals['_EXTERNALDATASETREFERENCE'].fields_by_name['external_source']._loaded_options = None
    _globals['_EXTERNALDATASETREFERENCE'].fields_by_name['external_source']._serialized_options = b'\xe0A\x02'
    _globals['_EXTERNALDATASETREFERENCE'].fields_by_name['connection']._loaded_options = None
    _globals['_EXTERNALDATASETREFERENCE'].fields_by_name['connection']._serialized_options = b'\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_EXTERNALDATASETREFERENCE']._serialized_start = 148
    _globals['_EXTERNALDATASETREFERENCE']._serialized_end = 278