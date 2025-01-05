"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/audit/audit_log.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ....google.rpc.context import attribute_context_pb2 as google_dot_rpc_dot_context_dot_attribute__context__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/audit/audit_log.proto\x12\x12google.cloud.audit\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a*google/rpc/context/attribute_context.proto\x1a\x17google/rpc/status.proto"\xc6\x05\n\x08AuditLog\x12\x14\n\x0cservice_name\x18\x07 \x01(\t\x12\x13\n\x0bmethod_name\x18\x08 \x01(\t\x12\x15\n\rresource_name\x18\x0b \x01(\t\x12?\n\x11resource_location\x18\x14 \x01(\x0b2$.google.cloud.audit.ResourceLocation\x128\n\x17resource_original_state\x18\x13 \x01(\x0b2\x17.google.protobuf.Struct\x12\x1a\n\x12num_response_items\x18\x0c \x01(\x03\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12C\n\x13authentication_info\x18\x03 \x01(\x0b2&.google.cloud.audit.AuthenticationInfo\x12A\n\x12authorization_info\x18\t \x03(\x0b2%.google.cloud.audit.AuthorizationInfo\x12F\n\x15policy_violation_info\x18\x19 \x01(\x0b2\'.google.cloud.audit.PolicyViolationInfo\x12=\n\x10request_metadata\x18\x04 \x01(\x0b2#.google.cloud.audit.RequestMetadata\x12(\n\x07request\x18\x10 \x01(\x0b2\x17.google.protobuf.Struct\x12)\n\x08response\x18\x11 \x01(\x0b2\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x12 \x01(\x0b2\x17.google.protobuf.Struct\x12.\n\x0cservice_data\x18\x0f \x01(\x0b2\x14.google.protobuf.AnyB\x02\x18\x01"\x99\x02\n\x12AuthenticationInfo\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\x12\x1a\n\x12authority_selector\x18\x02 \x01(\t\x126\n\x15third_party_principal\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12 \n\x18service_account_key_name\x18\x05 \x01(\t\x12Y\n\x1fservice_account_delegation_info\x18\x06 \x03(\x0b20.google.cloud.audit.ServiceAccountDelegationInfo\x12\x19\n\x11principal_subject\x18\x08 \x01(\t"\x96\x01\n\x11AuthorizationInfo\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x12\n\npermission\x18\x02 \x01(\t\x12\x0f\n\x07granted\x18\x03 \x01(\x08\x12J\n\x13resource_attributes\x18\x05 \x01(\x0b2-.google.rpc.context.AttributeContext.Resource"\xf5\x01\n\x0fRequestMetadata\x12\x11\n\tcaller_ip\x18\x01 \x01(\t\x12"\n\x1acaller_supplied_user_agent\x18\x02 \x01(\t\x12\x16\n\x0ecaller_network\x18\x03 \x01(\t\x12H\n\x12request_attributes\x18\x07 \x01(\x0b2,.google.rpc.context.AttributeContext.Request\x12I\n\x16destination_attributes\x18\x08 \x01(\x0b2).google.rpc.context.AttributeContext.Peer"I\n\x10ResourceLocation\x12\x19\n\x11current_locations\x18\x01 \x03(\t\x12\x1a\n\x12original_locations\x18\x02 \x03(\t"\xc3\x03\n\x1cServiceAccountDelegationInfo\x12\x19\n\x11principal_subject\x18\x03 \x01(\t\x12e\n\x15first_party_principal\x18\x01 \x01(\x0b2D.google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipalH\x00\x12e\n\x15third_party_principal\x18\x02 \x01(\x0b2D.google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipalH\x00\x1aa\n\x13FirstPartyPrincipal\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\x121\n\x10service_metadata\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x1aJ\n\x13ThirdPartyPrincipal\x123\n\x12third_party_claims\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\x0b\n\tAuthority"d\n\x13PolicyViolationInfo\x12M\n\x19org_policy_violation_info\x18\x01 \x01(\x0b2*.google.cloud.audit.OrgPolicyViolationInfo"\xb2\x02\n\x16OrgPolicyViolationInfo\x12-\n\x07payload\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x1a\n\rresource_type\x18\x02 \x01(\tB\x03\xe0A\x01\x12X\n\rresource_tags\x18\x03 \x03(\x0b2<.google.cloud.audit.OrgPolicyViolationInfo.ResourceTagsEntryB\x03\xe0A\x01\x12>\n\x0eviolation_info\x18\x04 \x03(\x0b2!.google.cloud.audit.ViolationInfoB\x03\xe0A\x01\x1a3\n\x11ResourceTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x97\x02\n\rViolationInfo\x12\x17\n\nconstraint\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rerror_message\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rchecked_value\x18\x03 \x01(\tB\x03\xe0A\x01\x12F\n\x0bpolicy_type\x18\x04 \x01(\x0e2,.google.cloud.audit.ViolationInfo.PolicyTypeB\x03\xe0A\x01"m\n\nPolicyType\x12\x1b\n\x17POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12BOOLEAN_CONSTRAINT\x10\x01\x12\x13\n\x0fLIST_CONSTRAINT\x10\x02\x12\x15\n\x11CUSTOM_CONSTRAINT\x10\x03Be\n\x16com.google.cloud.auditB\rAuditLogProtoP\x01Z7google.golang.org/genproto/googleapis/cloud/audit;audit\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.audit.audit_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.cloud.auditB\rAuditLogProtoP\x01Z7google.golang.org/genproto/googleapis/cloud/audit;audit\xf8\x01\x01'
    _globals['_AUDITLOG'].fields_by_name['service_data']._loaded_options = None
    _globals['_AUDITLOG'].fields_by_name['service_data']._serialized_options = b'\x18\x01'
    _globals['_ORGPOLICYVIOLATIONINFO_RESOURCETAGSENTRY']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONINFO_RESOURCETAGSENTRY']._serialized_options = b'8\x01'
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['payload']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['payload']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['resource_type']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['resource_tags']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['resource_tags']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['violation_info']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONINFO'].fields_by_name['violation_info']._serialized_options = b'\xe0A\x01'
    _globals['_VIOLATIONINFO'].fields_by_name['constraint']._loaded_options = None
    _globals['_VIOLATIONINFO'].fields_by_name['constraint']._serialized_options = b'\xe0A\x01'
    _globals['_VIOLATIONINFO'].fields_by_name['error_message']._loaded_options = None
    _globals['_VIOLATIONINFO'].fields_by_name['error_message']._serialized_options = b'\xe0A\x01'
    _globals['_VIOLATIONINFO'].fields_by_name['checked_value']._loaded_options = None
    _globals['_VIOLATIONINFO'].fields_by_name['checked_value']._serialized_options = b'\xe0A\x01'
    _globals['_VIOLATIONINFO'].fields_by_name['policy_type']._loaded_options = None
    _globals['_VIOLATIONINFO'].fields_by_name['policy_type']._serialized_options = b'\xe0A\x01'
    _globals['_AUDITLOG']._serialized_start = 218
    _globals['_AUDITLOG']._serialized_end = 928
    _globals['_AUTHENTICATIONINFO']._serialized_start = 931
    _globals['_AUTHENTICATIONINFO']._serialized_end = 1212
    _globals['_AUTHORIZATIONINFO']._serialized_start = 1215
    _globals['_AUTHORIZATIONINFO']._serialized_end = 1365
    _globals['_REQUESTMETADATA']._serialized_start = 1368
    _globals['_REQUESTMETADATA']._serialized_end = 1613
    _globals['_RESOURCELOCATION']._serialized_start = 1615
    _globals['_RESOURCELOCATION']._serialized_end = 1688
    _globals['_SERVICEACCOUNTDELEGATIONINFO']._serialized_start = 1691
    _globals['_SERVICEACCOUNTDELEGATIONINFO']._serialized_end = 2142
    _globals['_SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL']._serialized_start = 1956
    _globals['_SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL']._serialized_end = 2053
    _globals['_SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL']._serialized_start = 2055
    _globals['_SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL']._serialized_end = 2129
    _globals['_POLICYVIOLATIONINFO']._serialized_start = 2144
    _globals['_POLICYVIOLATIONINFO']._serialized_end = 2244
    _globals['_ORGPOLICYVIOLATIONINFO']._serialized_start = 2247
    _globals['_ORGPOLICYVIOLATIONINFO']._serialized_end = 2553
    _globals['_ORGPOLICYVIOLATIONINFO_RESOURCETAGSENTRY']._serialized_start = 2502
    _globals['_ORGPOLICYVIOLATIONINFO_RESOURCETAGSENTRY']._serialized_end = 2553
    _globals['_VIOLATIONINFO']._serialized_start = 2556
    _globals['_VIOLATIONINFO']._serialized_end = 2835
    _globals['_VIOLATIONINFO_POLICYTYPE']._serialized_start = 2726
    _globals['_VIOLATIONINFO_POLICYTYPE']._serialized_end = 2835