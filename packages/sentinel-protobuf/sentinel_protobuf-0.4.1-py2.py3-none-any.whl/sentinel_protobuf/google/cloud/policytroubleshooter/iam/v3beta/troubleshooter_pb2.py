"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/policytroubleshooter/iam/v3beta/troubleshooter.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from ......google.iam.v2 import policy_pb2 as google_dot_iam_dot_v2_dot_policy__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ......google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/policytroubleshooter/iam/v3beta/troubleshooter.proto\x12,google.cloud.policytroubleshooter.iam.v3beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1agoogle/iam/v2/policy.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/expr.proto"o\n\x1cTroubleshootIamPolicyRequest\x12O\n\x0caccess_tuple\x18\x01 \x01(\x0b29.google.cloud.policytroubleshooter.iam.v3beta.AccessTuple"\xc7\x04\n\x1dTroubleshootIamPolicyResponse\x12|\n\x14overall_access_state\x18\x01 \x01(\x0e2^.google.cloud.policytroubleshooter.iam.v3beta.TroubleshootIamPolicyResponse.OverallAccessState\x12O\n\x0caccess_tuple\x18\x02 \x01(\x0b29.google.cloud.policytroubleshooter.iam.v3beta.AccessTuple\x12f\n\x18allow_policy_explanation\x18\x03 \x01(\x0b2D.google.cloud.policytroubleshooter.iam.v3beta.AllowPolicyExplanation\x12d\n\x17deny_policy_explanation\x18\x04 \x01(\x0b2C.google.cloud.policytroubleshooter.iam.v3beta.DenyPolicyExplanation"\x88\x01\n\x12OverallAccessState\x12$\n OVERALL_ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nCAN_ACCESS\x10\x01\x12\x11\n\rCANNOT_ACCESS\x10\x02\x12\x10\n\x0cUNKNOWN_INFO\x10\x03\x12\x17\n\x13UNKNOWN_CONDITIONAL\x10\x04"\xdd\x01\n\x0bAccessTuple\x12\x16\n\tprincipal\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12full_resource_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\npermission\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fpermission_fqdn\x18\x04 \x01(\tB\x03\xe0A\x03\x12^\n\x11condition_context\x18\x05 \x01(\x0b2>.google.cloud.policytroubleshooter.iam.v3beta.ConditionContextB\x03\xe0A\x01"\xdf\x05\n\x10ConditionContext\x12Y\n\x08resource\x18\x01 \x01(\x0b2G.google.cloud.policytroubleshooter.iam.v3beta.ConditionContext.Resource\x12X\n\x0bdestination\x18\x02 \x01(\x0b2C.google.cloud.policytroubleshooter.iam.v3beta.ConditionContext.Peer\x12W\n\x07request\x18\x03 \x01(\x0b2F.google.cloud.policytroubleshooter.iam.v3beta.ConditionContext.Request\x12h\n\x0eeffective_tags\x18\x04 \x03(\x0b2K.google.cloud.policytroubleshooter.iam.v3beta.ConditionContext.EffectiveTagB\x03\xe0A\x03\x1a7\n\x08Resource\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x1a \n\x04Peer\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x1a@\n\x07Request\x125\n\x0creceive_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x1a\xb5\x01\n\x0cEffectiveTag\x12\x16\n\ttag_value\x18\x01 \x01(\tB\x03\xe0A\x03\x12!\n\x14namespaced_tag_value\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07tag_key\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12namespaced_tag_key\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x13tag_key_parent_name\x18\x06 \x01(\t\x12\x16\n\tinherited\x18\x05 \x01(\x08B\x03\xe0A\x03"\xa9\x02\n\x16AllowPolicyExplanation\x12Z\n\x12allow_access_state\x18\x01 \x01(\x0e2>.google.cloud.policytroubleshooter.iam.v3beta.AllowAccessState\x12^\n\x12explained_policies\x18\x02 \x03(\x0b2B.google.cloud.policytroubleshooter.iam.v3beta.ExplainedAllowPolicy\x12S\n\trelevance\x18\x03 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance"\xf4\x02\n\x14ExplainedAllowPolicy\x12_\n\x12allow_access_state\x18\x01 \x01(\x0e2>.google.cloud.policytroubleshooter.iam.v3beta.AllowAccessStateB\x03\xe0A\x02\x12\x1a\n\x12full_resource_name\x18\x02 \x01(\t\x12c\n\x14binding_explanations\x18\x03 \x03(\x0b2E.google.cloud.policytroubleshooter.iam.v3beta.AllowBindingExplanation\x12S\n\trelevance\x18\x04 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x12%\n\x06policy\x18\x05 \x01(\x0b2\x15.google.iam.v1.Policy"\xfc\x08\n\x17AllowBindingExplanation\x12_\n\x12allow_access_state\x18\x01 \x01(\x0e2>.google.cloud.policytroubleshooter.iam.v3beta.AllowAccessStateB\x03\xe0A\x02\x12\x0c\n\x04role\x18\x02 \x01(\t\x12c\n\x0frole_permission\x18\x03 \x01(\x0e2J.google.cloud.policytroubleshooter.iam.v3beta.RolePermissionInclusionState\x12c\n\x19role_permission_relevance\x18\x04 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x12{\n\x13combined_membership\x18\x05 \x01(\x0b2^.google.cloud.policytroubleshooter.iam.v3beta.AllowBindingExplanation.AnnotatedAllowMembership\x12k\n\x0bmemberships\x18\x06 \x03(\x0b2V.google.cloud.policytroubleshooter.iam.v3beta.AllowBindingExplanation.MembershipsEntry\x12S\n\trelevance\x18\x07 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x12$\n\tcondition\x18\x08 \x01(\x0b2\x11.google.type.Expr\x12a\n\x15condition_explanation\x18\t \x01(\x0b2B.google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation\x1a\xca\x01\n\x18AnnotatedAllowMembership\x12Y\n\nmembership\x18\x01 \x01(\x0e2E.google.cloud.policytroubleshooter.iam.v3beta.MembershipMatchingState\x12S\n\trelevance\x18\x02 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x1a\x92\x01\n\x10MembershipsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12m\n\x05value\x18\x02 \x01(\x0b2^.google.cloud.policytroubleshooter.iam.v3beta.AllowBindingExplanation.AnnotatedAllowMembership:\x028\x01"\xc5\x02\n\x15DenyPolicyExplanation\x12X\n\x11deny_access_state\x18\x01 \x01(\x0e2=.google.cloud.policytroubleshooter.iam.v3beta.DenyAccessState\x12`\n\x13explained_resources\x18\x02 \x03(\x0b2C.google.cloud.policytroubleshooter.iam.v3beta.ExplainedDenyResource\x12S\n\trelevance\x18\x03 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x12\x1b\n\x13permission_deniable\x18\x04 \x01(\x08"\xc6\x02\n\x15ExplainedDenyResource\x12]\n\x11deny_access_state\x18\x01 \x01(\x0e2=.google.cloud.policytroubleshooter.iam.v3beta.DenyAccessStateB\x03\xe0A\x02\x12\x1a\n\x12full_resource_name\x18\x02 \x01(\t\x12]\n\x12explained_policies\x18\x03 \x03(\x0b2A.google.cloud.policytroubleshooter.iam.v3beta.ExplainedDenyPolicy\x12S\n\trelevance\x18\x04 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance"\xce\x02\n\x13ExplainedDenyPolicy\x12]\n\x11deny_access_state\x18\x01 \x01(\x0e2=.google.cloud.policytroubleshooter.iam.v3beta.DenyAccessStateB\x03\xe0A\x02\x12%\n\x06policy\x18\x02 \x01(\x0b2\x15.google.iam.v2.Policy\x12\\\n\x11rule_explanations\x18\x03 \x03(\x0b2A.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation\x12S\n\trelevance\x18\x04 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance"\xf7\x12\n\x13DenyRuleExplanation\x12]\n\x11deny_access_state\x18\x01 \x01(\x0e2=.google.cloud.policytroubleshooter.iam.v3beta.DenyAccessStateB\x03\xe0A\x02\x12\x81\x01\n\x1acombined_denied_permission\x18\x02 \x01(\x0b2].google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedPermissionMatching\x12t\n\x12denied_permissions\x18\x03 \x03(\x0b2X.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.DeniedPermissionsEntry\x12\x84\x01\n\x1dcombined_exception_permission\x18\x04 \x01(\x0b2].google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedPermissionMatching\x12z\n\x15exception_permissions\x18\x05 \x03(\x0b2[.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.ExceptionPermissionsEntry\x12\x83\x01\n\x19combined_denied_principal\x18\x06 \x01(\x0b2`.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedDenyPrincipalMatching\x12r\n\x11denied_principals\x18\x07 \x03(\x0b2W.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.DeniedPrincipalsEntry\x12\x86\x01\n\x1ccombined_exception_principal\x18\x08 \x01(\x0b2`.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedDenyPrincipalMatching\x12x\n\x14exception_principals\x18\t \x03(\x0b2Z.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.ExceptionPrincipalsEntry\x12S\n\trelevance\x18\n \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x12$\n\tcondition\x18\x0b \x01(\x0b2\x11.google.type.Expr\x12a\n\x15condition_explanation\x18\x0c \x01(\x0b2B.google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation\x1a\xe3\x01\n\x1bAnnotatedPermissionMatching\x12o\n\x19permission_matching_state\x18\x01 \x01(\x0e2L.google.cloud.policytroubleshooter.iam.v3beta.PermissionPatternMatchingState\x12S\n\trelevance\x18\x02 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x1a\xd0\x01\n\x1eAnnotatedDenyPrincipalMatching\x12Y\n\nmembership\x18\x01 \x01(\x0e2E.google.cloud.policytroubleshooter.iam.v3beta.MembershipMatchingState\x12S\n\trelevance\x18\x02 \x01(\x0e2@.google.cloud.policytroubleshooter.iam.v3beta.HeuristicRelevance\x1a\x97\x01\n\x16DeniedPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12l\n\x05value\x18\x02 \x01(\x0b2].google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedPermissionMatching:\x028\x01\x1a\x9a\x01\n\x19ExceptionPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12l\n\x05value\x18\x02 \x01(\x0b2].google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedPermissionMatching:\x028\x01\x1a\x99\x01\n\x15DeniedPrincipalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12o\n\x05value\x18\x02 \x01(\x0b2`.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedDenyPrincipalMatching:\x028\x01\x1a\x9c\x01\n\x18ExceptionPrincipalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12o\n\x05value\x18\x02 \x01(\x0b2`.google.cloud.policytroubleshooter.iam.v3beta.DenyRuleExplanation.AnnotatedDenyPrincipalMatching:\x028\x01"\xca\x02\n\x14ConditionExplanation\x12%\n\x05value\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12"\n\x06errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status\x12m\n\x11evaluation_states\x18\x02 \x03(\x0b2R.google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation.EvaluationState\x1ax\n\x0fEvaluationState\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03end\x18\x02 \x01(\x05\x12%\n\x05value\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12"\n\x06errors\x18\x04 \x03(\x0b2\x12.google.rpc.Status*\xcb\x01\n\x10AllowAccessState\x12"\n\x1eALLOW_ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aALLOW_ACCESS_STATE_GRANTED\x10\x01\x12"\n\x1eALLOW_ACCESS_STATE_NOT_GRANTED\x10\x02\x12*\n&ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL\x10\x03\x12#\n\x1fALLOW_ACCESS_STATE_UNKNOWN_INFO\x10\x04*\xc3\x01\n\x0fDenyAccessState\x12!\n\x1dDENY_ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18DENY_ACCESS_STATE_DENIED\x10\x01\x12 \n\x1cDENY_ACCESS_STATE_NOT_DENIED\x10\x02\x12)\n%DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL\x10\x03\x12"\n\x1eDENY_ACCESS_STATE_UNKNOWN_INFO\x10\x04*\xb1\x01\n\x1cRolePermissionInclusionState\x12/\n+ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18ROLE_PERMISSION_INCLUDED\x10\x01\x12 \n\x1cROLE_PERMISSION_NOT_INCLUDED\x10\x02\x12 \n\x1cROLE_PERMISSION_UNKNOWN_INFO\x10\x03*\x97\x01\n\x1ePermissionPatternMatchingState\x121\n-PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aPERMISSION_PATTERN_MATCHED\x10\x01\x12"\n\x1ePERMISSION_PATTERN_NOT_MATCHED\x10\x02*\xb9\x01\n\x17MembershipMatchingState\x12)\n%MEMBERSHIP_MATCHING_STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12MEMBERSHIP_MATCHED\x10\x01\x12\x1a\n\x16MEMBERSHIP_NOT_MATCHED\x10\x02\x12\x1b\n\x17MEMBERSHIP_UNKNOWN_INFO\x10\x03\x12"\n\x1eMEMBERSHIP_UNKNOWN_UNSUPPORTED\x10\x04*w\n\x12HeuristicRelevance\x12#\n\x1fHEURISTIC_RELEVANCE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aHEURISTIC_RELEVANCE_NORMAL\x10\x01\x12\x1c\n\x18HEURISTIC_RELEVANCE_HIGH\x10\x022\xc7\x02\n\x14PolicyTroubleshooter\x12\xd5\x01\n\x15TroubleshootIamPolicy\x12J.google.cloud.policytroubleshooter.iam.v3beta.TroubleshootIamPolicyRequest\x1aK.google.cloud.policytroubleshooter.iam.v3beta.TroubleshootIamPolicyResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/v3beta/iam:troubleshoot:\x01*\x1aW\xcaA#policytroubleshooter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x90\x01\n0com.google.cloud.policytroubleshooter.iam.v3betaB\x13TroubleshooterProtoP\x01ZBcloud.google.com/go/policytroubleshooter/iam/apiv3beta/iampb;iampb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.policytroubleshooter.iam.v3beta.troubleshooter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0com.google.cloud.policytroubleshooter.iam.v3betaB\x13TroubleshooterProtoP\x01ZBcloud.google.com/go/policytroubleshooter/iam/apiv3beta/iampb;iampb\xf8\x01\x01'
    _globals['_ACCESSTUPLE'].fields_by_name['principal']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['principal']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSTUPLE'].fields_by_name['full_resource_name']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['full_resource_name']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSTUPLE'].fields_by_name['permission']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['permission']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSTUPLE'].fields_by_name['permission_fqdn']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['permission_fqdn']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSTUPLE'].fields_by_name['condition_context']._loaded_options = None
    _globals['_ACCESSTUPLE'].fields_by_name['condition_context']._serialized_options = b'\xe0A\x01'
    _globals['_CONDITIONCONTEXT_REQUEST'].fields_by_name['receive_time']._loaded_options = None
    _globals['_CONDITIONCONTEXT_REQUEST'].fields_by_name['receive_time']._serialized_options = b'\xe0A\x01'
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['tag_value']._loaded_options = None
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['tag_value']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['namespaced_tag_value']._loaded_options = None
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['namespaced_tag_value']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['tag_key']._loaded_options = None
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['tag_key']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['namespaced_tag_key']._loaded_options = None
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['namespaced_tag_key']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['inherited']._loaded_options = None
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG'].fields_by_name['inherited']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITIONCONTEXT'].fields_by_name['effective_tags']._loaded_options = None
    _globals['_CONDITIONCONTEXT'].fields_by_name['effective_tags']._serialized_options = b'\xe0A\x03'
    _globals['_EXPLAINEDALLOWPOLICY'].fields_by_name['allow_access_state']._loaded_options = None
    _globals['_EXPLAINEDALLOWPOLICY'].fields_by_name['allow_access_state']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOWBINDINGEXPLANATION_MEMBERSHIPSENTRY']._loaded_options = None
    _globals['_ALLOWBINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_options = b'8\x01'
    _globals['_ALLOWBINDINGEXPLANATION'].fields_by_name['allow_access_state']._loaded_options = None
    _globals['_ALLOWBINDINGEXPLANATION'].fields_by_name['allow_access_state']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLAINEDDENYRESOURCE'].fields_by_name['deny_access_state']._loaded_options = None
    _globals['_EXPLAINEDDENYRESOURCE'].fields_by_name['deny_access_state']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLAINEDDENYPOLICY'].fields_by_name['deny_access_state']._loaded_options = None
    _globals['_EXPLAINEDDENYPOLICY'].fields_by_name['deny_access_state']._serialized_options = b'\xe0A\x02'
    _globals['_DENYRULEEXPLANATION_DENIEDPERMISSIONSENTRY']._loaded_options = None
    _globals['_DENYRULEEXPLANATION_DENIEDPERMISSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPERMISSIONSENTRY']._loaded_options = None
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPERMISSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_DENYRULEEXPLANATION_DENIEDPRINCIPALSENTRY']._loaded_options = None
    _globals['_DENYRULEEXPLANATION_DENIEDPRINCIPALSENTRY']._serialized_options = b'8\x01'
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPRINCIPALSENTRY']._loaded_options = None
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPRINCIPALSENTRY']._serialized_options = b'8\x01'
    _globals['_DENYRULEEXPLANATION'].fields_by_name['deny_access_state']._loaded_options = None
    _globals['_DENYRULEEXPLANATION'].fields_by_name['deny_access_state']._serialized_options = b'\xe0A\x02'
    _globals['_POLICYTROUBLESHOOTER']._loaded_options = None
    _globals['_POLICYTROUBLESHOOTER']._serialized_options = b'\xcaA#policytroubleshooter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICYTROUBLESHOOTER'].methods_by_name['TroubleshootIamPolicy']._loaded_options = None
    _globals['_POLICYTROUBLESHOOTER'].methods_by_name['TroubleshootIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/v3beta/iam:troubleshoot:\x01*'
    _globals['_ALLOWACCESSSTATE']._serialized_start = 7612
    _globals['_ALLOWACCESSSTATE']._serialized_end = 7815
    _globals['_DENYACCESSSTATE']._serialized_start = 7818
    _globals['_DENYACCESSSTATE']._serialized_end = 8013
    _globals['_ROLEPERMISSIONINCLUSIONSTATE']._serialized_start = 8016
    _globals['_ROLEPERMISSIONINCLUSIONSTATE']._serialized_end = 8193
    _globals['_PERMISSIONPATTERNMATCHINGSTATE']._serialized_start = 8196
    _globals['_PERMISSIONPATTERNMATCHINGSTATE']._serialized_end = 8347
    _globals['_MEMBERSHIPMATCHINGSTATE']._serialized_start = 8350
    _globals['_MEMBERSHIPMATCHINGSTATE']._serialized_end = 8535
    _globals['_HEURISTICRELEVANCE']._serialized_start = 8537
    _globals['_HEURISTICRELEVANCE']._serialized_end = 8656
    _globals['_TROUBLESHOOTIAMPOLICYREQUEST']._serialized_start = 371
    _globals['_TROUBLESHOOTIAMPOLICYREQUEST']._serialized_end = 482
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE']._serialized_start = 485
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE']._serialized_end = 1068
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE_OVERALLACCESSSTATE']._serialized_start = 932
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE_OVERALLACCESSSTATE']._serialized_end = 1068
    _globals['_ACCESSTUPLE']._serialized_start = 1071
    _globals['_ACCESSTUPLE']._serialized_end = 1292
    _globals['_CONDITIONCONTEXT']._serialized_start = 1295
    _globals['_CONDITIONCONTEXT']._serialized_end = 2030
    _globals['_CONDITIONCONTEXT_RESOURCE']._serialized_start = 1691
    _globals['_CONDITIONCONTEXT_RESOURCE']._serialized_end = 1746
    _globals['_CONDITIONCONTEXT_PEER']._serialized_start = 1748
    _globals['_CONDITIONCONTEXT_PEER']._serialized_end = 1780
    _globals['_CONDITIONCONTEXT_REQUEST']._serialized_start = 1782
    _globals['_CONDITIONCONTEXT_REQUEST']._serialized_end = 1846
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG']._serialized_start = 1849
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG']._serialized_end = 2030
    _globals['_ALLOWPOLICYEXPLANATION']._serialized_start = 2033
    _globals['_ALLOWPOLICYEXPLANATION']._serialized_end = 2330
    _globals['_EXPLAINEDALLOWPOLICY']._serialized_start = 2333
    _globals['_EXPLAINEDALLOWPOLICY']._serialized_end = 2705
    _globals['_ALLOWBINDINGEXPLANATION']._serialized_start = 2708
    _globals['_ALLOWBINDINGEXPLANATION']._serialized_end = 3856
    _globals['_ALLOWBINDINGEXPLANATION_ANNOTATEDALLOWMEMBERSHIP']._serialized_start = 3505
    _globals['_ALLOWBINDINGEXPLANATION_ANNOTATEDALLOWMEMBERSHIP']._serialized_end = 3707
    _globals['_ALLOWBINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_start = 3710
    _globals['_ALLOWBINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_end = 3856
    _globals['_DENYPOLICYEXPLANATION']._serialized_start = 3859
    _globals['_DENYPOLICYEXPLANATION']._serialized_end = 4184
    _globals['_EXPLAINEDDENYRESOURCE']._serialized_start = 4187
    _globals['_EXPLAINEDDENYRESOURCE']._serialized_end = 4513
    _globals['_EXPLAINEDDENYPOLICY']._serialized_start = 4516
    _globals['_EXPLAINEDDENYPOLICY']._serialized_end = 4850
    _globals['_DENYRULEEXPLANATION']._serialized_start = 4853
    _globals['_DENYRULEEXPLANATION']._serialized_end = 7276
    _globals['_DENYRULEEXPLANATION_ANNOTATEDPERMISSIONMATCHING']._serialized_start = 6212
    _globals['_DENYRULEEXPLANATION_ANNOTATEDPERMISSIONMATCHING']._serialized_end = 6439
    _globals['_DENYRULEEXPLANATION_ANNOTATEDDENYPRINCIPALMATCHING']._serialized_start = 6442
    _globals['_DENYRULEEXPLANATION_ANNOTATEDDENYPRINCIPALMATCHING']._serialized_end = 6650
    _globals['_DENYRULEEXPLANATION_DENIEDPERMISSIONSENTRY']._serialized_start = 6653
    _globals['_DENYRULEEXPLANATION_DENIEDPERMISSIONSENTRY']._serialized_end = 6804
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPERMISSIONSENTRY']._serialized_start = 6807
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPERMISSIONSENTRY']._serialized_end = 6961
    _globals['_DENYRULEEXPLANATION_DENIEDPRINCIPALSENTRY']._serialized_start = 6964
    _globals['_DENYRULEEXPLANATION_DENIEDPRINCIPALSENTRY']._serialized_end = 7117
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPRINCIPALSENTRY']._serialized_start = 7120
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPRINCIPALSENTRY']._serialized_end = 7276
    _globals['_CONDITIONEXPLANATION']._serialized_start = 7279
    _globals['_CONDITIONEXPLANATION']._serialized_end = 7609
    _globals['_CONDITIONEXPLANATION_EVALUATIONSTATE']._serialized_start = 7489
    _globals['_CONDITIONEXPLANATION_EVALUATIONSTATE']._serialized_end = 7609
    _globals['_POLICYTROUBLESHOOTER']._serialized_start = 8659
    _globals['_POLICYTROUBLESHOOTER']._serialized_end = 8986