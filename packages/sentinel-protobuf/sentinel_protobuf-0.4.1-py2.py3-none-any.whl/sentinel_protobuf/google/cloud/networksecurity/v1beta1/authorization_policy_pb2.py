"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networksecurity/v1beta1/authorization_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/networksecurity/v1beta1/authorization_policy.proto\x12$google.cloud.networksecurity.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\t\n\x13AuthorizationPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Z\n\x06labels\x18\x05 \x03(\x0b2E.google.cloud.networksecurity.v1beta1.AuthorizationPolicy.LabelsEntryB\x03\xe0A\x01\x12U\n\x06action\x18\x06 \x01(\x0e2@.google.cloud.networksecurity.v1beta1.AuthorizationPolicy.ActionB\x03\xe0A\x02\x12R\n\x05rules\x18\x07 \x03(\x0b2>.google.cloud.networksecurity.v1beta1.AuthorizationPolicy.RuleB\x03\xe0A\x01\x1a\xa0\x04\n\x04Rule\x12[\n\x07sources\x18\x01 \x03(\x0b2E.google.cloud.networksecurity.v1beta1.AuthorizationPolicy.Rule.SourceB\x03\xe0A\x01\x12e\n\x0cdestinations\x18\x02 \x03(\x0b2J.google.cloud.networksecurity.v1beta1.AuthorizationPolicy.Rule.DestinationB\x03\xe0A\x01\x1a9\n\x06Source\x12\x17\n\nprincipals\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x16\n\tip_blocks\x18\x02 \x03(\tB\x03\xe0A\x01\x1a\x98\x02\n\x0bDestination\x12\x12\n\x05hosts\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x12\n\x05ports\x18\x02 \x03(\rB\x03\xe0A\x02\x12\x14\n\x07methods\x18\x04 \x03(\tB\x03\xe0A\x01\x12z\n\x11http_header_match\x18\x05 \x01(\x0b2Z.google.cloud.networksecurity.v1beta1.AuthorizationPolicy.Rule.Destination.HttpHeaderMatchB\x03\xe0A\x01\x1aO\n\x0fHttpHeaderMatch\x12\x1a\n\x0bregex_match\x18\x02 \x01(\tB\x03\xe0A\x02H\x00\x12\x18\n\x0bheader_name\x18\x01 \x01(\tB\x03\xe0A\x02B\x06\n\x04type\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"5\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\t\n\x05ALLOW\x10\x01\x12\x08\n\x04DENY\x10\x02:\x8e\x01\xeaA\x8a\x01\n2networksecurity.googleapis.com/AuthorizationPolicy\x12Tprojects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}"\x84\x01\n ListAuthorizationPoliciesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x97\x01\n!ListAuthorizationPoliciesResponse\x12Y\n\x16authorization_policies\x18\x01 \x03(\x0b29.google.cloud.networksecurity.v1beta1.AuthorizationPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"i\n\x1dGetAuthorizationPolicyRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2networksecurity.googleapis.com/AuthorizationPolicy"\xf2\x01\n CreateAuthorizationPolicyRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122networksecurity.googleapis.com/AuthorizationPolicy\x12$\n\x17authorization_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\\\n\x14authorization_policy\x18\x03 \x01(\x0b29.google.cloud.networksecurity.v1beta1.AuthorizationPolicyB\x03\xe0A\x02"\xb6\x01\n UpdateAuthorizationPolicyRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\\\n\x14authorization_policy\x18\x02 \x01(\x0b29.google.cloud.networksecurity.v1beta1.AuthorizationPolicyB\x03\xe0A\x02"l\n DeleteAuthorizationPolicyRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2networksecurity.googleapis.com/AuthorizationPolicyB\x92\x02\n(com.google.cloud.networksecurity.v1beta1B\x18AuthorizationPolicyProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02\'Google::Cloud::NetworkSecurity::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1beta1.authorization_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.networksecurity.v1beta1B\x18AuthorizationPolicyProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02'Google::Cloud::NetworkSecurity::V1beta1"
    _globals['_AUTHORIZATIONPOLICY_RULE_SOURCE'].fields_by_name['principals']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_SOURCE'].fields_by_name['principals']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY_RULE_SOURCE'].fields_by_name['ip_blocks']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_SOURCE'].fields_by_name['ip_blocks']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION_HTTPHEADERMATCH'].fields_by_name['regex_match']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION_HTTPHEADERMATCH'].fields_by_name['regex_match']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION_HTTPHEADERMATCH'].fields_by_name['header_name']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION_HTTPHEADERMATCH'].fields_by_name['header_name']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['hosts']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['hosts']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['ports']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['ports']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['methods']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['methods']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['http_header_match']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION'].fields_by_name['http_header_match']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY_RULE'].fields_by_name['sources']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE'].fields_by_name['sources']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY_RULE'].fields_by_name['destinations']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_RULE'].fields_by_name['destinations']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['description']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['labels']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['action']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['rules']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY'].fields_by_name['rules']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORIZATIONPOLICY']._loaded_options = None
    _globals['_AUTHORIZATIONPOLICY']._serialized_options = b'\xeaA\x8a\x01\n2networksecurity.googleapis.com/AuthorizationPolicy\x12Tprojects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}'
    _globals['_LISTAUTHORIZATIONPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAUTHORIZATIONPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETAUTHORIZATIONPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUTHORIZATIONPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2networksecurity.googleapis.com/AuthorizationPolicy'
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122networksecurity.googleapis.com/AuthorizationPolicy'
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['authorization_policy_id']._loaded_options = None
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['authorization_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['authorization_policy']._loaded_options = None
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['authorization_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['authorization_policy']._loaded_options = None
    _globals['_UPDATEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['authorization_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAUTHORIZATIONPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2networksecurity.googleapis.com/AuthorizationPolicy'
    _globals['_AUTHORIZATIONPOLICY']._serialized_start = 233
    _globals['_AUTHORIZATIONPOLICY']._serialized_end = 1464
    _globals['_AUTHORIZATIONPOLICY_RULE']._serialized_start = 673
    _globals['_AUTHORIZATIONPOLICY_RULE']._serialized_end = 1217
    _globals['_AUTHORIZATIONPOLICY_RULE_SOURCE']._serialized_start = 877
    _globals['_AUTHORIZATIONPOLICY_RULE_SOURCE']._serialized_end = 934
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION']._serialized_start = 937
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION']._serialized_end = 1217
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION_HTTPHEADERMATCH']._serialized_start = 1138
    _globals['_AUTHORIZATIONPOLICY_RULE_DESTINATION_HTTPHEADERMATCH']._serialized_end = 1217
    _globals['_AUTHORIZATIONPOLICY_LABELSENTRY']._serialized_start = 1219
    _globals['_AUTHORIZATIONPOLICY_LABELSENTRY']._serialized_end = 1264
    _globals['_AUTHORIZATIONPOLICY_ACTION']._serialized_start = 1266
    _globals['_AUTHORIZATIONPOLICY_ACTION']._serialized_end = 1319
    _globals['_LISTAUTHORIZATIONPOLICIESREQUEST']._serialized_start = 1467
    _globals['_LISTAUTHORIZATIONPOLICIESREQUEST']._serialized_end = 1599
    _globals['_LISTAUTHORIZATIONPOLICIESRESPONSE']._serialized_start = 1602
    _globals['_LISTAUTHORIZATIONPOLICIESRESPONSE']._serialized_end = 1753
    _globals['_GETAUTHORIZATIONPOLICYREQUEST']._serialized_start = 1755
    _globals['_GETAUTHORIZATIONPOLICYREQUEST']._serialized_end = 1860
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST']._serialized_start = 1863
    _globals['_CREATEAUTHORIZATIONPOLICYREQUEST']._serialized_end = 2105
    _globals['_UPDATEAUTHORIZATIONPOLICYREQUEST']._serialized_start = 2108
    _globals['_UPDATEAUTHORIZATIONPOLICYREQUEST']._serialized_end = 2290
    _globals['_DELETEAUTHORIZATIONPOLICYREQUEST']._serialized_start = 2292
    _globals['_DELETEAUTHORIZATIONPOLICYREQUEST']._serialized_end = 2400