"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/dataset_version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/aiplatform/v1/dataset_version.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf2\x03\n\x0eDatasetVersion\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x03 \x01(\t\x12#\n\x16big_query_dataset_name\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x07 \x01(\t\x120\n\x08metadata\x18\x08 \x01(\x0b2\x16.google.protobuf.ValueB\x06\xe0A\x03\xe0A\x02\x12\x1c\n\x0fmodel_reference\x18\t \x01(\tB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\n \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x0b \x01(\x08B\x03\xe0A\x03:\x8c\x01\xeaA\x88\x01\n(aiplatform.googleapis.com/DatasetVersion\x12\\projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}B\xd1\x01\n\x1ecom.google.cloud.aiplatform.v1B\x13DatasetVersionProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.dataset_version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x13DatasetVersionProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_DATASETVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_DATASETVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETVERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETVERSION'].fields_by_name['big_query_dataset_name']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['big_query_dataset_name']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETVERSION'].fields_by_name['metadata']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03\xe0A\x02'
    _globals['_DATASETVERSION'].fields_by_name['model_reference']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['model_reference']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETVERSION'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETVERSION'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DATASETVERSION'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETVERSION']._loaded_options = None
    _globals['_DATASETVERSION']._serialized_options = b'\xeaA\x88\x01\n(aiplatform.googleapis.com/DatasetVersion\x12\\projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}'
    _globals['_DATASETVERSION']._serialized_start = 204
    _globals['_DATASETVERSION']._serialized_end = 702