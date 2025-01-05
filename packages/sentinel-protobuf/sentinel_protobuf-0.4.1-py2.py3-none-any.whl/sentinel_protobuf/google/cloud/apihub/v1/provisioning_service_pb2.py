"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apihub/v1/provisioning_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apihub.v1 import common_fields_pb2 as google_dot_cloud_dot_apihub_dot_v1_dot_common__fields__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/apihub/v1/provisioning_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/apihub/v1/common_fields.proto\x1a#google/longrunning/operations.proto"\xc1\x01\n\x1bCreateApiHubInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12 \n\x13api_hub_instance_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12E\n\x10api_hub_instance\x18\x03 \x01(\x0b2&.google.cloud.apihub.v1.ApiHubInstanceB\x03\xe0A\x02"V\n\x18GetApiHubInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$apihub.googleapis.com/ApiHubInstance"[\n\x1bLookupApiHubInstanceRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$apihub.googleapis.com/ApiHubInstance"`\n\x1cLookupApiHubInstanceResponse\x12@\n\x10api_hub_instance\x18\x01 \x01(\x0b2&.google.cloud.apihub.v1.ApiHubInstance2\xef\x05\n\x0cProvisioning\x12\x8e\x02\n\x14CreateApiHubInstance\x123.google.cloud.apihub.v1.CreateApiHubInstanceRequest\x1a\x1d.google.longrunning.Operation"\xa1\x01\xcaA#\n\x0eApiHubInstance\x12\x11OperationMetadata\xdaA+parent,api_hub_instance,api_hub_instance_id\x82\xd3\xe4\x93\x02G"3/v1/{parent=projects/*/locations/*}/apiHubInstances:\x10api_hub_instance\x12\xb1\x01\n\x11GetApiHubInstance\x120.google.cloud.apihub.v1.GetApiHubInstanceRequest\x1a&.google.cloud.apihub.v1.ApiHubInstance"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/apiHubInstances/*}\x12\xce\x01\n\x14LookupApiHubInstance\x123.google.cloud.apihub.v1.LookupApiHubInstanceRequest\x1a4.google.cloud.apihub.v1.LookupApiHubInstanceResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*}/apiHubInstances:lookup\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xba\x01\n\x1acom.google.cloud.apihub.v1B\x18ProvisioningServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.provisioning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x18ProvisioningServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance_id']._loaded_options = None
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance']._loaded_options = None
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance']._serialized_options = b'\xe0A\x02'
    _globals['_GETAPIHUBINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAPIHUBINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$apihub.googleapis.com/ApiHubInstance'
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$apihub.googleapis.com/ApiHubInstance'
    _globals['_PROVISIONING']._loaded_options = None
    _globals['_PROVISIONING']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROVISIONING'].methods_by_name['CreateApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['CreateApiHubInstance']._serialized_options = b'\xcaA#\n\x0eApiHubInstance\x12\x11OperationMetadata\xdaA+parent,api_hub_instance,api_hub_instance_id\x82\xd3\xe4\x93\x02G"3/v1/{parent=projects/*/locations/*}/apiHubInstances:\x10api_hub_instance'
    _globals['_PROVISIONING'].methods_by_name['GetApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['GetApiHubInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/apiHubInstances/*}'
    _globals['_PROVISIONING'].methods_by_name['LookupApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['LookupApiHubInstance']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*}/apiHubInstances:lookup'
    _globals['_CREATEAPIHUBINSTANCEREQUEST']._serialized_start = 274
    _globals['_CREATEAPIHUBINSTANCEREQUEST']._serialized_end = 467
    _globals['_GETAPIHUBINSTANCEREQUEST']._serialized_start = 469
    _globals['_GETAPIHUBINSTANCEREQUEST']._serialized_end = 555
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST']._serialized_start = 557
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST']._serialized_end = 648
    _globals['_LOOKUPAPIHUBINSTANCERESPONSE']._serialized_start = 650
    _globals['_LOOKUPAPIHUBINSTANCERESPONSE']._serialized_end = 746
    _globals['_PROVISIONING']._serialized_start = 749
    _globals['_PROVISIONING']._serialized_end = 1500