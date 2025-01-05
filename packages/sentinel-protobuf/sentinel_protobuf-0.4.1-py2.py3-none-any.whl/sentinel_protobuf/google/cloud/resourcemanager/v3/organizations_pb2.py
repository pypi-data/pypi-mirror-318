"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/organizations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/resourcemanager/v3/organizations.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x04\n\x0cOrganization\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12$\n\x15directory_customer_id\x18\x03 \x01(\tB\x03\xe0A\x05H\x00\x12G\n\x05state\x18\x04 \x01(\x0e23.google.cloud.resourcemanager.v3.Organization.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x03"@\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x14\n\x10DELETE_REQUESTED\x10\x02:V\xeaAS\n0cloudresourcemanager.googleapis.com/Organization\x12\x1corganizations/{organization}R\x01\x01B\x07\n\x05owner"`\n\x16GetOrganizationRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization"a\n\x1aSearchOrganizationsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05query\x18\x03 \x01(\tB\x03\xe0A\x01"|\n\x1bSearchOrganizationsResponse\x12D\n\rorganizations\x18\x01 \x03(\x0b2-.google.cloud.resourcemanager.v3.Organization\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1c\n\x1aDeleteOrganizationMetadata"\x1e\n\x1cUndeleteOrganizationMetadata2\xe5\x07\n\rOrganizations\x12\xa4\x01\n\x0fGetOrganization\x127.google.cloud.resourcemanager.v3.GetOrganizationRequest\x1a-.google.cloud.resourcemanager.v3.Organization")\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v3/{name=organizations/*}\x12\xba\x01\n\x13SearchOrganizations\x12;.google.cloud.resourcemanager.v3.SearchOrganizationsRequest\x1a<.google.cloud.resourcemanager.v3.SearchOrganizationsResponse"(\xdaA\x05query\x82\xd3\xe4\x93\x02\x1a\x12\x18/v3/organizations:search\x12\x8c\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"A\xdaA\x08resource\x82\xd3\xe4\x93\x020"+/v3/{resource=organizations/*}:getIamPolicy:\x01*\x12\x8c\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"A\xdaA\x08resource\x82\xd3\xe4\x93\x020"+/v3/{resource=organizations/*}:setIamPolicy:\x01*\x12\xbe\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"S\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x026"1/v3/{resource=organizations/*}:testIamPermissions:\x01*\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xf3\x01\n#com.google.cloud.resourcemanager.v3B\x12OrganizationsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.organizations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\x12OrganizationsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_ORGANIZATION'].fields_by_name['name']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION'].fields_by_name['display_name']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION'].fields_by_name['directory_customer_id']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['directory_customer_id']._serialized_options = b'\xe0A\x05'
    _globals['_ORGANIZATION'].fields_by_name['state']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION'].fields_by_name['delete_time']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION'].fields_by_name['etag']._loaded_options = None
    _globals['_ORGANIZATION'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_ORGANIZATION']._loaded_options = None
    _globals['_ORGANIZATION']._serialized_options = b'\xeaAS\n0cloudresourcemanager.googleapis.com/Organization\x12\x1corganizations/{organization}R\x01\x01'
    _globals['_GETORGANIZATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORGANIZATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_SEARCHORGANIZATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHORGANIZATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHORGANIZATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHORGANIZATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHORGANIZATIONSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHORGANIZATIONSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_ORGANIZATIONS']._loaded_options = None
    _globals['_ORGANIZATIONS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_ORGANIZATIONS'].methods_by_name['GetOrganization']._loaded_options = None
    _globals['_ORGANIZATIONS'].methods_by_name['GetOrganization']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v3/{name=organizations/*}'
    _globals['_ORGANIZATIONS'].methods_by_name['SearchOrganizations']._loaded_options = None
    _globals['_ORGANIZATIONS'].methods_by_name['SearchOrganizations']._serialized_options = b'\xdaA\x05query\x82\xd3\xe4\x93\x02\x1a\x12\x18/v3/organizations:search'
    _globals['_ORGANIZATIONS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_ORGANIZATIONS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x020"+/v3/{resource=organizations/*}:getIamPolicy:\x01*'
    _globals['_ORGANIZATIONS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_ORGANIZATIONS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x020"+/v3/{resource=organizations/*}:setIamPolicy:\x01*'
    _globals['_ORGANIZATIONS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_ORGANIZATIONS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x026"1/v3/{resource=organizations/*}:testIamPermissions:\x01*'
    _globals['_ORGANIZATION']._serialized_start = 297
    _globals['_ORGANIZATION']._serialized_end = 812
    _globals['_ORGANIZATION_STATE']._serialized_start = 651
    _globals['_ORGANIZATION_STATE']._serialized_end = 715
    _globals['_GETORGANIZATIONREQUEST']._serialized_start = 814
    _globals['_GETORGANIZATIONREQUEST']._serialized_end = 910
    _globals['_SEARCHORGANIZATIONSREQUEST']._serialized_start = 912
    _globals['_SEARCHORGANIZATIONSREQUEST']._serialized_end = 1009
    _globals['_SEARCHORGANIZATIONSRESPONSE']._serialized_start = 1011
    _globals['_SEARCHORGANIZATIONSRESPONSE']._serialized_end = 1135
    _globals['_DELETEORGANIZATIONMETADATA']._serialized_start = 1137
    _globals['_DELETEORGANIZATIONMETADATA']._serialized_end = 1165
    _globals['_UNDELETEORGANIZATIONMETADATA']._serialized_start = 1167
    _globals['_UNDELETEORGANIZATIONMETADATA']._serialized_end = 1197
    _globals['_ORGANIZATIONS']._serialized_start = 1200
    _globals['_ORGANIZATIONS']._serialized_end = 2197