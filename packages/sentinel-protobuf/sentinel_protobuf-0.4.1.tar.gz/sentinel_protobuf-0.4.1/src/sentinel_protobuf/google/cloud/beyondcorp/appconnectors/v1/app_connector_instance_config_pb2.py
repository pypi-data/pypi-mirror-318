"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/beyondcorp/appconnectors/v1/app_connector_instance_config.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/cloud/beyondcorp/appconnectors/v1/app_connector_instance_config.proto\x12(google.cloud.beyondcorp.appconnectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto"\x91\x02\n\x1aAppConnectorInstanceConfig\x12\x1c\n\x0fsequence_number\x18\x01 \x01(\x03B\x03\xe0A\x02\x12-\n\x0finstance_config\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12Y\n\x13notification_config\x18\x03 \x01(\x0b2<.google.cloud.beyondcorp.appconnectors.v1.NotificationConfig\x12K\n\x0cimage_config\x18\x04 \x01(\x0b25.google.cloud.beyondcorp.appconnectors.v1.ImageConfig"\xd7\x01\n\x12NotificationConfig\x12y\n\x13pubsub_notification\x18\x01 \x01(\x0b2Z.google.cloud.beyondcorp.appconnectors.v1.NotificationConfig.CloudPubSubNotificationConfigH\x00\x1a<\n\x1dCloudPubSubNotificationConfig\x12\x1b\n\x13pubsub_subscription\x18\x01 \x01(\tB\x08\n\x06config"9\n\x0bImageConfig\x12\x14\n\x0ctarget_image\x18\x01 \x01(\t\x12\x14\n\x0cstable_image\x18\x02 \x01(\tB\xaa\x02\n,com.google.cloud.beyondcorp.appconnectors.v1B\x1fAppConnectorInstanceConfigProtoP\x01ZRcloud.google.com/go/beyondcorp/appconnectors/apiv1/appconnectorspb;appconnectorspb\xaa\x02(Google.Cloud.BeyondCorp.AppConnectors.V1\xca\x02(Google\\Cloud\\BeyondCorp\\AppConnectors\\V1\xea\x02,Google::Cloud::BeyondCorp::AppConnectors::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.beyondcorp.appconnectors.v1.app_connector_instance_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.beyondcorp.appconnectors.v1B\x1fAppConnectorInstanceConfigProtoP\x01ZRcloud.google.com/go/beyondcorp/appconnectors/apiv1/appconnectorspb;appconnectorspb\xaa\x02(Google.Cloud.BeyondCorp.AppConnectors.V1\xca\x02(Google\\Cloud\\BeyondCorp\\AppConnectors\\V1\xea\x02,Google::Cloud::BeyondCorp::AppConnectors::V1'
    _globals['_APPCONNECTORINSTANCECONFIG'].fields_by_name['sequence_number']._loaded_options = None
    _globals['_APPCONNECTORINSTANCECONFIG'].fields_by_name['sequence_number']._serialized_options = b'\xe0A\x02'
    _globals['_APPCONNECTORINSTANCECONFIG']._serialized_start = 183
    _globals['_APPCONNECTORINSTANCECONFIG']._serialized_end = 456
    _globals['_NOTIFICATIONCONFIG']._serialized_start = 459
    _globals['_NOTIFICATIONCONFIG']._serialized_end = 674
    _globals['_NOTIFICATIONCONFIG_CLOUDPUBSUBNOTIFICATIONCONFIG']._serialized_start = 604
    _globals['_NOTIFICATIONCONFIG_CLOUDPUBSUBNOTIFICATIONCONFIG']._serialized_end = 664
    _globals['_IMAGECONFIG']._serialized_start = 676
    _globals['_IMAGECONFIG']._serialized_end = 733