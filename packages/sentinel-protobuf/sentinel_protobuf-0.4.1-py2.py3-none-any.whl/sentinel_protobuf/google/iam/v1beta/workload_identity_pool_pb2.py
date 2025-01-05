"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v1beta/workload_identity_pool.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/iam/v1beta/workload_identity_pool.proto\x12\x11google.iam.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto"\xea\x02\n\x14WorkloadIdentityPool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12A\n\x05state\x18\x04 \x01(\x0e2-.google.iam.v1beta.WorkloadIdentityPool.StateB\x03\xe0A\x03\x12\x10\n\x08disabled\x18\x05 \x01(\x08"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07DELETED\x10\x02:\x85\x01\xeaA\x81\x01\n\'iam.googleapis.com/WorkloadIdentityPool\x12Vprojects/{project}/locations/{location}/workloadIdentityPools/{workload_identity_pool}"\xe0\x06\n\x1cWorkloadIdentityPoolProvider\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12I\n\x05state\x18\x04 \x01(\x0e25.google.iam.v1beta.WorkloadIdentityPoolProvider.StateB\x03\xe0A\x03\x12\x10\n\x08disabled\x18\x05 \x01(\x08\x12`\n\x11attribute_mapping\x18\x06 \x03(\x0b2E.google.iam.v1beta.WorkloadIdentityPoolProvider.AttributeMappingEntry\x12\x1b\n\x13attribute_condition\x18\x07 \x01(\t\x12B\n\x03aws\x18\x08 \x01(\x0b23.google.iam.v1beta.WorkloadIdentityPoolProvider.AwsH\x00\x12D\n\x04oidc\x18\t \x01(\x0b24.google.iam.v1beta.WorkloadIdentityPoolProvider.OidcH\x00\x1a\x1e\n\x03Aws\x12\x17\n\naccount_id\x18\x01 \x01(\tB\x03\xe0A\x02\x1a:\n\x04Oidc\x12\x17\n\nissuer_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x11allowed_audiences\x18\x02 \x03(\t\x1a7\n\x15AttributeMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07DELETED\x10\x02:\xba\x01\xeaA\xb6\x01\n/iam.googleapis.com/WorkloadIdentityPoolProvider\x12\x82\x01projects/{project}/locations/{location}/workloadIdentityPools/{workload_identity_pool}/providers/{workload_identity_pool_provider}B\x11\n\x0fprovider_config"\xa4\x01\n ListWorkloadIdentityPoolsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x14\n\x0cshow_deleted\x18\x04 \x01(\x08"\x86\x01\n!ListWorkloadIdentityPoolsResponse\x12H\n\x17workload_identity_pools\x18\x01 \x03(\x0b2\'.google.iam.v1beta.WorkloadIdentityPool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"_\n\x1eGetWorkloadIdentityPoolRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'iam.googleapis.com/WorkloadIdentityPool"\xde\x01\n!CreateWorkloadIdentityPoolRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12L\n\x16workload_identity_pool\x18\x02 \x01(\x0b2\'.google.iam.v1beta.WorkloadIdentityPoolB\x03\xe0A\x02\x12&\n\x19workload_identity_pool_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xa7\x01\n!UpdateWorkloadIdentityPoolRequest\x12L\n\x16workload_identity_pool\x18\x01 \x01(\x0b2\'.google.iam.v1beta.WorkloadIdentityPoolB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"b\n!DeleteWorkloadIdentityPoolRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'iam.googleapis.com/WorkloadIdentityPool"d\n#UndeleteWorkloadIdentityPoolRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'iam.googleapis.com/WorkloadIdentityPool"\xa8\x01\n(ListWorkloadIdentityPoolProvidersRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'iam.googleapis.com/WorkloadIdentityPool\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x14\n\x0cshow_deleted\x18\x04 \x01(\x08"\x9f\x01\n)ListWorkloadIdentityPoolProvidersResponse\x12Y\n workload_identity_pool_providers\x18\x01 \x03(\x0b2/.google.iam.v1beta.WorkloadIdentityPoolProvider\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"o\n&GetWorkloadIdentityPoolProviderRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/iam.googleapis.com/WorkloadIdentityPoolProvider"\xfc\x01\n)CreateWorkloadIdentityPoolProviderRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'iam.googleapis.com/WorkloadIdentityPool\x12]\n\x1fworkload_identity_pool_provider\x18\x02 \x01(\x0b2/.google.iam.v1beta.WorkloadIdentityPoolProviderB\x03\xe0A\x02\x12/\n"workload_identity_pool_provider_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xc0\x01\n)UpdateWorkloadIdentityPoolProviderRequest\x12]\n\x1fworkload_identity_pool_provider\x18\x01 \x01(\x0b2/.google.iam.v1beta.WorkloadIdentityPoolProviderB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"r\n)DeleteWorkloadIdentityPoolProviderRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/iam.googleapis.com/WorkloadIdentityPoolProvider"t\n+UndeleteWorkloadIdentityPoolProviderRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/iam.googleapis.com/WorkloadIdentityPoolProvider"\'\n%WorkloadIdentityPoolOperationMetadata"/\n-WorkloadIdentityPoolProviderOperationMetadata2\xb4\x1c\n\x15WorkloadIdentityPools\x12\xd6\x01\n\x19ListWorkloadIdentityPools\x123.google.iam.v1beta.ListWorkloadIdentityPoolsRequest\x1a4.google.iam.v1beta.ListWorkloadIdentityPoolsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/locations/*}/workloadIdentityPools\x12\xc3\x01\n\x17GetWorkloadIdentityPool\x121.google.iam.v1beta.GetWorkloadIdentityPoolRequest\x1a\'.google.iam.v1beta.WorkloadIdentityPool"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}\x12\xcb\x02\n\x1aCreateWorkloadIdentityPool\x124.google.iam.v1beta.CreateWorkloadIdentityPoolRequest\x1a\x1d.google.longrunning.Operation"\xd7\x01\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA7parent,workload_identity_pool,workload_identity_pool_id\x82\xd3\xe4\x93\x02W"=/v1beta/{parent=projects/*/locations/*}/workloadIdentityPools:\x16workload_identity_pool\x12\xcd\x02\n\x1aUpdateWorkloadIdentityPool\x124.google.iam.v1beta.UpdateWorkloadIdentityPoolRequest\x1a\x1d.google.longrunning.Operation"\xd9\x01\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA"workload_identity_pool,update_mask\x82\xd3\xe4\x93\x02n2T/v1beta/{workload_identity_pool.name=projects/*/locations/*/workloadIdentityPools/*}:\x16workload_identity_pool\x12\x80\x02\n\x1aDeleteWorkloadIdentityPool\x124.google.iam.v1beta.DeleteWorkloadIdentityPoolRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}\x12\x90\x02\n\x1cUndeleteWorkloadIdentityPool\x126.google.iam.v1beta.UndeleteWorkloadIdentityPoolRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02K"F/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}:undelete:\x01*\x12\xfa\x01\n!ListWorkloadIdentityPoolProviders\x12;.google.iam.v1beta.ListWorkloadIdentityPoolProvidersRequest\x1a<.google.iam.v1beta.ListWorkloadIdentityPoolProvidersResponse"Z\xdaA\x06parent\x82\xd3\xe4\x93\x02K\x12I/v1beta/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers\x12\xe7\x01\n\x1fGetWorkloadIdentityPoolProvider\x129.google.iam.v1beta.GetWorkloadIdentityPoolProviderRequest\x1a/.google.iam.v1beta.WorkloadIdentityPoolProvider"X\xdaA\x04name\x82\xd3\xe4\x93\x02K\x12I/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}\x12\x92\x03\n"CreateWorkloadIdentityPoolProvider\x12<.google.iam.v1beta.CreateWorkloadIdentityPoolProviderRequest\x1a\x1d.google.longrunning.Operation"\x8e\x02\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaAIparent,workload_identity_pool_provider,workload_identity_pool_provider_id\x82\xd3\xe4\x93\x02l"I/v1beta/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers:\x1fworkload_identity_pool_provider\x12\x95\x03\n"UpdateWorkloadIdentityPoolProvider\x12<.google.iam.v1beta.UpdateWorkloadIdentityPoolProviderRequest\x1a\x1d.google.longrunning.Operation"\x91\x02\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaA+workload_identity_pool_provider,update_mask\x82\xd3\xe4\x93\x02\x8c\x012i/v1beta/{workload_identity_pool_provider.name=projects/*/locations/*/workloadIdentityPools/*/providers/*}:\x1fworkload_identity_pool_provider\x12\xac\x02\n"DeleteWorkloadIdentityPoolProvider\x12<.google.iam.v1beta.DeleteWorkloadIdentityPoolProviderRequest\x1a\x1d.google.longrunning.Operation"\xa8\x01\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02K*I/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}\x12\xbc\x02\n$UndeleteWorkloadIdentityPoolProvider\x12>.google.iam.v1beta.UndeleteWorkloadIdentityPoolProviderRequest\x1a\x1d.google.longrunning.Operation"\xb4\x01\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02W"R/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}:undelete:\x01*\x1aF\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBc\n\x15com.google.iam.v1betaB\x19WorkloadIdentityPoolProtoP\x01Z-cloud.google.com/go/iam/apiv1beta/iampb;iampbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v1beta.workload_identity_pool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.iam.v1betaB\x19WorkloadIdentityPoolProtoP\x01Z-cloud.google.com/go/iam/apiv1beta/iampb;iampb'
    _globals['_WORKLOADIDENTITYPOOL'].fields_by_name['name']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADIDENTITYPOOL'].fields_by_name['state']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADIDENTITYPOOL']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOL']._serialized_options = b"\xeaA\x81\x01\n'iam.googleapis.com/WorkloadIdentityPool\x12Vprojects/{project}/locations/{location}/workloadIdentityPools/{workload_identity_pool}"
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_AWS'].fields_by_name['account_id']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_AWS'].fields_by_name['account_id']._serialized_options = b'\xe0A\x02'
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_OIDC'].fields_by_name['issuer_uri']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_OIDC'].fields_by_name['issuer_uri']._serialized_options = b'\xe0A\x02'
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_ATTRIBUTEMAPPINGENTRY']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_ATTRIBUTEMAPPINGENTRY']._serialized_options = b'8\x01'
    _globals['_WORKLOADIDENTITYPOOLPROVIDER'].fields_by_name['name']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLPROVIDER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADIDENTITYPOOLPROVIDER'].fields_by_name['state']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLPROVIDER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_WORKLOADIDENTITYPOOLPROVIDER']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLPROVIDER']._serialized_options = b'\xeaA\xb6\x01\n/iam.googleapis.com/WorkloadIdentityPoolProvider\x12\x82\x01projects/{project}/locations/{location}/workloadIdentityPools/{workload_identity_pool}/providers/{workload_identity_pool_provider}'
    _globals['_LISTWORKLOADIDENTITYPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWORKLOADIDENTITYPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_GETWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'iam.googleapis.com/WorkloadIdentityPool"
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['workload_identity_pool']._loaded_options = None
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['workload_identity_pool']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['workload_identity_pool_id']._loaded_options = None
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['workload_identity_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['workload_identity_pool']._loaded_options = None
    _globals['_UPDATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['workload_identity_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'iam.googleapis.com/WorkloadIdentityPool"
    _globals['_UNDELETEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETEWORKLOADIDENTITYPOOLREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'iam.googleapis.com/WorkloadIdentityPool"
    _globals['_LISTWORKLOADIDENTITYPOOLPROVIDERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWORKLOADIDENTITYPOOLPROVIDERSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'iam.googleapis.com/WorkloadIdentityPool"
    _globals['_GETWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/iam.googleapis.com/WorkloadIdentityPoolProvider'
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'iam.googleapis.com/WorkloadIdentityPool"
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['workload_identity_pool_provider']._loaded_options = None
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['workload_identity_pool_provider']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['workload_identity_pool_provider_id']._loaded_options = None
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['workload_identity_pool_provider_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['workload_identity_pool_provider']._loaded_options = None
    _globals['_UPDATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['workload_identity_pool_provider']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/iam.googleapis.com/WorkloadIdentityPoolProvider'
    _globals['_UNDELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/iam.googleapis.com/WorkloadIdentityPoolProvider'
    _globals['_WORKLOADIDENTITYPOOLS']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS']._serialized_options = b'\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['ListWorkloadIdentityPools']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['ListWorkloadIdentityPools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/locations/*}/workloadIdentityPools'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['GetWorkloadIdentityPool']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['GetWorkloadIdentityPool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['CreateWorkloadIdentityPool']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['CreateWorkloadIdentityPool']._serialized_options = b'\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA7parent,workload_identity_pool,workload_identity_pool_id\x82\xd3\xe4\x93\x02W"=/v1beta/{parent=projects/*/locations/*}/workloadIdentityPools:\x16workload_identity_pool'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UpdateWorkloadIdentityPool']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UpdateWorkloadIdentityPool']._serialized_options = b'\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA"workload_identity_pool,update_mask\x82\xd3\xe4\x93\x02n2T/v1beta/{workload_identity_pool.name=projects/*/locations/*/workloadIdentityPools/*}:\x16workload_identity_pool'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['DeleteWorkloadIdentityPool']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['DeleteWorkloadIdentityPool']._serialized_options = b'\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UndeleteWorkloadIdentityPool']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UndeleteWorkloadIdentityPool']._serialized_options = b'\xcaA=\n\x14WorkloadIdentityPool\x12%WorkloadIdentityPoolOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02K"F/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*}:undelete:\x01*'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['ListWorkloadIdentityPoolProviders']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['ListWorkloadIdentityPoolProviders']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02K\x12I/v1beta/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['GetWorkloadIdentityPoolProvider']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['GetWorkloadIdentityPoolProvider']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02K\x12I/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['CreateWorkloadIdentityPoolProvider']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['CreateWorkloadIdentityPoolProvider']._serialized_options = b'\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaAIparent,workload_identity_pool_provider,workload_identity_pool_provider_id\x82\xd3\xe4\x93\x02l"I/v1beta/{parent=projects/*/locations/*/workloadIdentityPools/*}/providers:\x1fworkload_identity_pool_provider'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UpdateWorkloadIdentityPoolProvider']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UpdateWorkloadIdentityPoolProvider']._serialized_options = b'\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaA+workload_identity_pool_provider,update_mask\x82\xd3\xe4\x93\x02\x8c\x012i/v1beta/{workload_identity_pool_provider.name=projects/*/locations/*/workloadIdentityPools/*/providers/*}:\x1fworkload_identity_pool_provider'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['DeleteWorkloadIdentityPoolProvider']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['DeleteWorkloadIdentityPoolProvider']._serialized_options = b'\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02K*I/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}'
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UndeleteWorkloadIdentityPoolProvider']._loaded_options = None
    _globals['_WORKLOADIDENTITYPOOLS'].methods_by_name['UndeleteWorkloadIdentityPoolProvider']._serialized_options = b'\xcaAM\n\x1cWorkloadIdentityPoolProvider\x12-WorkloadIdentityPoolProviderOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02W"R/v1beta/{name=projects/*/locations/*/workloadIdentityPools/*/providers/*}:undelete:\x01*'
    _globals['_WORKLOADIDENTITYPOOL']._serialized_start = 256
    _globals['_WORKLOADIDENTITYPOOL']._serialized_end = 618
    _globals['_WORKLOADIDENTITYPOOL_STATE']._serialized_start = 427
    _globals['_WORKLOADIDENTITYPOOL_STATE']._serialized_end = 482
    _globals['_WORKLOADIDENTITYPOOLPROVIDER']._serialized_start = 621
    _globals['_WORKLOADIDENTITYPOOLPROVIDER']._serialized_end = 1485
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_AWS']._serialized_start = 1073
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_AWS']._serialized_end = 1103
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_OIDC']._serialized_start = 1105
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_OIDC']._serialized_end = 1163
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_ATTRIBUTEMAPPINGENTRY']._serialized_start = 1165
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_ATTRIBUTEMAPPINGENTRY']._serialized_end = 1220
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_STATE']._serialized_start = 427
    _globals['_WORKLOADIDENTITYPOOLPROVIDER_STATE']._serialized_end = 482
    _globals['_LISTWORKLOADIDENTITYPOOLSREQUEST']._serialized_start = 1488
    _globals['_LISTWORKLOADIDENTITYPOOLSREQUEST']._serialized_end = 1652
    _globals['_LISTWORKLOADIDENTITYPOOLSRESPONSE']._serialized_start = 1655
    _globals['_LISTWORKLOADIDENTITYPOOLSRESPONSE']._serialized_end = 1789
    _globals['_GETWORKLOADIDENTITYPOOLREQUEST']._serialized_start = 1791
    _globals['_GETWORKLOADIDENTITYPOOLREQUEST']._serialized_end = 1886
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST']._serialized_start = 1889
    _globals['_CREATEWORKLOADIDENTITYPOOLREQUEST']._serialized_end = 2111
    _globals['_UPDATEWORKLOADIDENTITYPOOLREQUEST']._serialized_start = 2114
    _globals['_UPDATEWORKLOADIDENTITYPOOLREQUEST']._serialized_end = 2281
    _globals['_DELETEWORKLOADIDENTITYPOOLREQUEST']._serialized_start = 2283
    _globals['_DELETEWORKLOADIDENTITYPOOLREQUEST']._serialized_end = 2381
    _globals['_UNDELETEWORKLOADIDENTITYPOOLREQUEST']._serialized_start = 2383
    _globals['_UNDELETEWORKLOADIDENTITYPOOLREQUEST']._serialized_end = 2483
    _globals['_LISTWORKLOADIDENTITYPOOLPROVIDERSREQUEST']._serialized_start = 2486
    _globals['_LISTWORKLOADIDENTITYPOOLPROVIDERSREQUEST']._serialized_end = 2654
    _globals['_LISTWORKLOADIDENTITYPOOLPROVIDERSRESPONSE']._serialized_start = 2657
    _globals['_LISTWORKLOADIDENTITYPOOLPROVIDERSRESPONSE']._serialized_end = 2816
    _globals['_GETWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_start = 2818
    _globals['_GETWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_end = 2929
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_start = 2932
    _globals['_CREATEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_end = 3184
    _globals['_UPDATEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_start = 3187
    _globals['_UPDATEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_end = 3379
    _globals['_DELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_start = 3381
    _globals['_DELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_end = 3495
    _globals['_UNDELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_start = 3497
    _globals['_UNDELETEWORKLOADIDENTITYPOOLPROVIDERREQUEST']._serialized_end = 3613
    _globals['_WORKLOADIDENTITYPOOLOPERATIONMETADATA']._serialized_start = 3615
    _globals['_WORKLOADIDENTITYPOOLOPERATIONMETADATA']._serialized_end = 3654
    _globals['_WORKLOADIDENTITYPOOLPROVIDEROPERATIONMETADATA']._serialized_start = 3656
    _globals['_WORKLOADIDENTITYPOOLPROVIDEROPERATIONMETADATA']._serialized_end = 3703
    _globals['_WORKLOADIDENTITYPOOLS']._serialized_start = 3706
    _globals['_WORKLOADIDENTITYPOOLS']._serialized_end = 7342