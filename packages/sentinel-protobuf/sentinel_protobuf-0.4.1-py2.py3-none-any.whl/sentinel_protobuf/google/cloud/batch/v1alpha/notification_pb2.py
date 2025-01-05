"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/batch/v1alpha/notification.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/batch/v1alpha/notification.proto\x12\x1agoogle.cloud.batch.v1alpha\x1a\x1fgoogle/api/field_behavior.proto")\n\x0cNotification\x12\x19\n\x0cpubsub_topic\x18\x01 \x01(\tB\x03\xe0A\x02B\xcb\x01\n\x1ecom.google.cloud.batch.v1alphaB\x11NotificationProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1alpha.notification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.batch.v1alphaB\x11NotificationProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alpha'
    _globals['_NOTIFICATION'].fields_by_name['pubsub_topic']._loaded_options = None
    _globals['_NOTIFICATION'].fields_by_name['pubsub_topic']._serialized_options = b'\xe0A\x02'
    _globals['_NOTIFICATION']._serialized_start = 110
    _globals['_NOTIFICATION']._serialized_end = 151