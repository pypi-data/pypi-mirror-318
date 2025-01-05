"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/orgpolicy/v2/orgpolicy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.orgpolicy.v2 import constraint_pb2 as google_dot_cloud_dot_orgpolicy_dot_v2_dot_constraint__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/orgpolicy/v2/orgpolicy.proto\x12\x19google.cloud.orgpolicy.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/orgpolicy/v2/constraint.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/expr.proto"\x89\x03\n\x06Policy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x123\n\x04spec\x18\x02 \x01(\x0b2%.google.cloud.orgpolicy.v2.PolicySpec\x12E\n\talternate\x18\x03 \x01(\x0b2..google.cloud.orgpolicy.v2.AlternatePolicySpecB\x02\x18\x01\x12;\n\x0cdry_run_spec\x18\x04 \x01(\x0b2%.google.cloud.orgpolicy.v2.PolicySpec\x12\x11\n\x04etag\x18\x05 \x01(\tB\x03\xe0A\x01:\x9f\x01\xeaA\x9b\x01\n\x1forgpolicy.googleapis.com/Policy\x12$projects/{project}/policies/{policy}\x12"folders/{folder}/policies/{policy}\x12.organizations/{organization}/policies/{policy}"Z\n\x13AlternatePolicySpec\x12\x0e\n\x06launch\x18\x01 \x01(\t\x123\n\x04spec\x18\x02 \x01(\x0b2%.google.cloud.orgpolicy.v2.PolicySpec"\xc6\x03\n\nPolicySpec\x12\x0c\n\x04etag\x18\x01 \x01(\t\x124\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x05rules\x18\x03 \x03(\x0b20.google.cloud.orgpolicy.v2.PolicySpec.PolicyRule\x12\x1b\n\x13inherit_from_parent\x18\x04 \x01(\x08\x12\r\n\x05reset\x18\x05 \x01(\x08\x1a\x86\x02\n\nPolicyRule\x12O\n\x06values\x18\x01 \x01(\x0b2=.google.cloud.orgpolicy.v2.PolicySpec.PolicyRule.StringValuesH\x00\x12\x13\n\tallow_all\x18\x02 \x01(\x08H\x00\x12\x12\n\x08deny_all\x18\x03 \x01(\x08H\x00\x12\x11\n\x07enforce\x18\x04 \x01(\x08H\x00\x12$\n\tcondition\x18\x05 \x01(\x0b2\x11.google.type.Expr\x1a=\n\x0cStringValues\x12\x16\n\x0eallowed_values\x18\x01 \x03(\t\x12\x15\n\rdenied_values\x18\x02 \x03(\tB\x06\n\x04kind"|\n\x16ListConstraintsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#orgpolicy.googleapis.com/Constraint\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"n\n\x17ListConstraintsResponse\x12:\n\x0bconstraints\x18\x01 \x03(\x0b2%.google.cloud.orgpolicy.v2.Constraint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"u\n\x13ListPoliciesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1forgpolicy.googleapis.com/Policy\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"d\n\x14ListPoliciesResponse\x123\n\x08policies\x18\x01 \x03(\x0b2!.google.cloud.orgpolicy.v2.Policy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"I\n\x10GetPolicyRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1forgpolicy.googleapis.com/Policy"R\n\x19GetEffectivePolicyRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1forgpolicy.googleapis.com/Policy"\x86\x01\n\x13CreatePolicyRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1forgpolicy.googleapis.com/Policy\x126\n\x06policy\x18\x03 \x01(\x0b2!.google.cloud.orgpolicy.v2.PolicyB\x03\xe0A\x02"~\n\x13UpdatePolicyRequest\x126\n\x06policy\x18\x01 \x01(\x0b2!.google.cloud.orgpolicy.v2.PolicyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"_\n\x13DeletePolicyRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1forgpolicy.googleapis.com/Policy\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"\xaf\x01\n\x1dCreateCustomConstraintRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)orgpolicy.googleapis.com/CustomConstraint\x12K\n\x11custom_constraint\x18\x02 \x01(\x0b2+.google.cloud.orgpolicy.v2.CustomConstraintB\x03\xe0A\x02"]\n\x1aGetCustomConstraintRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)orgpolicy.googleapis.com/CustomConstraint"\x88\x01\n\x1cListCustomConstraintsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)orgpolicy.googleapis.com/CustomConstraint\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x81\x01\n\x1dListCustomConstraintsResponse\x12G\n\x12custom_constraints\x18\x01 \x03(\x0b2+.google.cloud.orgpolicy.v2.CustomConstraint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"l\n\x1dUpdateCustomConstraintRequest\x12K\n\x11custom_constraint\x18\x01 \x01(\x0b2+.google.cloud.orgpolicy.v2.CustomConstraintB\x03\xe0A\x02"`\n\x1dDeleteCustomConstraintRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)orgpolicy.googleapis.com/CustomConstraint2\xcd\x16\n\tOrgPolicy\x12\x81\x02\n\x0fListConstraints\x121.google.cloud.orgpolicy.v2.ListConstraintsRequest\x1a2.google.cloud.orgpolicy.v2.ListConstraintsResponse"\x86\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02w\x12#/v2/{parent=projects/*}/constraintsZ$\x12"/v2/{parent=folders/*}/constraintsZ*\x12(/v2/{parent=organizations/*}/constraints\x12\xee\x01\n\x0cListPolicies\x12..google.cloud.orgpolicy.v2.ListPoliciesRequest\x1a/.google.cloud.orgpolicy.v2.ListPoliciesResponse"}\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12 /v2/{parent=projects/*}/policiesZ!\x12\x1f/v2/{parent=folders/*}/policiesZ\'\x12%/v2/{parent=organizations/*}/policies\x12\xd8\x01\n\tGetPolicy\x12+.google.cloud.orgpolicy.v2.GetPolicyRequest\x1a!.google.cloud.orgpolicy.v2.Policy"{\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12 /v2/{name=projects/*/policies/*}Z!\x12\x1f/v2/{name=folders/*/policies/*}Z\'\x12%/v2/{name=organizations/*/policies/*}\x12\xa5\x02\n\x12GetEffectivePolicy\x124.google.cloud.orgpolicy.v2.GetEffectivePolicyRequest\x1a!.google.cloud.orgpolicy.v2.Policy"\xb5\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa7\x01\x123/v2/{name=projects/*/policies/*}:getEffectivePolicyZ4\x122/v2/{name=folders/*/policies/*}:getEffectivePolicyZ:\x128/v2/{name=organizations/*/policies/*}:getEffectivePolicy\x12\x81\x02\n\x0cCreatePolicy\x12..google.cloud.orgpolicy.v2.CreatePolicyRequest\x1a!.google.cloud.orgpolicy.v2.Policy"\x9d\x01\xdaA\rparent,policy\x82\xd3\xe4\x93\x02\x86\x01" /v2/{parent=projects/*}/policies:\x06policyZ)"\x1f/v2/{parent=folders/*}/policies:\x06policyZ/"%/v2/{parent=organizations/*}/policies:\x06policy\x12\x8f\x02\n\x0cUpdatePolicy\x12..google.cloud.orgpolicy.v2.UpdatePolicyRequest\x1a!.google.cloud.orgpolicy.v2.Policy"\xab\x01\xdaA\x06policy\x82\xd3\xe4\x93\x02\x9b\x012\'/v2/{policy.name=projects/*/policies/*}:\x06policyZ02&/v2/{policy.name=folders/*/policies/*}:\x06policyZ62,/v2/{policy.name=organizations/*/policies/*}:\x06policy\x12\xd3\x01\n\x0cDeletePolicy\x12..google.cloud.orgpolicy.v2.DeletePolicyRequest\x1a\x16.google.protobuf.Empty"{\xdaA\x04name\x82\xd3\xe4\x93\x02n* /v2/{name=projects/*/policies/*}Z!*\x1f/v2/{name=folders/*/policies/*}Z\'*%/v2/{name=organizations/*/policies/*}\x12\xe5\x01\n\x16CreateCustomConstraint\x128.google.cloud.orgpolicy.v2.CreateCustomConstraintRequest\x1a+.google.cloud.orgpolicy.v2.CustomConstraint"d\xdaA\x18parent,custom_constraint\x82\xd3\xe4\x93\x02C"./v2/{parent=organizations/*}/customConstraints:\x11custom_constraint\x12\xf0\x01\n\x16UpdateCustomConstraint\x128.google.cloud.orgpolicy.v2.UpdateCustomConstraintRequest\x1a+.google.cloud.orgpolicy.v2.CustomConstraint"o\xdaA\x11custom_constraint\x82\xd3\xe4\x93\x02U2@/v2/{custom_constraint.name=organizations/*/customConstraints/*}:\x11custom_constraint\x12\xb8\x01\n\x13GetCustomConstraint\x125.google.cloud.orgpolicy.v2.GetCustomConstraintRequest\x1a+.google.cloud.orgpolicy.v2.CustomConstraint"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v2/{name=organizations/*/customConstraints/*}\x12\xcb\x01\n\x15ListCustomConstraints\x127.google.cloud.orgpolicy.v2.ListCustomConstraintsRequest\x1a8.google.cloud.orgpolicy.v2.ListCustomConstraintsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v2/{parent=organizations/*}/customConstraints\x12\xa9\x01\n\x16DeleteCustomConstraint\x128.google.cloud.orgpolicy.v2.DeleteCustomConstraintRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020*./v2/{name=organizations/*/customConstraints/*}\x1aL\xcaA\x18orgpolicy.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc5\x01\n\x1dcom.google.cloud.orgpolicy.v2B\x0eOrgPolicyProtoP\x01Z;cloud.google.com/go/orgpolicy/apiv2/orgpolicypb;orgpolicypb\xaa\x02\x19Google.Cloud.OrgPolicy.V2\xca\x02\x19Google\\Cloud\\OrgPolicy\\V2\xea\x02\x1cGoogle::Cloud::OrgPolicy::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.orgpolicy.v2.orgpolicy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.orgpolicy.v2B\x0eOrgPolicyProtoP\x01Z;cloud.google.com/go/orgpolicy/apiv2/orgpolicypb;orgpolicypb\xaa\x02\x19Google.Cloud.OrgPolicy.V2\xca\x02\x19Google\\Cloud\\OrgPolicy\\V2\xea\x02\x1cGoogle::Cloud::OrgPolicy::V2'
    _globals['_POLICY'].fields_by_name['name']._loaded_options = None
    _globals['_POLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_POLICY'].fields_by_name['alternate']._loaded_options = None
    _globals['_POLICY'].fields_by_name['alternate']._serialized_options = b'\x18\x01'
    _globals['_POLICY'].fields_by_name['etag']._loaded_options = None
    _globals['_POLICY'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY']._loaded_options = None
    _globals['_POLICY']._serialized_options = b'\xeaA\x9b\x01\n\x1forgpolicy.googleapis.com/Policy\x12$projects/{project}/policies/{policy}\x12"folders/{folder}/policies/{policy}\x12.organizations/{organization}/policies/{policy}'
    _globals['_POLICYSPEC'].fields_by_name['update_time']._loaded_options = None
    _globals['_POLICYSPEC'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_LISTCONSTRAINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONSTRAINTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#orgpolicy.googleapis.com/Constraint'
    _globals['_LISTPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1forgpolicy.googleapis.com/Policy'
    _globals['_GETPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1forgpolicy.googleapis.com/Policy'
    _globals['_GETEFFECTIVEPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEFFECTIVEPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1forgpolicy.googleapis.com/Policy'
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1forgpolicy.googleapis.com/Policy'
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_UPDATEPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1forgpolicy.googleapis.com/Policy'
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECUSTOMCONSTRAINTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECUSTOMCONSTRAINTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)orgpolicy.googleapis.com/CustomConstraint'
    _globals['_CREATECUSTOMCONSTRAINTREQUEST'].fields_by_name['custom_constraint']._loaded_options = None
    _globals['_CREATECUSTOMCONSTRAINTREQUEST'].fields_by_name['custom_constraint']._serialized_options = b'\xe0A\x02'
    _globals['_GETCUSTOMCONSTRAINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMCONSTRAINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)orgpolicy.googleapis.com/CustomConstraint'
    _globals['_LISTCUSTOMCONSTRAINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCUSTOMCONSTRAINTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)orgpolicy.googleapis.com/CustomConstraint'
    _globals['_UPDATECUSTOMCONSTRAINTREQUEST'].fields_by_name['custom_constraint']._loaded_options = None
    _globals['_UPDATECUSTOMCONSTRAINTREQUEST'].fields_by_name['custom_constraint']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECUSTOMCONSTRAINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECUSTOMCONSTRAINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)orgpolicy.googleapis.com/CustomConstraint'
    _globals['_ORGPOLICY']._loaded_options = None
    _globals['_ORGPOLICY']._serialized_options = b'\xcaA\x18orgpolicy.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ORGPOLICY'].methods_by_name['ListConstraints']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['ListConstraints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02w\x12#/v2/{parent=projects/*}/constraintsZ$\x12"/v2/{parent=folders/*}/constraintsZ*\x12(/v2/{parent=organizations/*}/constraints'
    _globals['_ORGPOLICY'].methods_by_name['ListPolicies']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['ListPolicies']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12 /v2/{parent=projects/*}/policiesZ!\x12\x1f/v2/{parent=folders/*}/policiesZ'\x12%/v2/{parent=organizations/*}/policies"
    _globals['_ORGPOLICY'].methods_by_name['GetPolicy']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['GetPolicy']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12 /v2/{name=projects/*/policies/*}Z!\x12\x1f/v2/{name=folders/*/policies/*}Z'\x12%/v2/{name=organizations/*/policies/*}"
    _globals['_ORGPOLICY'].methods_by_name['GetEffectivePolicy']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['GetEffectivePolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa7\x01\x123/v2/{name=projects/*/policies/*}:getEffectivePolicyZ4\x122/v2/{name=folders/*/policies/*}:getEffectivePolicyZ:\x128/v2/{name=organizations/*/policies/*}:getEffectivePolicy'
    _globals['_ORGPOLICY'].methods_by_name['CreatePolicy']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['CreatePolicy']._serialized_options = b'\xdaA\rparent,policy\x82\xd3\xe4\x93\x02\x86\x01" /v2/{parent=projects/*}/policies:\x06policyZ)"\x1f/v2/{parent=folders/*}/policies:\x06policyZ/"%/v2/{parent=organizations/*}/policies:\x06policy'
    _globals['_ORGPOLICY'].methods_by_name['UpdatePolicy']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['UpdatePolicy']._serialized_options = b"\xdaA\x06policy\x82\xd3\xe4\x93\x02\x9b\x012'/v2/{policy.name=projects/*/policies/*}:\x06policyZ02&/v2/{policy.name=folders/*/policies/*}:\x06policyZ62,/v2/{policy.name=organizations/*/policies/*}:\x06policy"
    _globals['_ORGPOLICY'].methods_by_name['DeletePolicy']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['DeletePolicy']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02n* /v2/{name=projects/*/policies/*}Z!*\x1f/v2/{name=folders/*/policies/*}Z'*%/v2/{name=organizations/*/policies/*}"
    _globals['_ORGPOLICY'].methods_by_name['CreateCustomConstraint']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['CreateCustomConstraint']._serialized_options = b'\xdaA\x18parent,custom_constraint\x82\xd3\xe4\x93\x02C"./v2/{parent=organizations/*}/customConstraints:\x11custom_constraint'
    _globals['_ORGPOLICY'].methods_by_name['UpdateCustomConstraint']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['UpdateCustomConstraint']._serialized_options = b'\xdaA\x11custom_constraint\x82\xd3\xe4\x93\x02U2@/v2/{custom_constraint.name=organizations/*/customConstraints/*}:\x11custom_constraint'
    _globals['_ORGPOLICY'].methods_by_name['GetCustomConstraint']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['GetCustomConstraint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v2/{name=organizations/*/customConstraints/*}'
    _globals['_ORGPOLICY'].methods_by_name['ListCustomConstraints']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['ListCustomConstraints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v2/{parent=organizations/*}/customConstraints'
    _globals['_ORGPOLICY'].methods_by_name['DeleteCustomConstraint']._loaded_options = None
    _globals['_ORGPOLICY'].methods_by_name['DeleteCustomConstraint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020*./v2/{name=organizations/*/customConstraints/*}'
    _globals['_POLICY']._serialized_start = 352
    _globals['_POLICY']._serialized_end = 745
    _globals['_ALTERNATEPOLICYSPEC']._serialized_start = 747
    _globals['_ALTERNATEPOLICYSPEC']._serialized_end = 837
    _globals['_POLICYSPEC']._serialized_start = 840
    _globals['_POLICYSPEC']._serialized_end = 1294
    _globals['_POLICYSPEC_POLICYRULE']._serialized_start = 1032
    _globals['_POLICYSPEC_POLICYRULE']._serialized_end = 1294
    _globals['_POLICYSPEC_POLICYRULE_STRINGVALUES']._serialized_start = 1225
    _globals['_POLICYSPEC_POLICYRULE_STRINGVALUES']._serialized_end = 1286
    _globals['_LISTCONSTRAINTSREQUEST']._serialized_start = 1296
    _globals['_LISTCONSTRAINTSREQUEST']._serialized_end = 1420
    _globals['_LISTCONSTRAINTSRESPONSE']._serialized_start = 1422
    _globals['_LISTCONSTRAINTSRESPONSE']._serialized_end = 1532
    _globals['_LISTPOLICIESREQUEST']._serialized_start = 1534
    _globals['_LISTPOLICIESREQUEST']._serialized_end = 1651
    _globals['_LISTPOLICIESRESPONSE']._serialized_start = 1653
    _globals['_LISTPOLICIESRESPONSE']._serialized_end = 1753
    _globals['_GETPOLICYREQUEST']._serialized_start = 1755
    _globals['_GETPOLICYREQUEST']._serialized_end = 1828
    _globals['_GETEFFECTIVEPOLICYREQUEST']._serialized_start = 1830
    _globals['_GETEFFECTIVEPOLICYREQUEST']._serialized_end = 1912
    _globals['_CREATEPOLICYREQUEST']._serialized_start = 1915
    _globals['_CREATEPOLICYREQUEST']._serialized_end = 2049
    _globals['_UPDATEPOLICYREQUEST']._serialized_start = 2051
    _globals['_UPDATEPOLICYREQUEST']._serialized_end = 2177
    _globals['_DELETEPOLICYREQUEST']._serialized_start = 2179
    _globals['_DELETEPOLICYREQUEST']._serialized_end = 2274
    _globals['_CREATECUSTOMCONSTRAINTREQUEST']._serialized_start = 2277
    _globals['_CREATECUSTOMCONSTRAINTREQUEST']._serialized_end = 2452
    _globals['_GETCUSTOMCONSTRAINTREQUEST']._serialized_start = 2454
    _globals['_GETCUSTOMCONSTRAINTREQUEST']._serialized_end = 2547
    _globals['_LISTCUSTOMCONSTRAINTSREQUEST']._serialized_start = 2550
    _globals['_LISTCUSTOMCONSTRAINTSREQUEST']._serialized_end = 2686
    _globals['_LISTCUSTOMCONSTRAINTSRESPONSE']._serialized_start = 2689
    _globals['_LISTCUSTOMCONSTRAINTSRESPONSE']._serialized_end = 2818
    _globals['_UPDATECUSTOMCONSTRAINTREQUEST']._serialized_start = 2820
    _globals['_UPDATECUSTOMCONSTRAINTREQUEST']._serialized_end = 2928
    _globals['_DELETECUSTOMCONSTRAINTREQUEST']._serialized_start = 2930
    _globals['_DELETECUSTOMCONSTRAINTREQUEST']._serialized_end = 3026
    _globals['_ORGPOLICY']._serialized_start = 3029
    _globals['_ORGPOLICY']._serialized_end = 5922