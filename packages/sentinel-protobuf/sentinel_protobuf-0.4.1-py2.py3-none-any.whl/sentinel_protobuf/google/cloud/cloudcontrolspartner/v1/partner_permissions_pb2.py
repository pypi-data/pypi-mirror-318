"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1/partner_permissions.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/cloudcontrolspartner/v1/partner_permissions.proto\x12$google.cloud.cloudcontrolspartner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb5\x04\n\x12PartnerPermissions\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12`\n\x13partner_permissions\x18\x02 \x03(\x0e2C.google.cloud.cloudcontrolspartner.v1.PartnerPermissions.Permission"\xfa\x01\n\nPermission\x12\x1a\n\x16PERMISSION_UNSPECIFIED\x10\x00\x121\n-ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS\x10\x01\x12 \n\x1cASSURED_WORKLOADS_MONITORING\x10\x02\x12\x1c\n\x18ACCESS_APPROVAL_REQUESTS\x10\x03\x12+\n\'ASSURED_WORKLOADS_EKM_CONNECTION_STATUS\x10\x04\x120\n,ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER\x10\x05:\xac\x01\xeaA\xa8\x01\n6cloudcontrolspartner.googleapis.com/PartnerPermissions\x12norganizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions"l\n\x1cGetPartnerPermissionsRequest\x12L\n\x04name\x18\x01 \x01(\tB>\xe0A\x02\xfaA8\n6cloudcontrolspartner.googleapis.com/PartnerPermissionsB\x9b\x02\n(com.google.cloud.cloudcontrolspartner.v1B\x17PartnerPermissionsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02\'Google::Cloud::CloudControlsPartner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1.partner_permissions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.cloudcontrolspartner.v1B\x17PartnerPermissionsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02'Google::Cloud::CloudControlsPartner::V1"
    _globals['_PARTNERPERMISSIONS'].fields_by_name['name']._loaded_options = None
    _globals['_PARTNERPERMISSIONS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PARTNERPERMISSIONS']._loaded_options = None
    _globals['_PARTNERPERMISSIONS']._serialized_options = b'\xeaA\xa8\x01\n6cloudcontrolspartner.googleapis.com/PartnerPermissions\x12norganizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions'
    _globals['_GETPARTNERPERMISSIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPARTNERPERMISSIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA8\n6cloudcontrolspartner.googleapis.com/PartnerPermissions'
    _globals['_PARTNERPERMISSIONS']._serialized_start = 165
    _globals['_PARTNERPERMISSIONS']._serialized_end = 730
    _globals['_PARTNERPERMISSIONS_PERMISSION']._serialized_start = 305
    _globals['_PARTNERPERMISSIONS_PERMISSION']._serialized_end = 555
    _globals['_GETPARTNERPERMISSIONSREQUEST']._serialized_start = 732
    _globals['_GETPARTNERPERMISSIONSREQUEST']._serialized_end = 840