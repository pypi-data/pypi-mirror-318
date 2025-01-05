"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkservices/v1beta1/network_services.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.networkservices.v1beta1 import endpoint_policy_pb2 as google_dot_cloud_dot_networkservices_dot_v1beta1_dot_endpoint__policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/networkservices/v1beta1/network_services.proto\x12$google.cloud.networkservices.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a:google/cloud/networkservices/v1beta1/endpoint_policy.proto\x1a#google/longrunning/operations.proto2\xcf\x0b\n\x0fNetworkServices\x12\xe9\x01\n\x14ListEndpointPolicies\x12A.google.cloud.networkservices.v1beta1.ListEndpointPoliciesRequest\x1aB.google.cloud.networkservices.v1beta1.ListEndpointPoliciesResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1beta1/{parent=projects/*/locations/*}/endpointPolicies\x12\xd3\x01\n\x11GetEndpointPolicy\x12>.google.cloud.networkservices.v1beta1.GetEndpointPolicyRequest\x1a4.google.cloud.networkservices.v1beta1.EndpointPolicy"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1beta1/{name=projects/*/locations/*/endpointPolicies/*}\x12\xc4\x02\n\x14CreateEndpointPolicy\x12A.google.cloud.networkservices.v1beta1.CreateEndpointPolicyRequest\x1a\x1d.google.longrunning.Operation"\xc9\x01\xcaAH\n\x0eEndpointPolicy\x126google.cloud.networkservices.v1beta1.OperationMetadata\xdaA)parent,endpoint_policy,endpoint_policy_id\x82\xd3\xe4\x93\x02L"9/v1beta1/{parent=projects/*/locations/*}/endpointPolicies:\x0fendpoint_policy\x12\xc6\x02\n\x14UpdateEndpointPolicy\x12A.google.cloud.networkservices.v1beta1.UpdateEndpointPolicyRequest\x1a\x1d.google.longrunning.Operation"\xcb\x01\xcaAH\n\x0eEndpointPolicy\x126google.cloud.networkservices.v1beta1.OperationMetadata\xdaA\x1bendpoint_policy,update_mask\x82\xd3\xe4\x93\x02\\2I/v1beta1/{endpoint_policy.name=projects/*/locations/*/endpointPolicies/*}:\x0fendpoint_policy\x12\x95\x02\n\x14DeleteEndpointPolicy\x12A.google.cloud.networkservices.v1beta1.DeleteEndpointPolicyRequest\x1a\x1d.google.longrunning.Operation"\x9a\x01\xcaAO\n\x15google.protobuf.Empty\x126google.cloud.networkservices.v1beta1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1beta1/{name=projects/*/locations/*/endpointPolicies/*}\x1aR\xcaA\x1enetworkservices.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf8\x01\n(com.google.cloud.networkservices.v1beta1P\x01ZRcloud.google.com/go/networkservices/apiv1beta1/networkservicespb;networkservicespb\xaa\x02$Google.Cloud.NetworkServices.V1Beta1\xca\x02$Google\\Cloud\\NetworkServices\\V1beta1\xea\x02\'Google::Cloud::NetworkServices::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1beta1.network_services_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.networkservices.v1beta1P\x01ZRcloud.google.com/go/networkservices/apiv1beta1/networkservicespb;networkservicespb\xaa\x02$Google.Cloud.NetworkServices.V1Beta1\xca\x02$Google\\Cloud\\NetworkServices\\V1beta1\xea\x02'Google::Cloud::NetworkServices::V1beta1"
    _globals['_NETWORKSERVICES']._loaded_options = None
    _globals['_NETWORKSERVICES']._serialized_options = b'\xcaA\x1enetworkservices.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_NETWORKSERVICES'].methods_by_name['ListEndpointPolicies']._loaded_options = None
    _globals['_NETWORKSERVICES'].methods_by_name['ListEndpointPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1beta1/{parent=projects/*/locations/*}/endpointPolicies'
    _globals['_NETWORKSERVICES'].methods_by_name['GetEndpointPolicy']._loaded_options = None
    _globals['_NETWORKSERVICES'].methods_by_name['GetEndpointPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1beta1/{name=projects/*/locations/*/endpointPolicies/*}'
    _globals['_NETWORKSERVICES'].methods_by_name['CreateEndpointPolicy']._loaded_options = None
    _globals['_NETWORKSERVICES'].methods_by_name['CreateEndpointPolicy']._serialized_options = b'\xcaAH\n\x0eEndpointPolicy\x126google.cloud.networkservices.v1beta1.OperationMetadata\xdaA)parent,endpoint_policy,endpoint_policy_id\x82\xd3\xe4\x93\x02L"9/v1beta1/{parent=projects/*/locations/*}/endpointPolicies:\x0fendpoint_policy'
    _globals['_NETWORKSERVICES'].methods_by_name['UpdateEndpointPolicy']._loaded_options = None
    _globals['_NETWORKSERVICES'].methods_by_name['UpdateEndpointPolicy']._serialized_options = b'\xcaAH\n\x0eEndpointPolicy\x126google.cloud.networkservices.v1beta1.OperationMetadata\xdaA\x1bendpoint_policy,update_mask\x82\xd3\xe4\x93\x02\\2I/v1beta1/{endpoint_policy.name=projects/*/locations/*/endpointPolicies/*}:\x0fendpoint_policy'
    _globals['_NETWORKSERVICES'].methods_by_name['DeleteEndpointPolicy']._loaded_options = None
    _globals['_NETWORKSERVICES'].methods_by_name['DeleteEndpointPolicy']._serialized_options = b'\xcaAO\n\x15google.protobuf.Empty\x126google.cloud.networkservices.v1beta1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1beta1/{name=projects/*/locations/*/endpointPolicies/*}'
    _globals['_NETWORKSERVICES']._serialized_start = 254
    _globals['_NETWORKSERVICES']._serialized_end = 1741