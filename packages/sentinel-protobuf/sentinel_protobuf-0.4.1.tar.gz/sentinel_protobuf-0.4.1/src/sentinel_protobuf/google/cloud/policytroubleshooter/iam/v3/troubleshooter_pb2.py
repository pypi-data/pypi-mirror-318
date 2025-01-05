"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/policytroubleshooter/iam/v3/troubleshooter.proto')
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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/policytroubleshooter/iam/v3/troubleshooter.proto\x12(google.cloud.policytroubleshooter.iam.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1agoogle/iam/v2/policy.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/expr.proto"k\n\x1cTroubleshootIamPolicyRequest\x12K\n\x0caccess_tuple\x18\x01 \x01(\x0b25.google.cloud.policytroubleshooter.iam.v3.AccessTuple"\xb7\x04\n\x1dTroubleshootIamPolicyResponse\x12x\n\x14overall_access_state\x18\x01 \x01(\x0e2Z.google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse.OverallAccessState\x12K\n\x0caccess_tuple\x18\x02 \x01(\x0b25.google.cloud.policytroubleshooter.iam.v3.AccessTuple\x12b\n\x18allow_policy_explanation\x18\x03 \x01(\x0b2@.google.cloud.policytroubleshooter.iam.v3.AllowPolicyExplanation\x12`\n\x17deny_policy_explanation\x18\x04 \x01(\x0b2?.google.cloud.policytroubleshooter.iam.v3.DenyPolicyExplanation"\x88\x01\n\x12OverallAccessState\x12$\n OVERALL_ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nCAN_ACCESS\x10\x01\x12\x11\n\rCANNOT_ACCESS\x10\x02\x12\x10\n\x0cUNKNOWN_INFO\x10\x03\x12\x17\n\x13UNKNOWN_CONDITIONAL\x10\x04"\xd9\x01\n\x0bAccessTuple\x12\x16\n\tprincipal\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12full_resource_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\npermission\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fpermission_fqdn\x18\x04 \x01(\tB\x03\xe0A\x03\x12Z\n\x11condition_context\x18\x05 \x01(\x0b2:.google.cloud.policytroubleshooter.iam.v3.ConditionContextB\x03\xe0A\x01"\xcf\x05\n\x10ConditionContext\x12U\n\x08resource\x18\x01 \x01(\x0b2C.google.cloud.policytroubleshooter.iam.v3.ConditionContext.Resource\x12T\n\x0bdestination\x18\x02 \x01(\x0b2?.google.cloud.policytroubleshooter.iam.v3.ConditionContext.Peer\x12S\n\x07request\x18\x03 \x01(\x0b2B.google.cloud.policytroubleshooter.iam.v3.ConditionContext.Request\x12d\n\x0eeffective_tags\x18\x04 \x03(\x0b2G.google.cloud.policytroubleshooter.iam.v3.ConditionContext.EffectiveTagB\x03\xe0A\x03\x1a7\n\x08Resource\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x1a \n\x04Peer\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x1a@\n\x07Request\x125\n\x0creceive_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x1a\xb5\x01\n\x0cEffectiveTag\x12\x16\n\ttag_value\x18\x01 \x01(\tB\x03\xe0A\x03\x12!\n\x14namespaced_tag_value\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07tag_key\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12namespaced_tag_key\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x13tag_key_parent_name\x18\x06 \x01(\t\x12\x16\n\tinherited\x18\x05 \x01(\x08B\x03\xe0A\x03"\x9d\x02\n\x16AllowPolicyExplanation\x12V\n\x12allow_access_state\x18\x01 \x01(\x0e2:.google.cloud.policytroubleshooter.iam.v3.AllowAccessState\x12Z\n\x12explained_policies\x18\x02 \x03(\x0b2>.google.cloud.policytroubleshooter.iam.v3.ExplainedAllowPolicy\x12O\n\trelevance\x18\x03 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance"\xe8\x02\n\x14ExplainedAllowPolicy\x12[\n\x12allow_access_state\x18\x01 \x01(\x0e2:.google.cloud.policytroubleshooter.iam.v3.AllowAccessStateB\x03\xe0A\x02\x12\x1a\n\x12full_resource_name\x18\x02 \x01(\t\x12_\n\x14binding_explanations\x18\x03 \x03(\x0b2A.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation\x12O\n\trelevance\x18\x04 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x12%\n\x06policy\x18\x05 \x01(\x0b2\x15.google.iam.v1.Policy"\xd4\x08\n\x17AllowBindingExplanation\x12[\n\x12allow_access_state\x18\x01 \x01(\x0e2:.google.cloud.policytroubleshooter.iam.v3.AllowAccessStateB\x03\xe0A\x02\x12\x0c\n\x04role\x18\x02 \x01(\t\x12_\n\x0frole_permission\x18\x03 \x01(\x0e2F.google.cloud.policytroubleshooter.iam.v3.RolePermissionInclusionState\x12_\n\x19role_permission_relevance\x18\x04 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x12w\n\x13combined_membership\x18\x05 \x01(\x0b2Z.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership\x12g\n\x0bmemberships\x18\x06 \x03(\x0b2R.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.MembershipsEntry\x12O\n\trelevance\x18\x07 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x12$\n\tcondition\x18\x08 \x01(\x0b2\x11.google.type.Expr\x12]\n\x15condition_explanation\x18\t \x01(\x0b2>.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation\x1a\xc2\x01\n\x18AnnotatedAllowMembership\x12U\n\nmembership\x18\x01 \x01(\x0e2A.google.cloud.policytroubleshooter.iam.v3.MembershipMatchingState\x12O\n\trelevance\x18\x02 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x1a\x8e\x01\n\x10MembershipsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12i\n\x05value\x18\x02 \x01(\x0b2Z.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership:\x028\x01"\xb9\x02\n\x15DenyPolicyExplanation\x12T\n\x11deny_access_state\x18\x01 \x01(\x0e29.google.cloud.policytroubleshooter.iam.v3.DenyAccessState\x12\\\n\x13explained_resources\x18\x02 \x03(\x0b2?.google.cloud.policytroubleshooter.iam.v3.ExplainedDenyResource\x12O\n\trelevance\x18\x03 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x12\x1b\n\x13permission_deniable\x18\x04 \x01(\x08"\xba\x02\n\x15ExplainedDenyResource\x12Y\n\x11deny_access_state\x18\x01 \x01(\x0e29.google.cloud.policytroubleshooter.iam.v3.DenyAccessStateB\x03\xe0A\x02\x12\x1a\n\x12full_resource_name\x18\x02 \x01(\t\x12Y\n\x12explained_policies\x18\x03 \x03(\x0b2=.google.cloud.policytroubleshooter.iam.v3.ExplainedDenyPolicy\x12O\n\trelevance\x18\x04 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance"\xc2\x02\n\x13ExplainedDenyPolicy\x12Y\n\x11deny_access_state\x18\x01 \x01(\x0e29.google.cloud.policytroubleshooter.iam.v3.DenyAccessStateB\x03\xe0A\x02\x12%\n\x06policy\x18\x02 \x01(\x0b2\x15.google.iam.v2.Policy\x12X\n\x11rule_explanations\x18\x03 \x03(\x0b2=.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation\x12O\n\trelevance\x18\x04 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance"\xa9\x12\n\x13DenyRuleExplanation\x12Y\n\x11deny_access_state\x18\x01 \x01(\x0e29.google.cloud.policytroubleshooter.iam.v3.DenyAccessStateB\x03\xe0A\x02\x12}\n\x1acombined_denied_permission\x18\x02 \x01(\x0b2Y.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching\x12p\n\x12denied_permissions\x18\x03 \x03(\x0b2T.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.DeniedPermissionsEntry\x12\x80\x01\n\x1dcombined_exception_permission\x18\x04 \x01(\x0b2Y.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching\x12v\n\x15exception_permissions\x18\x05 \x03(\x0b2W.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.ExceptionPermissionsEntry\x12\x7f\n\x19combined_denied_principal\x18\x06 \x01(\x0b2\\.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching\x12n\n\x11denied_principals\x18\x07 \x03(\x0b2S.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.DeniedPrincipalsEntry\x12\x82\x01\n\x1ccombined_exception_principal\x18\x08 \x01(\x0b2\\.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching\x12t\n\x14exception_principals\x18\t \x03(\x0b2V.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.ExceptionPrincipalsEntry\x12O\n\trelevance\x18\n \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x12$\n\tcondition\x18\x0b \x01(\x0b2\x11.google.type.Expr\x12]\n\x15condition_explanation\x18\x0c \x01(\x0b2>.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation\x1a\xdb\x01\n\x1bAnnotatedPermissionMatching\x12k\n\x19permission_matching_state\x18\x01 \x01(\x0e2H.google.cloud.policytroubleshooter.iam.v3.PermissionPatternMatchingState\x12O\n\trelevance\x18\x02 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x1a\xc8\x01\n\x1eAnnotatedDenyPrincipalMatching\x12U\n\nmembership\x18\x01 \x01(\x0e2A.google.cloud.policytroubleshooter.iam.v3.MembershipMatchingState\x12O\n\trelevance\x18\x02 \x01(\x0e2<.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance\x1a\x93\x01\n\x16DeniedPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12h\n\x05value\x18\x02 \x01(\x0b2Y.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching:\x028\x01\x1a\x96\x01\n\x19ExceptionPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12h\n\x05value\x18\x02 \x01(\x0b2Y.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedPermissionMatching:\x028\x01\x1a\x95\x01\n\x15DeniedPrincipalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12k\n\x05value\x18\x02 \x01(\x0b2\\.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching:\x028\x01\x1a\x98\x01\n\x18ExceptionPrincipalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12k\n\x05value\x18\x02 \x01(\x0b2\\.google.cloud.policytroubleshooter.iam.v3.DenyRuleExplanation.AnnotatedDenyPrincipalMatching:\x028\x01"\xc6\x02\n\x14ConditionExplanation\x12%\n\x05value\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12"\n\x06errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status\x12i\n\x11evaluation_states\x18\x02 \x03(\x0b2N.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation.EvaluationState\x1ax\n\x0fEvaluationState\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03end\x18\x02 \x01(\x05\x12%\n\x05value\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12"\n\x06errors\x18\x04 \x03(\x0b2\x12.google.rpc.Status*\xcb\x01\n\x10AllowAccessState\x12"\n\x1eALLOW_ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aALLOW_ACCESS_STATE_GRANTED\x10\x01\x12"\n\x1eALLOW_ACCESS_STATE_NOT_GRANTED\x10\x02\x12*\n&ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL\x10\x03\x12#\n\x1fALLOW_ACCESS_STATE_UNKNOWN_INFO\x10\x04*\xc3\x01\n\x0fDenyAccessState\x12!\n\x1dDENY_ACCESS_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18DENY_ACCESS_STATE_DENIED\x10\x01\x12 \n\x1cDENY_ACCESS_STATE_NOT_DENIED\x10\x02\x12)\n%DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL\x10\x03\x12"\n\x1eDENY_ACCESS_STATE_UNKNOWN_INFO\x10\x04*\xb1\x01\n\x1cRolePermissionInclusionState\x12/\n+ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18ROLE_PERMISSION_INCLUDED\x10\x01\x12 \n\x1cROLE_PERMISSION_NOT_INCLUDED\x10\x02\x12 \n\x1cROLE_PERMISSION_UNKNOWN_INFO\x10\x03*\x97\x01\n\x1ePermissionPatternMatchingState\x121\n-PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aPERMISSION_PATTERN_MATCHED\x10\x01\x12"\n\x1ePERMISSION_PATTERN_NOT_MATCHED\x10\x02*\xb9\x01\n\x17MembershipMatchingState\x12)\n%MEMBERSHIP_MATCHING_STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12MEMBERSHIP_MATCHED\x10\x01\x12\x1a\n\x16MEMBERSHIP_NOT_MATCHED\x10\x02\x12\x1b\n\x17MEMBERSHIP_UNKNOWN_INFO\x10\x03\x12"\n\x1eMEMBERSHIP_UNKNOWN_UNSUPPORTED\x10\x04*w\n\x12HeuristicRelevance\x12#\n\x1fHEURISTIC_RELEVANCE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aHEURISTIC_RELEVANCE_NORMAL\x10\x01\x12\x1c\n\x18HEURISTIC_RELEVANCE_HIGH\x10\x022\xbb\x02\n\x14PolicyTroubleshooter\x12\xc9\x01\n\x15TroubleshootIamPolicy\x12F.google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyRequest\x1aG.google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/v3/iam:troubleshoot:\x01*\x1aW\xcaA#policytroubleshooter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8d\x02\n,com.google.cloud.policytroubleshooter.iam.v3B\x13TroubleshooterProtoP\x01Z>cloud.google.com/go/policytroubleshooter/iam/apiv3/iampb;iampb\xf8\x01\x01\xaa\x02(Google.Cloud.PolicyTroubleshooter.Iam.V3\xca\x02(Google\\Cloud\\PolicyTroubleshooter\\Iam\\V3\xea\x02,Google::Cloud::PolicyTroubleshooter::Iam::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.policytroubleshooter.iam.v3.troubleshooter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.policytroubleshooter.iam.v3B\x13TroubleshooterProtoP\x01Z>cloud.google.com/go/policytroubleshooter/iam/apiv3/iampb;iampb\xf8\x01\x01\xaa\x02(Google.Cloud.PolicyTroubleshooter.Iam.V3\xca\x02(Google\\Cloud\\PolicyTroubleshooter\\Iam\\V3\xea\x02,Google::Cloud::PolicyTroubleshooter::Iam::V3'
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
    _globals['_POLICYTROUBLESHOOTER'].methods_by_name['TroubleshootIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/v3/iam:troubleshoot:\x01*'
    _globals['_ALLOWACCESSSTATE']._serialized_start = 7382
    _globals['_ALLOWACCESSSTATE']._serialized_end = 7585
    _globals['_DENYACCESSSTATE']._serialized_start = 7588
    _globals['_DENYACCESSSTATE']._serialized_end = 7783
    _globals['_ROLEPERMISSIONINCLUSIONSTATE']._serialized_start = 7786
    _globals['_ROLEPERMISSIONINCLUSIONSTATE']._serialized_end = 7963
    _globals['_PERMISSIONPATTERNMATCHINGSTATE']._serialized_start = 7966
    _globals['_PERMISSIONPATTERNMATCHINGSTATE']._serialized_end = 8117
    _globals['_MEMBERSHIPMATCHINGSTATE']._serialized_start = 8120
    _globals['_MEMBERSHIPMATCHINGSTATE']._serialized_end = 8305
    _globals['_HEURISTICRELEVANCE']._serialized_start = 8307
    _globals['_HEURISTICRELEVANCE']._serialized_end = 8426
    _globals['_TROUBLESHOOTIAMPOLICYREQUEST']._serialized_start = 363
    _globals['_TROUBLESHOOTIAMPOLICYREQUEST']._serialized_end = 470
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE']._serialized_start = 473
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE']._serialized_end = 1040
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE_OVERALLACCESSSTATE']._serialized_start = 904
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE_OVERALLACCESSSTATE']._serialized_end = 1040
    _globals['_ACCESSTUPLE']._serialized_start = 1043
    _globals['_ACCESSTUPLE']._serialized_end = 1260
    _globals['_CONDITIONCONTEXT']._serialized_start = 1263
    _globals['_CONDITIONCONTEXT']._serialized_end = 1982
    _globals['_CONDITIONCONTEXT_RESOURCE']._serialized_start = 1643
    _globals['_CONDITIONCONTEXT_RESOURCE']._serialized_end = 1698
    _globals['_CONDITIONCONTEXT_PEER']._serialized_start = 1700
    _globals['_CONDITIONCONTEXT_PEER']._serialized_end = 1732
    _globals['_CONDITIONCONTEXT_REQUEST']._serialized_start = 1734
    _globals['_CONDITIONCONTEXT_REQUEST']._serialized_end = 1798
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG']._serialized_start = 1801
    _globals['_CONDITIONCONTEXT_EFFECTIVETAG']._serialized_end = 1982
    _globals['_ALLOWPOLICYEXPLANATION']._serialized_start = 1985
    _globals['_ALLOWPOLICYEXPLANATION']._serialized_end = 2270
    _globals['_EXPLAINEDALLOWPOLICY']._serialized_start = 2273
    _globals['_EXPLAINEDALLOWPOLICY']._serialized_end = 2633
    _globals['_ALLOWBINDINGEXPLANATION']._serialized_start = 2636
    _globals['_ALLOWBINDINGEXPLANATION']._serialized_end = 3744
    _globals['_ALLOWBINDINGEXPLANATION_ANNOTATEDALLOWMEMBERSHIP']._serialized_start = 3405
    _globals['_ALLOWBINDINGEXPLANATION_ANNOTATEDALLOWMEMBERSHIP']._serialized_end = 3599
    _globals['_ALLOWBINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_start = 3602
    _globals['_ALLOWBINDINGEXPLANATION_MEMBERSHIPSENTRY']._serialized_end = 3744
    _globals['_DENYPOLICYEXPLANATION']._serialized_start = 3747
    _globals['_DENYPOLICYEXPLANATION']._serialized_end = 4060
    _globals['_EXPLAINEDDENYRESOURCE']._serialized_start = 4063
    _globals['_EXPLAINEDDENYRESOURCE']._serialized_end = 4377
    _globals['_EXPLAINEDDENYPOLICY']._serialized_start = 4380
    _globals['_EXPLAINEDDENYPOLICY']._serialized_end = 4702
    _globals['_DENYRULEEXPLANATION']._serialized_start = 4705
    _globals['_DENYRULEEXPLANATION']._serialized_end = 7050
    _globals['_DENYRULEEXPLANATION_ANNOTATEDPERMISSIONMATCHING']._serialized_start = 6018
    _globals['_DENYRULEEXPLANATION_ANNOTATEDPERMISSIONMATCHING']._serialized_end = 6237
    _globals['_DENYRULEEXPLANATION_ANNOTATEDDENYPRINCIPALMATCHING']._serialized_start = 6240
    _globals['_DENYRULEEXPLANATION_ANNOTATEDDENYPRINCIPALMATCHING']._serialized_end = 6440
    _globals['_DENYRULEEXPLANATION_DENIEDPERMISSIONSENTRY']._serialized_start = 6443
    _globals['_DENYRULEEXPLANATION_DENIEDPERMISSIONSENTRY']._serialized_end = 6590
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPERMISSIONSENTRY']._serialized_start = 6593
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPERMISSIONSENTRY']._serialized_end = 6743
    _globals['_DENYRULEEXPLANATION_DENIEDPRINCIPALSENTRY']._serialized_start = 6746
    _globals['_DENYRULEEXPLANATION_DENIEDPRINCIPALSENTRY']._serialized_end = 6895
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPRINCIPALSENTRY']._serialized_start = 6898
    _globals['_DENYRULEEXPLANATION_EXCEPTIONPRINCIPALSENTRY']._serialized_end = 7050
    _globals['_CONDITIONEXPLANATION']._serialized_start = 7053
    _globals['_CONDITIONEXPLANATION']._serialized_end = 7379
    _globals['_CONDITIONEXPLANATION_EVALUATIONSTATE']._serialized_start = 7259
    _globals['_CONDITIONEXPLANATION_EVALUATIONSTATE']._serialized_end = 7379
    _globals['_POLICYTROUBLESHOOTER']._serialized_start = 8429
    _globals['_POLICYTROUBLESHOOTER']._serialized_end = 8744