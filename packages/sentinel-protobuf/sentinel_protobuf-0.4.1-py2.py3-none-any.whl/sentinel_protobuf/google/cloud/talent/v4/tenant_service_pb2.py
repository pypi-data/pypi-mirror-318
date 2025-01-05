"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/tenant_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4 import common_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_common__pb2
from .....google.cloud.talent.v4 import tenant_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_tenant__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/talent/v4/tenant_service.proto\x12\x16google.cloud.talent.v4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/talent/v4/common.proto\x1a#google/cloud/talent/v4/tenant.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x8f\x01\n\x13CreateTenantRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x123\n\x06tenant\x18\x02 \x01(\x0b2\x1e.google.cloud.talent.v4.TenantB\x03\xe0A\x02"D\n\x10GetTenantRequest\x120\n\x04name\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant"{\n\x13UpdateTenantRequest\x123\n\x06tenant\x18\x01 \x01(\x0b2\x1e.google.cloud.talent.v4.TenantB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"G\n\x13DeleteTenantRequest\x120\n\x04name\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant"\x80\x01\n\x12ListTenantsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\x9b\x01\n\x13ListTenantsResponse\x12/\n\x07tenants\x18\x01 \x03(\x0b2\x1e.google.cloud.talent.v4.Tenant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12:\n\x08metadata\x18\x03 \x01(\x0b2(.google.cloud.talent.v4.ResponseMetadata2\xf0\x06\n\rTenantService\x12\x9c\x01\n\x0cCreateTenant\x12+.google.cloud.talent.v4.CreateTenantRequest\x1a\x1e.google.cloud.talent.v4.Tenant"?\xdaA\rparent,tenant\x82\xd3\xe4\x93\x02)"\x1f/v4/{parent=projects/*}/tenants:\x06tenant\x12\x85\x01\n\tGetTenant\x12(.google.cloud.talent.v4.GetTenantRequest\x1a\x1e.google.cloud.talent.v4.Tenant".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v4/{name=projects/*/tenants/*}\x12\xa8\x01\n\x0cUpdateTenant\x12+.google.cloud.talent.v4.UpdateTenantRequest\x1a\x1e.google.cloud.talent.v4.Tenant"K\xdaA\x12tenant,update_mask\x82\xd3\xe4\x93\x0202&/v4/{tenant.name=projects/*/tenants/*}:\x06tenant\x12\x83\x01\n\x0cDeleteTenant\x12+.google.cloud.talent.v4.DeleteTenantRequest\x1a\x16.google.protobuf.Empty".\xdaA\x04name\x82\xd3\xe4\x93\x02!*\x1f/v4/{name=projects/*/tenants/*}\x12\x98\x01\n\x0bListTenants\x12*.google.cloud.talent.v4.ListTenantsRequest\x1a+.google.cloud.talent.v4.ListTenantsResponse"0\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v4/{parent=projects/*}/tenants\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBl\n\x1acom.google.cloud.talent.v4B\x12TenantServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.tenant_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x12TenantServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_CREATETENANTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETENANTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATETENANTREQUEST'].fields_by_name['tenant']._loaded_options = None
    _globals['_CREATETENANTREQUEST'].fields_by_name['tenant']._serialized_options = b'\xe0A\x02'
    _globals['_GETTENANTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTENANTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant'
    _globals['_UPDATETENANTREQUEST'].fields_by_name['tenant']._loaded_options = None
    _globals['_UPDATETENANTREQUEST'].fields_by_name['tenant']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETENANTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETENANTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant'
    _globals['_LISTTENANTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTENANTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_TENANTSERVICE']._loaded_options = None
    _globals['_TENANTSERVICE']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_TENANTSERVICE'].methods_by_name['CreateTenant']._loaded_options = None
    _globals['_TENANTSERVICE'].methods_by_name['CreateTenant']._serialized_options = b'\xdaA\rparent,tenant\x82\xd3\xe4\x93\x02)"\x1f/v4/{parent=projects/*}/tenants:\x06tenant'
    _globals['_TENANTSERVICE'].methods_by_name['GetTenant']._loaded_options = None
    _globals['_TENANTSERVICE'].methods_by_name['GetTenant']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v4/{name=projects/*/tenants/*}'
    _globals['_TENANTSERVICE'].methods_by_name['UpdateTenant']._loaded_options = None
    _globals['_TENANTSERVICE'].methods_by_name['UpdateTenant']._serialized_options = b'\xdaA\x12tenant,update_mask\x82\xd3\xe4\x93\x0202&/v4/{tenant.name=projects/*/tenants/*}:\x06tenant'
    _globals['_TENANTSERVICE'].methods_by_name['DeleteTenant']._loaded_options = None
    _globals['_TENANTSERVICE'].methods_by_name['DeleteTenant']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!*\x1f/v4/{name=projects/*/tenants/*}'
    _globals['_TENANTSERVICE'].methods_by_name['ListTenants']._loaded_options = None
    _globals['_TENANTSERVICE'].methods_by_name['ListTenants']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v4/{parent=projects/*}/tenants'
    _globals['_CREATETENANTREQUEST']._serialized_start = 324
    _globals['_CREATETENANTREQUEST']._serialized_end = 467
    _globals['_GETTENANTREQUEST']._serialized_start = 469
    _globals['_GETTENANTREQUEST']._serialized_end = 537
    _globals['_UPDATETENANTREQUEST']._serialized_start = 539
    _globals['_UPDATETENANTREQUEST']._serialized_end = 662
    _globals['_DELETETENANTREQUEST']._serialized_start = 664
    _globals['_DELETETENANTREQUEST']._serialized_end = 735
    _globals['_LISTTENANTSREQUEST']._serialized_start = 738
    _globals['_LISTTENANTSREQUEST']._serialized_end = 866
    _globals['_LISTTENANTSRESPONSE']._serialized_start = 869
    _globals['_LISTTENANTSRESPONSE']._serialized_end = 1024
    _globals['_TENANTSERVICE']._serialized_start = 1027
    _globals['_TENANTSERVICE']._serialized_end = 1907