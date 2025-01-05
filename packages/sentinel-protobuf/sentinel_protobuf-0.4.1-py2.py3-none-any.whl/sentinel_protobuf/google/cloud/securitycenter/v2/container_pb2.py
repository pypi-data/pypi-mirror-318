"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/container.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.securitycenter.v2 import label_pb2 as google_dot_cloud_dot_securitycenter_dot_v2_dot_label__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/securitycenter/v2/container.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a*google/cloud/securitycenter/v2/label.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x01\n\tContainer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x10\n\x08image_id\x18\x03 \x01(\t\x125\n\x06labels\x18\x04 \x03(\x0b2%.google.cloud.securitycenter.v2.Label\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\xe8\x01\n"com.google.cloud.securitycenter.v2B\x0eContainerProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.container_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0eContainerProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_CONTAINER']._serialized_start = 160
    _globals['_CONTAINER']._serialized_end = 320