"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/aiplatform/v1beta1/event.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x03\n\x05Event\x12<\n\x08artifact\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Artifact\x12>\n\texecution\x18\x02 \x01(\tB+\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/Execution\x123\n\nevent_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12>\n\x04type\x18\x04 \x01(\x0e2+.google.cloud.aiplatform.v1beta1.Event.TypeB\x03\xe0A\x02\x12B\n\x06labels\x18\x05 \x03(\x0b22.google.cloud.aiplatform.v1beta1.Event.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"3\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05INPUT\x10\x01\x12\n\n\x06OUTPUT\x10\x02B\xe1\x01\n#com.google.cloud.aiplatform.v1beta1B\nEventProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\nEventProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_EVENT_LABELSENTRY']._loaded_options = None
    _globals['_EVENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EVENT'].fields_by_name['artifact']._loaded_options = None
    _globals['_EVENT'].fields_by_name['artifact']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Artifact'
    _globals['_EVENT'].fields_by_name['execution']._loaded_options = None
    _globals['_EVENT'].fields_by_name['execution']._serialized_options = b'\xe0A\x03\xfaA%\n#aiplatform.googleapis.com/Execution'
    _globals['_EVENT'].fields_by_name['event_time']._loaded_options = None
    _globals['_EVENT'].fields_by_name['event_time']._serialized_options = b'\xe0A\x03'
    _globals['_EVENT'].fields_by_name['type']._loaded_options = None
    _globals['_EVENT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_EVENT']._serialized_start = 174
    _globals['_EVENT']._serialized_end = 592
    _globals['_EVENT_LABELSENTRY']._serialized_start = 494
    _globals['_EVENT_LABELSENTRY']._serialized_end = 539
    _globals['_EVENT_TYPE']._serialized_start = 541
    _globals['_EVENT_TYPE']._serialized_end = 592