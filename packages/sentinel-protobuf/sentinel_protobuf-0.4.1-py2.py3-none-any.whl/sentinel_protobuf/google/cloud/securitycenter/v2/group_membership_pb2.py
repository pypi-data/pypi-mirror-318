"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/group_membership.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/securitycenter/v2/group_membership.proto\x12\x1egoogle.cloud.securitycenter.v2"\xbd\x01\n\x0fGroupMembership\x12M\n\ngroup_type\x18\x01 \x01(\x0e29.google.cloud.securitycenter.v2.GroupMembership.GroupType\x12\x10\n\x08group_id\x18\x02 \x01(\t"I\n\tGroupType\x12\x1a\n\x16GROUP_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cGROUP_TYPE_TOXIC_COMBINATION\x10\x01B\xee\x01\n"com.google.cloud.securitycenter.v2B\x14GroupMembershipProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.group_membership_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x14GroupMembershipProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_GROUPMEMBERSHIP']._serialized_start = 90
    _globals['_GROUPMEMBERSHIP']._serialized_end = 279
    _globals['_GROUPMEMBERSHIP_GROUPTYPE']._serialized_start = 206
    _globals['_GROUPMEMBERSHIP_GROUPTYPE']._serialized_end = 279