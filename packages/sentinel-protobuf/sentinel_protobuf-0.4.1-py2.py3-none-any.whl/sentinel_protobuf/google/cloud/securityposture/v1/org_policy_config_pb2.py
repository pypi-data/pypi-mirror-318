"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securityposture/v1/org_policy_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/securityposture/v1/org_policy_config.proto\x12\x1fgoogle.cloud.securityposture.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/expr.proto"\x81\x02\n\nPolicyRule\x12J\n\x06values\x18\x01 \x01(\x0b28.google.cloud.securityposture.v1.PolicyRule.StringValuesH\x00\x12\x13\n\tallow_all\x18\x02 \x01(\x08H\x00\x12\x12\n\x08deny_all\x18\x03 \x01(\x08H\x00\x12\x11\n\x07enforce\x18\x04 \x01(\x08H\x00\x12$\n\tcondition\x18\x05 \x01(\x0b2\x11.google.type.Expr\x1a=\n\x0cStringValues\x12\x16\n\x0eallowed_values\x18\x01 \x03(\t\x12\x15\n\rdenied_values\x18\x02 \x03(\tB\x06\n\x04kind"\xec\x03\n\x10CustomConstraint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x1b\n\x0eresource_types\x18\x02 \x03(\tB\x03\xe0A\x05\x12R\n\x0cmethod_types\x18\x03 \x03(\x0e2<.google.cloud.securityposture.v1.CustomConstraint.MethodType\x12\x11\n\tcondition\x18\x04 \x01(\t\x12Q\n\x0baction_type\x18\x05 \x01(\x0e2<.google.cloud.securityposture.v1.CustomConstraint.ActionType\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"M\n\nMethodType\x12\x1b\n\x17METHOD_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06DELETE\x10\x03">\n\nActionType\x12\x1b\n\x17ACTION_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02B\x8c\x01\n#com.google.cloud.securityposture.v1B\x14OrgPolicyConfigProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securityposture.v1.org_policy_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.securityposture.v1B\x14OrgPolicyConfigProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepb'
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['resource_types']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['resource_types']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['update_time']._loaded_options = None
    _globals['_CUSTOMCONSTRAINT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICYRULE']._serialized_start = 183
    _globals['_POLICYRULE']._serialized_end = 440
    _globals['_POLICYRULE_STRINGVALUES']._serialized_start = 371
    _globals['_POLICYRULE_STRINGVALUES']._serialized_end = 432
    _globals['_CUSTOMCONSTRAINT']._serialized_start = 443
    _globals['_CUSTOMCONSTRAINT']._serialized_end = 935
    _globals['_CUSTOMCONSTRAINT_METHODTYPE']._serialized_start = 794
    _globals['_CUSTOMCONSTRAINT_METHODTYPE']._serialized_end = 871
    _globals['_CUSTOMCONSTRAINT_ACTIONTYPE']._serialized_start = 873
    _globals['_CUSTOMCONSTRAINT_ACTIONTYPE']._serialized_end = 935