"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/asset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1 import folder_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_folder__pb2
from .....google.cloud.securitycenter.v1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_security__marks__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/securitycenter/v1/asset.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x19google/api/resource.proto\x1a+google/cloud/securitycenter/v1/folder.proto\x1a3google/cloud/securitycenter/v1/security_marks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb8\x08\n\x05Asset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12b\n\x1asecurity_center_properties\x18\x02 \x01(\x0b2>.google.cloud.securitycenter.v1.Asset.SecurityCenterProperties\x12Z\n\x13resource_properties\x18\x07 \x03(\x0b2=.google.cloud.securitycenter.v1.Asset.ResourcePropertiesEntry\x12E\n\x0esecurity_marks\x18\x08 \x01(\x0b2-.google.cloud.securitycenter.v1.SecurityMarks\x12/\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\niam_policy\x18\x0b \x01(\x0b2/.google.cloud.securitycenter.v1.Asset.IamPolicy\x12\x16\n\x0ecanonical_name\x18\r \x01(\t\x1a\xb9\x02\n\x18SecurityCenterProperties\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x17\n\x0fresource_parent\x18\x03 \x01(\t\x12\x18\n\x10resource_project\x18\x04 \x01(\t\x12\x17\n\x0fresource_owners\x18\x05 \x03(\t\x12\x1d\n\x15resource_display_name\x18\x06 \x01(\t\x12$\n\x1cresource_parent_display_name\x18\x07 \x01(\t\x12%\n\x1dresource_project_display_name\x18\x08 \x01(\t\x127\n\x07folders\x18\n \x03(\x0b2&.google.cloud.securitycenter.v1.Folder\x1a \n\tIamPolicy\x12\x13\n\x0bpolicy_blob\x18\x01 \x01(\t\x1aQ\n\x17ResourcePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01:\xa9\x01\xeaA\xa5\x01\n#securitycenter.googleapis.com/Asset\x12+organizations/{organization}/assets/{asset}\x12\x1ffolders/{folder}/assets/{asset}\x12!projects/{project}/assets/{asset}*\x06assets2\x05assetB\xd8\x01\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._loaded_options = None
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_ASSET']._loaded_options = None
    _globals['_ASSET']._serialized_options = b'\xeaA\xa5\x01\n#securitycenter.googleapis.com/Asset\x12+organizations/{organization}/assets/{asset}\x12\x1ffolders/{folder}/assets/{asset}\x12!projects/{project}/assets/{asset}*\x06assets2\x05asset'
    _globals['_ASSET']._serialized_start = 267
    _globals['_ASSET']._serialized_end = 1347
    _globals['_ASSET_SECURITYCENTERPROPERTIES']._serialized_start = 745
    _globals['_ASSET_SECURITYCENTERPROPERTIES']._serialized_end = 1058
    _globals['_ASSET_IAMPOLICY']._serialized_start = 1060
    _globals['_ASSET_IAMPOLICY']._serialized_end = 1092
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._serialized_start = 1094
    _globals['_ASSET_RESOURCEPROPERTIESENTRY']._serialized_end = 1175