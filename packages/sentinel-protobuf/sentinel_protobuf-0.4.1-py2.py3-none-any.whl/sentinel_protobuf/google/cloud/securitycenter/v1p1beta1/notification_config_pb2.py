"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1p1beta1/notification_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/securitycenter/v1p1beta1/notification_config.proto\x12%google.cloud.securitycenter.v1p1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb6\x04\n\x12NotificationConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12W\n\nevent_type\x18\x03 \x01(\x0e2C.google.cloud.securitycenter.v1p1beta1.NotificationConfig.EventType\x126\n\x0cpubsub_topic\x18\x04 \x01(\tB \xfaA\x1d\n\x1bpubsub.googleapis.com/Topic\x12\x1c\n\x0fservice_account\x18\x05 \x01(\tB\x03\xe0A\x03\x12e\n\x10streaming_config\x18\x06 \x01(\x0b2I.google.cloud.securitycenter.v1p1beta1.NotificationConfig.StreamingConfigH\x00\x1a!\n\x0fStreamingConfig\x12\x0e\n\x06filter\x18\x01 \x01(\t"4\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07FINDING\x10\x01:}\xeaAz\n0securitycenter.googleapis.com/NotificationConfig\x12Forganizations/{organization}/notificationConfigs/{notification_config}B\x0f\n\rnotify_configB\xbe\x02\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1p1beta1.notification_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}'
    _globals['_NOTIFICATIONCONFIG'].fields_by_name['pubsub_topic']._loaded_options = None
    _globals['_NOTIFICATIONCONFIG'].fields_by_name['pubsub_topic']._serialized_options = b'\xfaA\x1d\n\x1bpubsub.googleapis.com/Topic'
    _globals['_NOTIFICATIONCONFIG'].fields_by_name['service_account']._loaded_options = None
    _globals['_NOTIFICATIONCONFIG'].fields_by_name['service_account']._serialized_options = b'\xe0A\x03'
    _globals['_NOTIFICATIONCONFIG']._loaded_options = None
    _globals['_NOTIFICATIONCONFIG']._serialized_options = b'\xeaAz\n0securitycenter.googleapis.com/NotificationConfig\x12Forganizations/{organization}/notificationConfigs/{notification_config}'
    _globals['_NOTIFICATIONCONFIG']._serialized_start = 167
    _globals['_NOTIFICATIONCONFIG']._serialized_end = 733
    _globals['_NOTIFICATIONCONFIG_STREAMINGCONFIG']._serialized_start = 502
    _globals['_NOTIFICATIONCONFIG_STREAMINGCONFIG']._serialized_end = 535
    _globals['_NOTIFICATIONCONFIG_EVENTTYPE']._serialized_start = 537
    _globals['_NOTIFICATIONCONFIG_EVENTTYPE']._serialized_end = 589