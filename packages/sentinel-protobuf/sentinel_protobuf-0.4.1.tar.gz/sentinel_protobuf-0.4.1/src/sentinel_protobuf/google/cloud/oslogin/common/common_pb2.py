"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oslogin/common/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/oslogin/common/common.proto\x12\x1bgoogle.cloud.oslogin.common\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdc\x02\n\x0cPosixAccount\x12\x0f\n\x07primary\x18\x01 \x01(\x08\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\x03\x12\x0b\n\x03gid\x18\x04 \x01(\x03\x12\x16\n\x0ehome_directory\x18\x05 \x01(\t\x12\r\n\x05shell\x18\x06 \x01(\t\x12\r\n\x05gecos\x18\x07 \x01(\t\x12\x11\n\tsystem_id\x18\x08 \x01(\t\x12\x17\n\naccount_id\x18\t \x01(\tB\x03\xe0A\x03\x12O\n\x15operating_system_type\x18\n \x01(\x0e20.google.cloud.oslogin.common.OperatingSystemType\x12\x11\n\x04name\x18\x0b \x01(\tB\x03\xe0A\x03:I\xeaAF\n#oslogin.googleapis.com/PosixAccount\x12\x1fusers/{user}/projects/{project}"\xba\x01\n\x0cSshPublicKey\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x14expiration_time_usec\x18\x02 \x01(\x03\x12\x18\n\x0bfingerprint\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04name\x18\x04 \x01(\tB\x03\xe0A\x03:R\xeaAO\n#oslogin.googleapis.com/SshPublicKey\x12(users/{user}/sshPublicKeys/{fingerprint}*T\n\x13OperatingSystemType\x12%\n!OPERATING_SYSTEM_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05LINUX\x10\x01\x12\x0b\n\x07WINDOWS\x10\x02B\xf0\x01\n\x1fcom.google.cloud.oslogin.commonB\x0cOsLoginProtoZ4cloud.google.com/go/oslogin/common/commonpb;commonpb\xaa\x02\x1bGoogle.Cloud.OsLogin.Common\xca\x02\x1bGoogle\\Cloud\\OsLogin\\Common\xea\x02\x1eGoogle::Cloud::OsLogin::Common\xeaA+\n\x1boslogin.googleapis.com/User\x12\x0cusers/{user}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oslogin.common.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.oslogin.commonB\x0cOsLoginProtoZ4cloud.google.com/go/oslogin/common/commonpb;commonpb\xaa\x02\x1bGoogle.Cloud.OsLogin.Common\xca\x02\x1bGoogle\\Cloud\\OsLogin\\Common\xea\x02\x1eGoogle::Cloud::OsLogin::Common\xeaA+\n\x1boslogin.googleapis.com/User\x12\x0cusers/{user}'
    _globals['_POSIXACCOUNT'].fields_by_name['account_id']._loaded_options = None
    _globals['_POSIXACCOUNT'].fields_by_name['account_id']._serialized_options = b'\xe0A\x03'
    _globals['_POSIXACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_POSIXACCOUNT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_POSIXACCOUNT']._loaded_options = None
    _globals['_POSIXACCOUNT']._serialized_options = b'\xeaAF\n#oslogin.googleapis.com/PosixAccount\x12\x1fusers/{user}/projects/{project}'
    _globals['_SSHPUBLICKEY'].fields_by_name['fingerprint']._loaded_options = None
    _globals['_SSHPUBLICKEY'].fields_by_name['fingerprint']._serialized_options = b'\xe0A\x03'
    _globals['_SSHPUBLICKEY'].fields_by_name['name']._loaded_options = None
    _globals['_SSHPUBLICKEY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SSHPUBLICKEY']._loaded_options = None
    _globals['_SSHPUBLICKEY']._serialized_options = b'\xeaAO\n#oslogin.googleapis.com/SshPublicKey\x12(users/{user}/sshPublicKeys/{fingerprint}'
    _globals['_OPERATINGSYSTEMTYPE']._serialized_start = 673
    _globals['_OPERATINGSYSTEMTYPE']._serialized_end = 757
    _globals['_POSIXACCOUNT']._serialized_start = 134
    _globals['_POSIXACCOUNT']._serialized_end = 482
    _globals['_SSHPUBLICKEY']._serialized_start = 485
    _globals['_SSHPUBLICKEY']._serialized_end = 671