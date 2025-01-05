"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/notification_message.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.securitycenter.v1 import finding_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_finding__pb2
from .....google.cloud.securitycenter.v1 import resource_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/securitycenter/v1/notification_message.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a,google/cloud/securitycenter/v1/finding.proto\x1a-google/cloud/securitycenter/v1/resource.proto"\xb8\x01\n\x13NotificationMessage\x12 \n\x18notification_config_name\x18\x01 \x01(\t\x12:\n\x07finding\x18\x02 \x01(\x0b2\'.google.cloud.securitycenter.v1.FindingH\x00\x12:\n\x08resource\x18\x03 \x01(\x0b2(.google.cloud.securitycenter.v1.ResourceB\x07\n\x05eventB\xf2\x01\n"com.google.cloud.securitycenter.v1B\x18NotificationMessageProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.notification_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x18NotificationMessageProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_NOTIFICATIONMESSAGE']._serialized_start = 187
    _globals['_NOTIFICATIONMESSAGE']._serialized_end = 371