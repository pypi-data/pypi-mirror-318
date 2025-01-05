"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1beta1/asset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1beta1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1beta1_dot_security__marks__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/securitycenter/v1beta1/asset.proto\x12#google.cloud.securitycenter.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/securitycenter/v1beta1/security_marks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd3\x05\n\x05Asset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12g\n\x1asecurity_center_properties\x18\x02 \x01(\x0b2C.google.cloud.securitycenter.v1beta1.Asset.SecurityCenterProperties\x12_\n\x13resource_properties\x18\x07 \x03(\x0b2B.google.cloud.securitycenter.v1beta1.Asset.ResourcePropertiesEntry\x12J\n\x0esecurity_marks\x18\x08 \x01(\x0b22.google.cloud.securitycenter.v1beta1.SecurityMarks\x12/\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x99\x01\n\x18SecurityCenterProperties\x12\x1a\n\rresource_name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x17\n\x0fresource_parent\x18\x03 \x01(\t\x12\x18\n\x10resource_project\x18\x04 \x01(\t\x12\x17\n\x0fresource_owners\x18\x05 \x03(\t\x1aQ\n\x17ResourcePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01:U\xeaAR\n#securitycenter.googleapis.com/Asset\x12+organizations/{organization}/assets/{asset}B|\n\'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1beta1.asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpb"
    _globals['_ASSET_SECURITYCENTERPROPERTIES'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSET_SECURITYCENTERPROPERTIES'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._loaded_options = None
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_ASSET']._loaded_options = None
    _globals['_ASSET']._serialized_options = b'\xeaAR\n#securitycenter.googleapis.com/Asset\x12+organizations/{organization}/assets/{asset}'
    _globals['_ASSET']._serialized_start = 270
    _globals['_ASSET']._serialized_end = 993
    _globals['_ASSET_SECURITYCENTERPROPERTIES']._serialized_start = 670
    _globals['_ASSET_SECURITYCENTERPROPERTIES']._serialized_end = 823
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._serialized_start = 825
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._serialized_end = 906