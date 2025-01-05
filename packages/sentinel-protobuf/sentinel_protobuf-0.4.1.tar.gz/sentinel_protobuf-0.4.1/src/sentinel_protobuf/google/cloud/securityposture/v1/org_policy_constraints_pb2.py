"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securityposture/v1/org_policy_constraints.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.securityposture.v1 import org_policy_config_pb2 as google_dot_cloud_dot_securityposture_dot_v1_dot_org__policy__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/securityposture/v1/org_policy_constraints.proto\x12\x1fgoogle.cloud.securityposture.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a7google/cloud/securityposture/v1/org_policy_config.proto"\x80\x01\n\x13OrgPolicyConstraint\x12!\n\x14canned_constraint_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12F\n\x0cpolicy_rules\x18\x02 \x03(\x0b2+.google.cloud.securityposture.v1.PolicyRuleB\x03\xe0A\x02"\xb6\x01\n\x19OrgPolicyConstraintCustom\x12Q\n\x11custom_constraint\x18\x01 \x01(\x0b21.google.cloud.securityposture.v1.CustomConstraintB\x03\xe0A\x02\x12F\n\x0cpolicy_rules\x18\x02 \x03(\x0b2+.google.cloud.securityposture.v1.PolicyRuleB\x03\xe0A\x02B\x91\x01\n#com.google.cloud.securityposture.v1B\x19OrgPolicyConstraintsProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securityposture.v1.org_policy_constraints_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.securityposture.v1B\x19OrgPolicyConstraintsProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepb'
    _globals['_ORGPOLICYCONSTRAINT'].fields_by_name['canned_constraint_id']._loaded_options = None
    _globals['_ORGPOLICYCONSTRAINT'].fields_by_name['canned_constraint_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORGPOLICYCONSTRAINT'].fields_by_name['policy_rules']._loaded_options = None
    _globals['_ORGPOLICYCONSTRAINT'].fields_by_name['policy_rules']._serialized_options = b'\xe0A\x02'
    _globals['_ORGPOLICYCONSTRAINTCUSTOM'].fields_by_name['custom_constraint']._loaded_options = None
    _globals['_ORGPOLICYCONSTRAINTCUSTOM'].fields_by_name['custom_constraint']._serialized_options = b'\xe0A\x02'
    _globals['_ORGPOLICYCONSTRAINTCUSTOM'].fields_by_name['policy_rules']._loaded_options = None
    _globals['_ORGPOLICYCONSTRAINTCUSTOM'].fields_by_name['policy_rules']._serialized_options = b'\xe0A\x02'
    _globals['_ORGPOLICYCONSTRAINT']._serialized_start = 188
    _globals['_ORGPOLICYCONSTRAINT']._serialized_end = 316
    _globals['_ORGPOLICYCONSTRAINTCUSTOM']._serialized_start = 319
    _globals['_ORGPOLICYCONSTRAINTCUSTOM']._serialized_end = 501