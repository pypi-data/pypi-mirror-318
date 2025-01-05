"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/annotation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import user_action_reference_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_user__action__reference__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/aiplatform/v1/annotation.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/aiplatform/v1/user_action_reference.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x04\n\nAnnotation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12payload_schema_uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12,\n\x07payload\x18\x03 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x01\x12O\n\x11annotation_source\x18\x05 \x01(\x0b2/.google.cloud.aiplatform.v1.UserActionReferenceB\x03\xe0A\x03\x12G\n\x06labels\x18\x06 \x03(\x0b22.google.cloud.aiplatform.v1.Annotation.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x95\x01\xeaA\x91\x01\n$aiplatform.googleapis.com/Annotation\x12iprojects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}/annotations/{annotation}B\xcd\x01\n\x1ecom.google.cloud.aiplatform.v1B\x0fAnnotationProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x0fAnnotationProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_ANNOTATION_LABELSENTRY']._loaded_options = None
    _globals['_ANNOTATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ANNOTATION'].fields_by_name['name']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATION'].fields_by_name['payload_schema_uri']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['payload_schema_uri']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATION'].fields_by_name['payload']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATION'].fields_by_name['etag']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATION'].fields_by_name['annotation_source']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['annotation_source']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATION'].fields_by_name['labels']._loaded_options = None
    _globals['_ANNOTATION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATION']._loaded_options = None
    _globals['_ANNOTATION']._serialized_options = b'\xeaA\x91\x01\n$aiplatform.googleapis.com/Annotation\x12iprojects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}/annotations/{annotation}'
    _globals['_ANNOTATION']._serialized_start = 255
    _globals['_ANNOTATION']._serialized_end = 845
    _globals['_ANNOTATION_LABELSENTRY']._serialized_start = 648
    _globals['_ANNOTATION_LABELSENTRY']._serialized_end = 693