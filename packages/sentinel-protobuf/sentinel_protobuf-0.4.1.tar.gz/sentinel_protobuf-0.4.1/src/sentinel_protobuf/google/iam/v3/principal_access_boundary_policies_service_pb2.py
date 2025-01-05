"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v3/principal_access_boundary_policies_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.iam.v3 import operation_metadata_pb2 as google_dot_iam_dot_v3_dot_operation__metadata__pb2
from ....google.iam.v3 import policy_binding_resources_pb2 as google_dot_iam_dot_v3_dot_policy__binding__resources__pb2
from ....google.iam.v3 import principal_access_boundary_policy_resources_pb2 as google_dot_iam_dot_v3_dot_principal__access__boundary__policy__resources__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/iam/v3/principal_access_boundary_policies_service.proto\x12\rgoogle.iam.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/iam/v3/operation_metadata.proto\x1a,google/iam/v3/policy_binding_resources.proto\x1a>google/iam/v3/principal_access_boundary_policy_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa1\x02\n*CreatePrincipalAccessBoundaryPolicyRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120iam.googleapis.com/PrincipalAccessBoundaryPolicy\x120\n#principal_access_boundary_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12[\n principal_access_boundary_policy\x18\x03 \x01(\x0b2,.google.iam.v3.PrincipalAccessBoundaryPolicyB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"q\n\'GetPrincipalAccessBoundaryPolicyRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy"\xdb\x01\n*UpdatePrincipalAccessBoundaryPolicyRequest\x12[\n principal_access_boundary_policy\x18\x01 \x01(\x0b2,.google.iam.v3.PrincipalAccessBoundaryPolicyB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xb7\x01\n*DeletePrincipalAccessBoundaryPolicyRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x12\n\x05force\x18\x04 \x01(\x08B\x03\xe0A\x01"\xa7\x01\n*ListPrincipalAccessBoundaryPoliciesRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120iam.googleapis.com/PrincipalAccessBoundaryPolicy\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xa5\x01\n+ListPrincipalAccessBoundaryPoliciesResponse\x12X\n"principal_access_boundary_policies\x18\x01 \x03(\x0b2,.google.iam.v3.PrincipalAccessBoundaryPolicy\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x01"\xad\x01\n2SearchPrincipalAccessBoundaryPolicyBindingsRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"\x8a\x01\n3SearchPrincipalAccessBoundaryPolicyBindingsResponse\x125\n\x0fpolicy_bindings\x18\x01 \x03(\x0b2\x1c.google.iam.v3.PolicyBinding\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x012\xec\x0e\n\x1fPrincipalAccessBoundaryPolicies\x12\xf7\x02\n#CreatePrincipalAccessBoundaryPolicy\x129.google.iam.v3.CreatePrincipalAccessBoundaryPolicyRequest\x1a\x1d.google.longrunning.Operation"\xf5\x01\xcaA2\n\x1dPrincipalAccessBoundaryPolicy\x12\x11OperationMetadata\xdaAKparent,principal_access_boundary_policy,principal_access_boundary_policy_id\x82\xd3\xe4\x93\x02l"H/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies: principal_access_boundary_policy\x12\xe1\x01\n GetPrincipalAccessBoundaryPolicy\x126.google.iam.v3.GetPrincipalAccessBoundaryPolicyRequest\x1a,.google.iam.v3.PrincipalAccessBoundaryPolicy"W\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}\x12\xfa\x02\n#UpdatePrincipalAccessBoundaryPolicy\x129.google.iam.v3.UpdatePrincipalAccessBoundaryPolicyRequest\x1a\x1d.google.longrunning.Operation"\xf8\x01\xcaA2\n\x1dPrincipalAccessBoundaryPolicy\x12\x11OperationMetadata\xdaA,principal_access_boundary_policy,update_mask\x82\xd3\xe4\x93\x02\x8d\x012i/v3/{principal_access_boundary_policy.name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}: principal_access_boundary_policy\x12\x86\x02\n#DeletePrincipalAccessBoundaryPolicy\x129.google.iam.v3.DeletePrincipalAccessBoundaryPolicyRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}\x12\xf7\x01\n#ListPrincipalAccessBoundaryPolicies\x129.google.iam.v3.ListPrincipalAccessBoundaryPoliciesRequest\x1a:.google.iam.v3.ListPrincipalAccessBoundaryPoliciesResponse"Y\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies\x12\xa2\x02\n+SearchPrincipalAccessBoundaryPolicyBindings\x12A.google.iam.v3.SearchPrincipalAccessBoundaryPolicyBindingsRequest\x1aB.google.iam.v3.SearchPrincipalAccessBoundaryPolicyBindingsResponse"l\xdaA\x04name\x82\xd3\xe4\x93\x02_\x12]/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}:searchPolicyBindings\x1aF\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x83\x01\n\x11com.google.iam.v3B+PrincipalAccessBoundaryPoliciesServiceProtoP\x01Z)cloud.google.com/go/iam/apiv3/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v3.principal_access_boundary_policies_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x11com.google.iam.v3B+PrincipalAccessBoundaryPoliciesServiceProtoP\x01Z)cloud.google.com/go/iam/apiv3/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V3'
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120iam.googleapis.com/PrincipalAccessBoundaryPolicy'
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['principal_access_boundary_policy_id']._loaded_options = None
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['principal_access_boundary_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['principal_access_boundary_policy']._loaded_options = None
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['principal_access_boundary_policy']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_GETPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy'
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['principal_access_boundary_policy']._loaded_options = None
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['principal_access_boundary_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy'
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120iam.googleapis.com/PrincipalAccessBoundaryPolicy'
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0iam.googleapis.com/PrincipalAccessBoundaryPolicy'
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x01'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES']._serialized_options = b'\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['CreatePrincipalAccessBoundaryPolicy']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['CreatePrincipalAccessBoundaryPolicy']._serialized_options = b'\xcaA2\n\x1dPrincipalAccessBoundaryPolicy\x12\x11OperationMetadata\xdaAKparent,principal_access_boundary_policy,principal_access_boundary_policy_id\x82\xd3\xe4\x93\x02l"H/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies: principal_access_boundary_policy'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['GetPrincipalAccessBoundaryPolicy']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['GetPrincipalAccessBoundaryPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['UpdatePrincipalAccessBoundaryPolicy']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['UpdatePrincipalAccessBoundaryPolicy']._serialized_options = b'\xcaA2\n\x1dPrincipalAccessBoundaryPolicy\x12\x11OperationMetadata\xdaA,principal_access_boundary_policy,update_mask\x82\xd3\xe4\x93\x02\x8d\x012i/v3/{principal_access_boundary_policy.name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}: principal_access_boundary_policy'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['DeletePrincipalAccessBoundaryPolicy']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['DeletePrincipalAccessBoundaryPolicy']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['ListPrincipalAccessBoundaryPolicies']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['ListPrincipalAccessBoundaryPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies'
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['SearchPrincipalAccessBoundaryPolicyBindings']._loaded_options = None
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES'].methods_by_name['SearchPrincipalAccessBoundaryPolicyBindings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02_\x12]/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}:searchPolicyBindings'
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_start = 447
    _globals['_CREATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_end = 736
    _globals['_GETPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_start = 738
    _globals['_GETPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_end = 851
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_start = 854
    _globals['_UPDATEPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_end = 1073
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_start = 1076
    _globals['_DELETEPRINCIPALACCESSBOUNDARYPOLICYREQUEST']._serialized_end = 1259
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST']._serialized_start = 1262
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESREQUEST']._serialized_end = 1429
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESRESPONSE']._serialized_start = 1432
    _globals['_LISTPRINCIPALACCESSBOUNDARYPOLICIESRESPONSE']._serialized_end = 1597
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST']._serialized_start = 1600
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSREQUEST']._serialized_end = 1773
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSRESPONSE']._serialized_start = 1776
    _globals['_SEARCHPRINCIPALACCESSBOUNDARYPOLICYBINDINGSRESPONSE']._serialized_end = 1914
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES']._serialized_start = 1917
    _globals['_PRINCIPALACCESSBOUNDARYPOLICIES']._serialized_end = 3817