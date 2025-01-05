"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/notification.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import label_pb2 as google_dot_api_dot_label__pb2
from ....google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
from ....google.monitoring.v3 import mutation_record_pb2 as google_dot_monitoring_dot_v3_dot_mutation__record__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/monitoring/v3/notification.proto\x12\x14google.monitoring.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x16google/api/label.proto\x1a\x1dgoogle/api/launch_stage.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/common.proto\x1a*google/monitoring/v3/mutation_record.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa5\x04\n\x1dNotificationChannelDescriptor\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12+\n\x06labels\x18\x04 \x03(\x0b2\x1b.google.api.LabelDescriptor\x12>\n\x0fsupported_tiers\x18\x05 \x03(\x0e2!.google.monitoring.v3.ServiceTierB\x02\x18\x01\x12-\n\x0claunch_stage\x18\x07 \x01(\x0e2\x17.google.api.LaunchStage:\xa0\x02\xeaA\x9c\x02\n7monitoring.googleapis.com/NotificationChannelDescriptor\x12Fprojects/{project}/notificationChannelDescriptors/{channel_descriptor}\x12Porganizations/{organization}/notificationChannelDescriptors/{channel_descriptor}\x12Dfolders/{folder}/notificationChannelDescriptors/{channel_descriptor}\x12\x01*"\xbb\x07\n\x13NotificationChannel\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\x04name\x18\x06 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12E\n\x06labels\x18\x05 \x03(\x0b25.google.monitoring.v3.NotificationChannel.LabelsEntry\x12N\n\x0buser_labels\x18\x08 \x03(\x0b29.google.monitoring.v3.NotificationChannel.UserLabelsEntry\x12Y\n\x13verification_status\x18\t \x01(\x0e2<.google.monitoring.v3.NotificationChannel.VerificationStatus\x12+\n\x07enabled\x18\x0b \x01(\x0b2\x1a.google.protobuf.BoolValue\x12=\n\x0fcreation_record\x18\x0c \x01(\x0b2$.google.monitoring.v3.MutationRecord\x12>\n\x10mutation_records\x18\r \x03(\x0b2$.google.monitoring.v3.MutationRecord\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"W\n\x12VerificationStatus\x12#\n\x1fVERIFICATION_STATUS_UNSPECIFIED\x10\x00\x12\x0e\n\nUNVERIFIED\x10\x01\x12\x0c\n\x08VERIFIED\x10\x02:\xfe\x01\xeaA\xfa\x01\n-monitoring.googleapis.com/NotificationChannel\x12>projects/{project}/notificationChannels/{notification_channel}\x12Horganizations/{organization}/notificationChannels/{notification_channel}\x12<folders/{folder}/notificationChannels/{notification_channel}\x12\x01*B\xcc\x01\n\x18com.google.monitoring.v3B\x11NotificationProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.notification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x11NotificationProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_NOTIFICATIONCHANNELDESCRIPTOR'].fields_by_name['supported_tiers']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELDESCRIPTOR'].fields_by_name['supported_tiers']._serialized_options = b'\x18\x01'
    _globals['_NOTIFICATIONCHANNELDESCRIPTOR']._loaded_options = None
    _globals['_NOTIFICATIONCHANNELDESCRIPTOR']._serialized_options = b'\xeaA\x9c\x02\n7monitoring.googleapis.com/NotificationChannelDescriptor\x12Fprojects/{project}/notificationChannelDescriptors/{channel_descriptor}\x12Porganizations/{organization}/notificationChannelDescriptors/{channel_descriptor}\x12Dfolders/{folder}/notificationChannelDescriptors/{channel_descriptor}\x12\x01*'
    _globals['_NOTIFICATIONCHANNEL_LABELSENTRY']._loaded_options = None
    _globals['_NOTIFICATIONCHANNEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NOTIFICATIONCHANNEL_USERLABELSENTRY']._loaded_options = None
    _globals['_NOTIFICATIONCHANNEL_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NOTIFICATIONCHANNEL'].fields_by_name['name']._loaded_options = None
    _globals['_NOTIFICATIONCHANNEL'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_NOTIFICATIONCHANNEL']._loaded_options = None
    _globals['_NOTIFICATIONCHANNEL']._serialized_options = b'\xeaA\xfa\x01\n-monitoring.googleapis.com/NotificationChannel\x12>projects/{project}/notificationChannels/{notification_channel}\x12Horganizations/{organization}/notificationChannels/{notification_channel}\x12<folders/{folder}/notificationChannels/{notification_channel}\x12\x01*'
    _globals['_NOTIFICATIONCHANNELDESCRIPTOR']._serialized_start = 292
    _globals['_NOTIFICATIONCHANNELDESCRIPTOR']._serialized_end = 841
    _globals['_NOTIFICATIONCHANNEL']._serialized_start = 844
    _globals['_NOTIFICATIONCHANNEL']._serialized_end = 1799
    _globals['_NOTIFICATIONCHANNEL_LABELSENTRY']._serialized_start = 1357
    _globals['_NOTIFICATIONCHANNEL_LABELSENTRY']._serialized_end = 1402
    _globals['_NOTIFICATIONCHANNEL_USERLABELSENTRY']._serialized_start = 1404
    _globals['_NOTIFICATIONCHANNEL_USERLABELSENTRY']._serialized_end = 1453
    _globals['_NOTIFICATIONCHANNEL_VERIFICATIONSTATUS']._serialized_start = 1455
    _globals['_NOTIFICATIONCHANNEL_VERIFICATIONSTATUS']._serialized_end = 1542