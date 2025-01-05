"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/orgpolicy/v1/orgpolicy.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/orgpolicy/v1/orgpolicy.proto\x12\x19google.cloud.orgpolicy.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x05\n\x06Policy\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x12\n\nconstraint\x18\x02 \x01(\t\x12\x0c\n\x04etag\x18\x03 \x01(\x0c\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\x0blist_policy\x18\x05 \x01(\x0b2,.google.cloud.orgpolicy.v1.Policy.ListPolicyH\x00\x12I\n\x0eboolean_policy\x18\x06 \x01(\x0b2/.google.cloud.orgpolicy.v1.Policy.BooleanPolicyH\x00\x12K\n\x0frestore_default\x18\x07 \x01(\x0b20.google.cloud.orgpolicy.v1.Policy.RestoreDefaultH\x00\x1a\xfb\x01\n\nListPolicy\x12\x16\n\x0eallowed_values\x18\x01 \x03(\t\x12\x15\n\rdenied_values\x18\x02 \x03(\t\x12J\n\nall_values\x18\x03 \x01(\x0e26.google.cloud.orgpolicy.v1.Policy.ListPolicy.AllValues\x12\x17\n\x0fsuggested_value\x18\x04 \x01(\t\x12\x1b\n\x13inherit_from_parent\x18\x05 \x01(\x08"<\n\tAllValues\x12\x1a\n\x16ALL_VALUES_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02\x1a!\n\rBooleanPolicy\x12\x10\n\x08enforced\x18\x01 \x01(\x08\x1a\x10\n\x0eRestoreDefaultB\r\n\x0bpolicy_typeB\xc5\x01\n\x1dcom.google.cloud.orgpolicy.v1B\x0eOrgPolicyProtoP\x01Z;cloud.google.com/go/orgpolicy/apiv1/orgpolicypb;orgpolicypb\xaa\x02\x19Google.Cloud.OrgPolicy.V1\xca\x02\x19Google\\Cloud\\OrgPolicy\\V1\xea\x02\x1cGoogle::Cloud::OrgPolicy::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.orgpolicy.v1.orgpolicy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.orgpolicy.v1B\x0eOrgPolicyProtoP\x01Z;cloud.google.com/go/orgpolicy/apiv1/orgpolicypb;orgpolicypb\xaa\x02\x19Google.Cloud.OrgPolicy.V1\xca\x02\x19Google\\Cloud\\OrgPolicy\\V1\xea\x02\x1cGoogle::Cloud::OrgPolicy::V1'
    _globals['_POLICY']._serialized_start = 106
    _globals['_POLICY']._serialized_end = 757
    _globals['_POLICY_LISTPOLICY']._serialized_start = 438
    _globals['_POLICY_LISTPOLICY']._serialized_end = 689
    _globals['_POLICY_LISTPOLICY_ALLVALUES']._serialized_start = 629
    _globals['_POLICY_LISTPOLICY_ALLVALUES']._serialized_end = 689
    _globals['_POLICY_BOOLEANPOLICY']._serialized_start = 691
    _globals['_POLICY_BOOLEANPOLICY']._serialized_end = 724
    _globals['_POLICY_RESTOREDEFAULT']._serialized_start = 726
    _globals['_POLICY_RESTOREDEFAULT']._serialized_end = 742