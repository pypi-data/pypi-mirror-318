"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/identity/accesscontextmanager/v1/access_level.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.identity.accesscontextmanager.type import device_resources_pb2 as google_dot_identity_dot_accesscontextmanager_dot_type_dot_device__resources__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/identity/accesscontextmanager/v1/access_level.proto\x12\'google.identity.accesscontextmanager.v1\x1a\x19google/api/resource.proto\x1a@google/identity/accesscontextmanager/type/device_resources.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/expr.proto"\xaa\x03\n\x0bAccessLevel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12D\n\x05basic\x18\x04 \x01(\x0b23.google.identity.accesscontextmanager.v1.BasicLevelH\x00\x12F\n\x06custom\x18\x05 \x01(\x0b24.google.identity.accesscontextmanager.v1.CustomLevelH\x00\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp:p\xeaAm\n/accesscontextmanager.googleapis.com/AccessLevel\x12:accessPolicies/{access_policy}/accessLevels/{access_level}B\x07\n\x05level"\xef\x01\n\nBasicLevel\x12F\n\nconditions\x18\x01 \x03(\x0b22.google.identity.accesscontextmanager.v1.Condition\x12j\n\x12combining_function\x18\x02 \x01(\x0e2N.google.identity.accesscontextmanager.v1.BasicLevel.ConditionCombiningFunction"-\n\x1aConditionCombiningFunction\x12\x07\n\x03AND\x10\x00\x12\x06\n\x02OR\x10\x01"\xc3\x01\n\tCondition\x12\x16\n\x0eip_subnetworks\x18\x01 \x03(\t\x12L\n\rdevice_policy\x18\x02 \x01(\x0b25.google.identity.accesscontextmanager.v1.DevicePolicy\x12\x1e\n\x16required_access_levels\x18\x03 \x03(\t\x12\x0e\n\x06negate\x18\x05 \x01(\x08\x12\x0f\n\x07members\x18\x06 \x03(\t\x12\x0f\n\x07regions\x18\x07 \x03(\t".\n\x0bCustomLevel\x12\x1f\n\x04expr\x18\x01 \x01(\x0b2\x11.google.type.Expr"\x89\x03\n\x0cDevicePolicy\x12\x1a\n\x12require_screenlock\x18\x01 \x01(\x08\x12f\n\x1ballowed_encryption_statuses\x18\x02 \x03(\x0e2A.google.identity.accesscontextmanager.type.DeviceEncryptionStatus\x12M\n\x0eos_constraints\x18\x03 \x03(\x0b25.google.identity.accesscontextmanager.v1.OsConstraint\x12j\n allowed_device_management_levels\x18\x06 \x03(\x0e2@.google.identity.accesscontextmanager.type.DeviceManagementLevel\x12\x1e\n\x16require_admin_approval\x18\x07 \x01(\x08\x12\x1a\n\x12require_corp_owned\x18\x08 \x01(\x08"\x8f\x01\n\x0cOsConstraint\x12B\n\x07os_type\x18\x01 \x01(\x0e21.google.identity.accesscontextmanager.type.OsType\x12\x17\n\x0fminimum_version\x18\x02 \x01(\t\x12"\n\x1arequire_verified_chrome_os\x18\x03 \x01(\x08B\xa7\x02\n+com.google.identity.accesscontextmanager.v1B\x10AccessLevelProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02\'Google.Identity.AccessContextManager.V1\xca\x02\'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.identity.accesscontextmanager.v1.access_level_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.identity.accesscontextmanager.v1B\x10AccessLevelProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02'Google.Identity.AccessContextManager.V1\xca\x02'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1"
    _globals['_ACCESSLEVEL']._loaded_options = None
    _globals['_ACCESSLEVEL']._serialized_options = b'\xeaAm\n/accesscontextmanager.googleapis.com/AccessLevel\x12:accessPolicies/{access_policy}/accessLevels/{access_level}'
    _globals['_ACCESSLEVEL']._serialized_start = 254
    _globals['_ACCESSLEVEL']._serialized_end = 680
    _globals['_BASICLEVEL']._serialized_start = 683
    _globals['_BASICLEVEL']._serialized_end = 922
    _globals['_BASICLEVEL_CONDITIONCOMBININGFUNCTION']._serialized_start = 877
    _globals['_BASICLEVEL_CONDITIONCOMBININGFUNCTION']._serialized_end = 922
    _globals['_CONDITION']._serialized_start = 925
    _globals['_CONDITION']._serialized_end = 1120
    _globals['_CUSTOMLEVEL']._serialized_start = 1122
    _globals['_CUSTOMLEVEL']._serialized_end = 1168
    _globals['_DEVICEPOLICY']._serialized_start = 1171
    _globals['_DEVICEPOLICY']._serialized_end = 1564
    _globals['_OSCONSTRAINT']._serialized_start = 1567
    _globals['_OSCONSTRAINT']._serialized_end = 1710