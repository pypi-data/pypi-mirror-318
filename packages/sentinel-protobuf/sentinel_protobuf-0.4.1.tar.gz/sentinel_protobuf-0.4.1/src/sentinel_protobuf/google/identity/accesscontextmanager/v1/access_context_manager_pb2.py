"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/identity/accesscontextmanager/v1/access_context_manager.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.identity.accesscontextmanager.v1 import access_level_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2
from .....google.identity.accesscontextmanager.v1 import access_policy_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2
from .....google.identity.accesscontextmanager.v1 import gcp_user_access_binding_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_gcp__user__access__binding__pb2
from .....google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/identity/accesscontextmanager/v1/access_context_manager.proto\x12\'google.identity.accesscontextmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a:google/identity/accesscontextmanager/v1/access_level.proto\x1a;google/identity/accesscontextmanager/v1/access_policy.proto\x1aEgoogle/identity/accesscontextmanager/v1/gcp_user_access_binding.proto\x1a?google/identity/accesscontextmanager/v1/service_perimeter.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto"\x8c\x01\n\x19ListAccessPoliciesRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x85\x01\n\x1aListAccessPoliciesResponse\x12N\n\x0faccess_policies\x18\x01 \x03(\x0b25.google.identity.accesscontextmanager.v1.AccessPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x16GetAccessPolicyRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0accesscontextmanager.googleapis.com/AccessPolicy"\x9d\x01\n\x19UpdateAccessPolicyRequest\x12J\n\x06policy\x18\x01 \x01(\x0b25.google.identity.accesscontextmanager.v1.AccessPolicyB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"c\n\x19DeleteAccessPolicyRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0accesscontextmanager.googleapis.com/AccessPolicy"\xdc\x01\n\x17ListAccessLevelsRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/accesscontextmanager.googleapis.com/AccessLevel\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12Q\n\x13access_level_format\x18\x04 \x01(\x0e24.google.identity.accesscontextmanager.v1.LevelFormat"\x80\x01\n\x18ListAccessLevelsResponse\x12K\n\raccess_levels\x18\x01 \x03(\x0b24.google.identity.accesscontextmanager.v1.AccessLevel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb1\x01\n\x15GetAccessLevelRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/accesscontextmanager.googleapis.com/AccessLevel\x12Q\n\x13access_level_format\x18\x02 \x01(\x0e24.google.identity.accesscontextmanager.v1.LevelFormat"\xb4\x01\n\x18CreateAccessLevelRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/accesscontextmanager.googleapis.com/AccessLevel\x12O\n\x0caccess_level\x18\x02 \x01(\x0b24.google.identity.accesscontextmanager.v1.AccessLevelB\x03\xe0A\x02"\xa1\x01\n\x18UpdateAccessLevelRequest\x12O\n\x0caccess_level\x18\x01 \x01(\x0b24.google.identity.accesscontextmanager.v1.AccessLevelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"a\n\x18DeleteAccessLevelRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/accesscontextmanager.googleapis.com/AccessLevel"\xc5\x01\n\x1aReplaceAccessLevelsRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/accesscontextmanager.googleapis.com/AccessLevel\x12P\n\raccess_levels\x18\x02 \x03(\x0b24.google.identity.accesscontextmanager.v1.AccessLevelB\x03\xe0A\x02\x12\x0c\n\x04etag\x18\x04 \x01(\t"j\n\x1bReplaceAccessLevelsResponse\x12K\n\raccess_levels\x18\x01 \x03(\x0b24.google.identity.accesscontextmanager.v1.AccessLevel"\x93\x01\n\x1cListServicePerimetersRequest\x12L\n\x06parent\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8f\x01\n\x1dListServicePerimetersResponse\x12U\n\x12service_perimeters\x18\x01 \x03(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeter\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"h\n\x1aGetServicePerimeterRequest\x12J\n\x04name\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\n4accesscontextmanager.googleapis.com/ServicePerimeter"\xc8\x01\n\x1dCreateServicePerimeterRequest\x12L\n\x06parent\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter\x12Y\n\x11service_perimeter\x18\x02 \x01(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeterB\x03\xe0A\x02"\xb0\x01\n\x1dUpdateServicePerimeterRequest\x12Y\n\x11service_perimeter\x18\x01 \x01(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeterB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"k\n\x1dDeleteServicePerimeterRequest\x12J\n\x04name\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\n4accesscontextmanager.googleapis.com/ServicePerimeter"\xd9\x01\n\x1fReplaceServicePerimetersRequest\x12L\n\x06parent\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter\x12Z\n\x12service_perimeters\x18\x02 \x03(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeterB\x03\xe0A\x02\x12\x0c\n\x04etag\x18\x03 \x01(\t"y\n ReplaceServicePerimetersResponse\x12U\n\x12service_perimeters\x18\x01 \x03(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeter"|\n\x1eCommitServicePerimetersRequest\x12L\n\x06parent\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter\x12\x0c\n\x04etag\x18\x02 \x01(\t"x\n\x1fCommitServicePerimetersResponse\x12U\n\x12service_perimeters\x18\x01 \x03(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeter"\x9d\x01\n ListGcpUserAccessBindingsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x9d\x01\n!ListGcpUserAccessBindingsResponse\x12_\n\x18gcp_user_access_bindings\x18\x01 \x03(\x0b2=.google.identity.accesscontextmanager.v1.GcpUserAccessBinding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"p\n\x1eGetGcpUserAccessBindingRequest\x12N\n\x04name\x18\x01 \x01(\tB@\xe0A\x02\xfaA:\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding"\xd2\x01\n!CreateGcpUserAccessBindingRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12c\n\x17gcp_user_access_binding\x18\x02 \x01(\x0b2=.google.identity.accesscontextmanager.v1.GcpUserAccessBindingB\x03\xe0A\x02"\xbe\x01\n!UpdateGcpUserAccessBindingRequest\x12c\n\x17gcp_user_access_binding\x18\x01 \x01(\x0b2=.google.identity.accesscontextmanager.v1.GcpUserAccessBindingB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"s\n!DeleteGcpUserAccessBindingRequest\x12N\n\x04name\x18\x01 \x01(\tB@\xe0A\x02\xfaA:\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding"\'\n%GcpUserAccessBindingOperationMetadata"\'\n%AccessContextManagerOperationMetadata*D\n\x0bLevelFormat\x12\x1c\n\x18LEVEL_FORMAT_UNSPECIFIED\x10\x00\x12\x0e\n\nAS_DEFINED\x10\x01\x12\x07\n\x03CEL\x10\x022\xf12\n\x14AccessContextManager\x12\xb9\x01\n\x12ListAccessPolicies\x12B.google.identity.accesscontextmanager.v1.ListAccessPoliciesRequest\x1aC.google.identity.accesscontextmanager.v1.ListAccessPoliciesResponse"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/accessPolicies\x12\xb5\x01\n\x0fGetAccessPolicy\x12?.google.identity.accesscontextmanager.v1.GetAccessPolicyRequest\x1a5.google.identity.accesscontextmanager.v1.AccessPolicy"*\xdaA\x04name\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/{name=accessPolicies/*}\x12\xc1\x01\n\x12CreateAccessPolicy\x125.google.identity.accesscontextmanager.v1.AccessPolicy\x1a\x1d.google.longrunning.Operation"U\xcaA5\n\x0cAccessPolicy\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02\x17"\x12/v1/accessPolicies:\x01*\x12\xf8\x01\n\x12UpdateAccessPolicy\x12B.google.identity.accesscontextmanager.v1.UpdateAccessPolicyRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA5\n\x0cAccessPolicy\x12%AccessContextManagerOperationMetadata\xdaA\x12policy,update_mask\x82\xd3\xe4\x93\x02,2"/v1/{policy.name=accessPolicies/*}:\x06policy\x12\xe4\x01\n\x12DeleteAccessPolicy\x12B.google.identity.accesscontextmanager.v1.DeleteAccessPolicyRequest\x1a\x1d.google.longrunning.Operation"k\xcaA>\n\x15google.protobuf.Empty\x12%AccessContextManagerOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/{name=accessPolicies/*}\x12\xd4\x01\n\x10ListAccessLevels\x12@.google.identity.accesscontextmanager.v1.ListAccessLevelsRequest\x1aA.google.identity.accesscontextmanager.v1.ListAccessLevelsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=accessPolicies/*}/accessLevels\x12\xc1\x01\n\x0eGetAccessLevel\x12>.google.identity.accesscontextmanager.v1.GetAccessLevelRequest\x1a4.google.identity.accesscontextmanager.v1.AccessLevel"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=accessPolicies/*/accessLevels/*}\x12\x85\x02\n\x11CreateAccessLevel\x12A.google.identity.accesscontextmanager.v1.CreateAccessLevelRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA4\n\x0bAccessLevel\x12%AccessContextManagerOperationMetadata\xdaA\x13parent,access_level\x82\xd3\xe4\x93\x02:"*/v1/{parent=accessPolicies/*}/accessLevels:\x0caccess_level\x12\x97\x02\n\x11UpdateAccessLevel\x12A.google.identity.accesscontextmanager.v1.UpdateAccessLevelRequest\x1a\x1d.google.longrunning.Operation"\x9f\x01\xcaA4\n\x0bAccessLevel\x12%AccessContextManagerOperationMetadata\xdaA\x18access_level,update_mask\x82\xd3\xe4\x93\x02G27/v1/{access_level.name=accessPolicies/*/accessLevels/*}:\x0caccess_level\x12\xf1\x01\n\x11DeleteAccessLevel\x12A.google.identity.accesscontextmanager.v1.DeleteAccessLevelRequest\x1a\x1d.google.longrunning.Operation"z\xcaA>\n\x15google.protobuf.Empty\x12%AccessContextManagerOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=accessPolicies/*/accessLevels/*}\x12\x83\x02\n\x13ReplaceAccessLevels\x12C.google.identity.accesscontextmanager.v1.ReplaceAccessLevelsRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaAD\n\x1bReplaceAccessLevelsResponse\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02:"5/v1/{parent=accessPolicies/*}/accessLevels:replaceAll:\x01*\x12\xe8\x01\n\x15ListServicePerimeters\x12E.google.identity.accesscontextmanager.v1.ListServicePerimetersRequest\x1aF.google.identity.accesscontextmanager.v1.ListServicePerimetersResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=accessPolicies/*}/servicePerimeters\x12\xd5\x01\n\x13GetServicePerimeter\x12C.google.identity.accesscontextmanager.v1.GetServicePerimeterRequest\x1a9.google.identity.accesscontextmanager.v1.ServicePerimeter">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=accessPolicies/*/servicePerimeters/*}\x12\xa3\x02\n\x16CreateServicePerimeter\x12F.google.identity.accesscontextmanager.v1.CreateServicePerimeterRequest\x1a\x1d.google.longrunning.Operation"\xa1\x01\xcaA9\n\x10ServicePerimeter\x12%AccessContextManagerOperationMetadata\xdaA\x18parent,service_perimeter\x82\xd3\xe4\x93\x02D"//v1/{parent=accessPolicies/*}/servicePerimeters:\x11service_perimeter\x12\xba\x02\n\x16UpdateServicePerimeter\x12F.google.identity.accesscontextmanager.v1.UpdateServicePerimeterRequest\x1a\x1d.google.longrunning.Operation"\xb8\x01\xcaA9\n\x10ServicePerimeter\x12%AccessContextManagerOperationMetadata\xdaA\x1dservice_perimeter,update_mask\x82\xd3\xe4\x93\x02V2A/v1/{service_perimeter.name=accessPolicies/*/servicePerimeters/*}:\x11service_perimeter\x12\x80\x02\n\x16DeleteServicePerimeter\x12F.google.identity.accesscontextmanager.v1.DeleteServicePerimeterRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA>\n\x15google.protobuf.Empty\x12%AccessContextManagerOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=accessPolicies/*/servicePerimeters/*}\x12\x97\x02\n\x18ReplaceServicePerimeters\x12H.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersRequest\x1a\x1d.google.longrunning.Operation"\x91\x01\xcaAI\n ReplaceServicePerimetersResponse\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02?":/v1/{parent=accessPolicies/*}/servicePerimeters:replaceAll:\x01*\x12\x90\x02\n\x17CommitServicePerimeters\x12G.google.identity.accesscontextmanager.v1.CommitServicePerimetersRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaAH\n\x1fCommitServicePerimetersResponse\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02;"6/v1/{parent=accessPolicies/*}/servicePerimeters:commit:\x01*\x12\xf7\x01\n\x19ListGcpUserAccessBindings\x12I.google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsRequest\x1aJ.google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=organizations/*}/gcpUserAccessBindings\x12\xe4\x01\n\x17GetGcpUserAccessBinding\x12G.google.identity.accesscontextmanager.v1.GetGcpUserAccessBindingRequest\x1a=.google.identity.accesscontextmanager.v1.GcpUserAccessBinding"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=organizations/*/gcpUserAccessBindings/*}\x12\xbe\x02\n\x1aCreateGcpUserAccessBinding\x12J.google.identity.accesscontextmanager.v1.CreateGcpUserAccessBindingRequest\x1a\x1d.google.longrunning.Operation"\xb4\x01\xcaA=\n\x14GcpUserAccessBinding\x12%GcpUserAccessBindingOperationMetadata\xdaA\x1eparent,gcp_user_access_binding\x82\xd3\xe4\x93\x02M"2/v1/{parent=organizations/*}/gcpUserAccessBindings:\x17gcp_user_access_binding\x12\xdb\x02\n\x1aUpdateGcpUserAccessBinding\x12J.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest\x1a\x1d.google.longrunning.Operation"\xd1\x01\xcaA=\n\x14GcpUserAccessBinding\x12%GcpUserAccessBindingOperationMetadata\xdaA#gcp_user_access_binding,update_mask\x82\xd3\xe4\x93\x02e2J/v1/{gcp_user_access_binding.name=organizations/*/gcpUserAccessBindings/*}:\x17gcp_user_access_binding\x12\x8c\x02\n\x1aDeleteGcpUserAccessBinding\x12J.google.identity.accesscontextmanager.v1.DeleteGcpUserAccessBindingRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA>\n\x15google.protobuf.Empty\x12%GcpUserAccessBindingOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=organizations/*/gcpUserAccessBindings/*}\x12\x82\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"7\x82\xd3\xe4\x93\x021",/v1/{resource=accessPolicies/*}:setIamPolicy:\x01*\x12\x82\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"7\x82\xd3\xe4\x93\x021",/v1/{resource=accessPolicies/*}:getIamPolicy:\x01*\x12\xbf\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xd3\x01\x82\xd3\xe4\x93\x02\xcc\x01"2/v1/{resource=accessPolicies/*}:testIamPermissions:\x01*ZF"A/v1/{resource=accessPolicies/*/accessLevels/*}:testIamPermissions:\x01*ZK"F/v1/{resource=accessPolicies/*/servicePerimeters/*}:testIamPermissions:\x01*\x1aW\xcaA#accesscontextmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb0\x02\n+com.google.identity.accesscontextmanager.v1B\x19AccessContextManagerProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02\'Google.Identity.AccessContextManager.V1\xca\x02\'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.identity.accesscontextmanager.v1.access_context_manager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.identity.accesscontextmanager.v1B\x19AccessContextManagerProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02'Google.Identity.AccessContextManager.V1\xca\x02'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1"
    _globals['_LISTACCESSPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCESSPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_GETACCESSPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCESSPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0accesscontextmanager.googleapis.com/AccessPolicy'
    _globals['_UPDATEACCESSPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_UPDATEACCESSPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCESSPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEACCESSPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEACCESSPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACCESSPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0accesscontextmanager.googleapis.com/AccessPolicy'
    _globals['_LISTACCESSLEVELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCESSLEVELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/accesscontextmanager.googleapis.com/AccessLevel'
    _globals['_GETACCESSLEVELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCESSLEVELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/accesscontextmanager.googleapis.com/AccessLevel'
    _globals['_CREATEACCESSLEVELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEACCESSLEVELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/accesscontextmanager.googleapis.com/AccessLevel'
    _globals['_CREATEACCESSLEVELREQUEST'].fields_by_name['access_level']._loaded_options = None
    _globals['_CREATEACCESSLEVELREQUEST'].fields_by_name['access_level']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCESSLEVELREQUEST'].fields_by_name['access_level']._loaded_options = None
    _globals['_UPDATEACCESSLEVELREQUEST'].fields_by_name['access_level']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCESSLEVELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEACCESSLEVELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEACCESSLEVELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACCESSLEVELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/accesscontextmanager.googleapis.com/AccessLevel'
    _globals['_REPLACEACCESSLEVELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REPLACEACCESSLEVELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/accesscontextmanager.googleapis.com/AccessLevel'
    _globals['_REPLACEACCESSLEVELSREQUEST'].fields_by_name['access_levels']._loaded_options = None
    _globals['_REPLACEACCESSLEVELSREQUEST'].fields_by_name['access_levels']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSERVICEPERIMETERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVICEPERIMETERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter'
    _globals['_GETSERVICEPERIMETERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVICEPERIMETERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA6\n4accesscontextmanager.googleapis.com/ServicePerimeter'
    _globals['_CREATESERVICEPERIMETERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVICEPERIMETERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter'
    _globals['_CREATESERVICEPERIMETERREQUEST'].fields_by_name['service_perimeter']._loaded_options = None
    _globals['_CREATESERVICEPERIMETERREQUEST'].fields_by_name['service_perimeter']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVICEPERIMETERREQUEST'].fields_by_name['service_perimeter']._loaded_options = None
    _globals['_UPDATESERVICEPERIMETERREQUEST'].fields_by_name['service_perimeter']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVICEPERIMETERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESERVICEPERIMETERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICEPERIMETERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVICEPERIMETERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA6\n4accesscontextmanager.googleapis.com/ServicePerimeter'
    _globals['_REPLACESERVICEPERIMETERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REPLACESERVICEPERIMETERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter'
    _globals['_REPLACESERVICEPERIMETERSREQUEST'].fields_by_name['service_perimeters']._loaded_options = None
    _globals['_REPLACESERVICEPERIMETERSREQUEST'].fields_by_name['service_perimeters']._serialized_options = b'\xe0A\x02'
    _globals['_COMMITSERVICEPERIMETERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COMMITSERVICEPERIMETERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA6\x124accesscontextmanager.googleapis.com/ServicePerimeter'
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETGCPUSERACCESSBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGCPUSERACCESSBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA:\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding'
    _globals['_CREATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_CREATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['gcp_user_access_binding']._loaded_options = None
    _globals['_CREATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['gcp_user_access_binding']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['gcp_user_access_binding']._loaded_options = None
    _globals['_UPDATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['gcp_user_access_binding']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGCPUSERACCESSBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA:\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding'
    _globals['_ACCESSCONTEXTMANAGER']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER']._serialized_options = b'\xcaA#accesscontextmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListAccessPolicies']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListAccessPolicies']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/accessPolicies'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetAccessPolicy']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetAccessPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/{name=accessPolicies/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateAccessPolicy']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateAccessPolicy']._serialized_options = b'\xcaA5\n\x0cAccessPolicy\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02\x17"\x12/v1/accessPolicies:\x01*'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateAccessPolicy']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateAccessPolicy']._serialized_options = b'\xcaA5\n\x0cAccessPolicy\x12%AccessContextManagerOperationMetadata\xdaA\x12policy,update_mask\x82\xd3\xe4\x93\x02,2"/v1/{policy.name=accessPolicies/*}:\x06policy'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteAccessPolicy']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteAccessPolicy']._serialized_options = b'\xcaA>\n\x15google.protobuf.Empty\x12%AccessContextManagerOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/{name=accessPolicies/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListAccessLevels']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListAccessLevels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=accessPolicies/*}/accessLevels'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetAccessLevel']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetAccessLevel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=accessPolicies/*/accessLevels/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateAccessLevel']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateAccessLevel']._serialized_options = b'\xcaA4\n\x0bAccessLevel\x12%AccessContextManagerOperationMetadata\xdaA\x13parent,access_level\x82\xd3\xe4\x93\x02:"*/v1/{parent=accessPolicies/*}/accessLevels:\x0caccess_level'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateAccessLevel']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateAccessLevel']._serialized_options = b'\xcaA4\n\x0bAccessLevel\x12%AccessContextManagerOperationMetadata\xdaA\x18access_level,update_mask\x82\xd3\xe4\x93\x02G27/v1/{access_level.name=accessPolicies/*/accessLevels/*}:\x0caccess_level'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteAccessLevel']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteAccessLevel']._serialized_options = b'\xcaA>\n\x15google.protobuf.Empty\x12%AccessContextManagerOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=accessPolicies/*/accessLevels/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ReplaceAccessLevels']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ReplaceAccessLevels']._serialized_options = b'\xcaAD\n\x1bReplaceAccessLevelsResponse\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02:"5/v1/{parent=accessPolicies/*}/accessLevels:replaceAll:\x01*'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListServicePerimeters']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListServicePerimeters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=accessPolicies/*}/servicePerimeters'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetServicePerimeter']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetServicePerimeter']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=accessPolicies/*/servicePerimeters/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateServicePerimeter']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateServicePerimeter']._serialized_options = b'\xcaA9\n\x10ServicePerimeter\x12%AccessContextManagerOperationMetadata\xdaA\x18parent,service_perimeter\x82\xd3\xe4\x93\x02D"//v1/{parent=accessPolicies/*}/servicePerimeters:\x11service_perimeter'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateServicePerimeter']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateServicePerimeter']._serialized_options = b'\xcaA9\n\x10ServicePerimeter\x12%AccessContextManagerOperationMetadata\xdaA\x1dservice_perimeter,update_mask\x82\xd3\xe4\x93\x02V2A/v1/{service_perimeter.name=accessPolicies/*/servicePerimeters/*}:\x11service_perimeter'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteServicePerimeter']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteServicePerimeter']._serialized_options = b'\xcaA>\n\x15google.protobuf.Empty\x12%AccessContextManagerOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=accessPolicies/*/servicePerimeters/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ReplaceServicePerimeters']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ReplaceServicePerimeters']._serialized_options = b'\xcaAI\n ReplaceServicePerimetersResponse\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02?":/v1/{parent=accessPolicies/*}/servicePerimeters:replaceAll:\x01*'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CommitServicePerimeters']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CommitServicePerimeters']._serialized_options = b'\xcaAH\n\x1fCommitServicePerimetersResponse\x12%AccessContextManagerOperationMetadata\x82\xd3\xe4\x93\x02;"6/v1/{parent=accessPolicies/*}/servicePerimeters:commit:\x01*'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListGcpUserAccessBindings']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['ListGcpUserAccessBindings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=organizations/*}/gcpUserAccessBindings'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetGcpUserAccessBinding']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetGcpUserAccessBinding']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=organizations/*/gcpUserAccessBindings/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateGcpUserAccessBinding']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['CreateGcpUserAccessBinding']._serialized_options = b'\xcaA=\n\x14GcpUserAccessBinding\x12%GcpUserAccessBindingOperationMetadata\xdaA\x1eparent,gcp_user_access_binding\x82\xd3\xe4\x93\x02M"2/v1/{parent=organizations/*}/gcpUserAccessBindings:\x17gcp_user_access_binding'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateGcpUserAccessBinding']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['UpdateGcpUserAccessBinding']._serialized_options = b'\xcaA=\n\x14GcpUserAccessBinding\x12%GcpUserAccessBindingOperationMetadata\xdaA#gcp_user_access_binding,update_mask\x82\xd3\xe4\x93\x02e2J/v1/{gcp_user_access_binding.name=organizations/*/gcpUserAccessBindings/*}:\x17gcp_user_access_binding'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteGcpUserAccessBinding']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['DeleteGcpUserAccessBinding']._serialized_options = b'\xcaA>\n\x15google.protobuf.Empty\x12%GcpUserAccessBindingOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=organizations/*/gcpUserAccessBindings/*}'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1/{resource=accessPolicies/*}:setIamPolicy:\x01*'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1/{resource=accessPolicies/*}:getIamPolicy:\x01*'
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_ACCESSCONTEXTMANAGER'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\xcc\x01"2/v1/{resource=accessPolicies/*}:testIamPermissions:\x01*ZF"A/v1/{resource=accessPolicies/*/accessLevels/*}:testIamPermissions:\x01*ZK"F/v1/{resource=accessPolicies/*/servicePerimeters/*}:testIamPermissions:\x01*'
    _globals['_LEVELFORMAT']._serialized_start = 5065
    _globals['_LEVELFORMAT']._serialized_end = 5133
    _globals['_LISTACCESSPOLICIESREQUEST']._serialized_start = 617
    _globals['_LISTACCESSPOLICIESREQUEST']._serialized_end = 757
    _globals['_LISTACCESSPOLICIESRESPONSE']._serialized_start = 760
    _globals['_LISTACCESSPOLICIESRESPONSE']._serialized_end = 893
    _globals['_GETACCESSPOLICYREQUEST']._serialized_start = 895
    _globals['_GETACCESSPOLICYREQUEST']._serialized_end = 991
    _globals['_UPDATEACCESSPOLICYREQUEST']._serialized_start = 994
    _globals['_UPDATEACCESSPOLICYREQUEST']._serialized_end = 1151
    _globals['_DELETEACCESSPOLICYREQUEST']._serialized_start = 1153
    _globals['_DELETEACCESSPOLICYREQUEST']._serialized_end = 1252
    _globals['_LISTACCESSLEVELSREQUEST']._serialized_start = 1255
    _globals['_LISTACCESSLEVELSREQUEST']._serialized_end = 1475
    _globals['_LISTACCESSLEVELSRESPONSE']._serialized_start = 1478
    _globals['_LISTACCESSLEVELSRESPONSE']._serialized_end = 1606
    _globals['_GETACCESSLEVELREQUEST']._serialized_start = 1609
    _globals['_GETACCESSLEVELREQUEST']._serialized_end = 1786
    _globals['_CREATEACCESSLEVELREQUEST']._serialized_start = 1789
    _globals['_CREATEACCESSLEVELREQUEST']._serialized_end = 1969
    _globals['_UPDATEACCESSLEVELREQUEST']._serialized_start = 1972
    _globals['_UPDATEACCESSLEVELREQUEST']._serialized_end = 2133
    _globals['_DELETEACCESSLEVELREQUEST']._serialized_start = 2135
    _globals['_DELETEACCESSLEVELREQUEST']._serialized_end = 2232
    _globals['_REPLACEACCESSLEVELSREQUEST']._serialized_start = 2235
    _globals['_REPLACEACCESSLEVELSREQUEST']._serialized_end = 2432
    _globals['_REPLACEACCESSLEVELSRESPONSE']._serialized_start = 2434
    _globals['_REPLACEACCESSLEVELSRESPONSE']._serialized_end = 2540
    _globals['_LISTSERVICEPERIMETERSREQUEST']._serialized_start = 2543
    _globals['_LISTSERVICEPERIMETERSREQUEST']._serialized_end = 2690
    _globals['_LISTSERVICEPERIMETERSRESPONSE']._serialized_start = 2693
    _globals['_LISTSERVICEPERIMETERSRESPONSE']._serialized_end = 2836
    _globals['_GETSERVICEPERIMETERREQUEST']._serialized_start = 2838
    _globals['_GETSERVICEPERIMETERREQUEST']._serialized_end = 2942
    _globals['_CREATESERVICEPERIMETERREQUEST']._serialized_start = 2945
    _globals['_CREATESERVICEPERIMETERREQUEST']._serialized_end = 3145
    _globals['_UPDATESERVICEPERIMETERREQUEST']._serialized_start = 3148
    _globals['_UPDATESERVICEPERIMETERREQUEST']._serialized_end = 3324
    _globals['_DELETESERVICEPERIMETERREQUEST']._serialized_start = 3326
    _globals['_DELETESERVICEPERIMETERREQUEST']._serialized_end = 3433
    _globals['_REPLACESERVICEPERIMETERSREQUEST']._serialized_start = 3436
    _globals['_REPLACESERVICEPERIMETERSREQUEST']._serialized_end = 3653
    _globals['_REPLACESERVICEPERIMETERSRESPONSE']._serialized_start = 3655
    _globals['_REPLACESERVICEPERIMETERSRESPONSE']._serialized_end = 3776
    _globals['_COMMITSERVICEPERIMETERSREQUEST']._serialized_start = 3778
    _globals['_COMMITSERVICEPERIMETERSREQUEST']._serialized_end = 3902
    _globals['_COMMITSERVICEPERIMETERSRESPONSE']._serialized_start = 3904
    _globals['_COMMITSERVICEPERIMETERSRESPONSE']._serialized_end = 4024
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST']._serialized_start = 4027
    _globals['_LISTGCPUSERACCESSBINDINGSREQUEST']._serialized_end = 4184
    _globals['_LISTGCPUSERACCESSBINDINGSRESPONSE']._serialized_start = 4187
    _globals['_LISTGCPUSERACCESSBINDINGSRESPONSE']._serialized_end = 4344
    _globals['_GETGCPUSERACCESSBINDINGREQUEST']._serialized_start = 4346
    _globals['_GETGCPUSERACCESSBINDINGREQUEST']._serialized_end = 4458
    _globals['_CREATEGCPUSERACCESSBINDINGREQUEST']._serialized_start = 4461
    _globals['_CREATEGCPUSERACCESSBINDINGREQUEST']._serialized_end = 4671
    _globals['_UPDATEGCPUSERACCESSBINDINGREQUEST']._serialized_start = 4674
    _globals['_UPDATEGCPUSERACCESSBINDINGREQUEST']._serialized_end = 4864
    _globals['_DELETEGCPUSERACCESSBINDINGREQUEST']._serialized_start = 4866
    _globals['_DELETEGCPUSERACCESSBINDINGREQUEST']._serialized_end = 4981
    _globals['_GCPUSERACCESSBINDINGOPERATIONMETADATA']._serialized_start = 4983
    _globals['_GCPUSERACCESSBINDINGOPERATIONMETADATA']._serialized_end = 5022
    _globals['_ACCESSCONTEXTMANAGEROPERATIONMETADATA']._serialized_start = 5024
    _globals['_ACCESSCONTEXTMANAGEROPERATIONMETADATA']._serialized_end = 5063
    _globals['_ACCESSCONTEXTMANAGER']._serialized_start = 5136
    _globals['_ACCESSCONTEXTMANAGER']._serialized_end = 11649