"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v1/resource_policy_member.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/iam/v1/resource_policy_member.proto\x12\rgoogle.iam.v1\x1a\x1fgoogle/api/field_behavior.proto"e\n\x14ResourcePolicyMember\x12&\n\x19iam_policy_name_principal\x18\x01 \x01(\tB\x03\xe0A\x03\x12%\n\x18iam_policy_uid_principal\x18\x02 \x01(\tB\x03\xe0A\x03B\x87\x01\n\x11com.google.iam.v1B\x19ResourcePolicyMemberProtoP\x01Z)cloud.google.com/go/iam/apiv1/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V1\xca\x02\x13Google\\Cloud\\Iam\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v1.resource_policy_member_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x11com.google.iam.v1B\x19ResourcePolicyMemberProtoP\x01Z)cloud.google.com/go/iam/apiv1/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V1\xca\x02\x13Google\\Cloud\\Iam\\V1'
    _globals['_RESOURCEPOLICYMEMBER'].fields_by_name['iam_policy_name_principal']._loaded_options = None
    _globals['_RESOURCEPOLICYMEMBER'].fields_by_name['iam_policy_name_principal']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEPOLICYMEMBER'].fields_by_name['iam_policy_uid_principal']._loaded_options = None
    _globals['_RESOURCEPOLICYMEMBER'].fields_by_name['iam_policy_uid_principal']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEPOLICYMEMBER']._serialized_start = 94
    _globals['_RESOURCEPOLICYMEMBER']._serialized_end = 195