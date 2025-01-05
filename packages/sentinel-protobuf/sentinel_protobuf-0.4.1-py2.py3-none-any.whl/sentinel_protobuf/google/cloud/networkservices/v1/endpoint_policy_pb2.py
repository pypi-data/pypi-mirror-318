"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networkservices/v1/endpoint_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkservices.v1 import common_pb2 as google_dot_cloud_dot_networkservices_dot_v1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/networkservices/v1/endpoint_policy.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/networkservices/v1/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8c\x08\n\x0eEndpointPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x06labels\x18\x04 \x03(\x0b2;.google.cloud.networkservices.v1.EndpointPolicy.LabelsEntryB\x03\xe0A\x01\x12U\n\x04type\x18\x05 \x01(\x0e2B.google.cloud.networkservices.v1.EndpointPolicy.EndpointPolicyTypeB\x03\xe0A\x02\x12X\n\x14authorization_policy\x18\x07 \x01(\tB:\xe0A\x01\xfaA4\n2networksecurity.googleapis.com/AuthorizationPolicy\x12O\n\x10endpoint_matcher\x18\t \x01(\x0b20.google.cloud.networkservices.v1.EndpointMatcherB\x03\xe0A\x02\x12X\n\x15traffic_port_selector\x18\n \x01(\x0b24.google.cloud.networkservices.v1.TrafficPortSelectorB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x0b \x01(\tB\x03\xe0A\x01\x12Q\n\x11server_tls_policy\x18\x0c \x01(\tB6\xe0A\x01\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Q\n\x11client_tls_policy\x18\r \x01(\tB6\xe0A\x01\xfaA0\n.networksecurity.googleapis.com/ClientTlsPolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x12EndpointPolicyType\x12$\n ENDPOINT_POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rSIDECAR_PROXY\x10\x01\x12\x0f\n\x0bGRPC_SERVER\x10\x02:~\xeaA{\n-networkservices.googleapis.com/EndpointPolicy\x12Jprojects/{project}/locations/{location}/endpointPolicies/{endpoint_policy}"\x8b\x01\n\x1bListEndpointPoliciesRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/EndpointPolicy\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x83\x01\n\x1cListEndpointPoliciesResponse\x12J\n\x11endpoint_policies\x18\x01 \x03(\x0b2/.google.cloud.networkservices.v1.EndpointPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"_\n\x18GetEndpointPolicyRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-networkservices.googleapis.com/EndpointPolicy"\xd4\x01\n\x1bCreateEndpointPolicyRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/EndpointPolicy\x12\x1f\n\x12endpoint_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12M\n\x0fendpoint_policy\x18\x03 \x01(\x0b2/.google.cloud.networkservices.v1.EndpointPolicyB\x03\xe0A\x02"\xa2\x01\n\x1bUpdateEndpointPolicyRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12M\n\x0fendpoint_policy\x18\x02 \x01(\x0b2/.google.cloud.networkservices.v1.EndpointPolicyB\x03\xe0A\x02"b\n\x1bDeleteEndpointPolicyRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-networkservices.googleapis.com/EndpointPolicyB\x86\x05\n#com.google.cloud.networkservices.v1B\x13EndpointPolicyProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaA\x8a\x01\n2networksecurity.googleapis.com/AuthorizationPolicy\x12Tprojects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}\xeaA\x7f\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}\xeaA\x7f\n.networksecurity.googleapis.com/ClientTlsPolicy\x12Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.endpoint_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x13EndpointPolicyProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaA\x8a\x01\n2networksecurity.googleapis.com/AuthorizationPolicy\x12Tprojects/{project}/locations/{location}/authorizationPolicies/{authorization_policy}\xeaA\x7f\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}\xeaA\x7f\n.networksecurity.googleapis.com/ClientTlsPolicy\x12Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}'
    _globals['_ENDPOINTPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_ENDPOINTPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ENDPOINTPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINTPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINTPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINTPOLICY'].fields_by_name['labels']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINTPOLICY'].fields_by_name['type']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINTPOLICY'].fields_by_name['authorization_policy']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['authorization_policy']._serialized_options = b'\xe0A\x01\xfaA4\n2networksecurity.googleapis.com/AuthorizationPolicy'
    _globals['_ENDPOINTPOLICY'].fields_by_name['endpoint_matcher']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['endpoint_matcher']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINTPOLICY'].fields_by_name['traffic_port_selector']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['traffic_port_selector']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINTPOLICY'].fields_by_name['description']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINTPOLICY'].fields_by_name['server_tls_policy']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['server_tls_policy']._serialized_options = b'\xe0A\x01\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy'
    _globals['_ENDPOINTPOLICY'].fields_by_name['client_tls_policy']._loaded_options = None
    _globals['_ENDPOINTPOLICY'].fields_by_name['client_tls_policy']._serialized_options = b'\xe0A\x01\xfaA0\n.networksecurity.googleapis.com/ClientTlsPolicy'
    _globals['_ENDPOINTPOLICY']._loaded_options = None
    _globals['_ENDPOINTPOLICY']._serialized_options = b'\xeaA{\n-networkservices.googleapis.com/EndpointPolicy\x12Jprojects/{project}/locations/{location}/endpointPolicies/{endpoint_policy}'
    _globals['_LISTENDPOINTPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENDPOINTPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/EndpointPolicy'
    _globals['_GETENDPOINTPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENDPOINTPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-networkservices.googleapis.com/EndpointPolicy'
    _globals['_CREATEENDPOINTPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENDPOINTPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/EndpointPolicy'
    _globals['_CREATEENDPOINTPOLICYREQUEST'].fields_by_name['endpoint_policy_id']._loaded_options = None
    _globals['_CREATEENDPOINTPOLICYREQUEST'].fields_by_name['endpoint_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENDPOINTPOLICYREQUEST'].fields_by_name['endpoint_policy']._loaded_options = None
    _globals['_CREATEENDPOINTPOLICYREQUEST'].fields_by_name['endpoint_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENDPOINTPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENDPOINTPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENDPOINTPOLICYREQUEST'].fields_by_name['endpoint_policy']._loaded_options = None
    _globals['_UPDATEENDPOINTPOLICYREQUEST'].fields_by_name['endpoint_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENDPOINTPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENDPOINTPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-networkservices.googleapis.com/EndpointPolicy'
    _globals['_ENDPOINTPOLICY']._serialized_start = 264
    _globals['_ENDPOINTPOLICY']._serialized_end = 1300
    _globals['_ENDPOINTPOLICY_LABELSENTRY']._serialized_start = 1031
    _globals['_ENDPOINTPOLICY_LABELSENTRY']._serialized_end = 1076
    _globals['_ENDPOINTPOLICY_ENDPOINTPOLICYTYPE']._serialized_start = 1078
    _globals['_ENDPOINTPOLICY_ENDPOINTPOLICYTYPE']._serialized_end = 1172
    _globals['_LISTENDPOINTPOLICIESREQUEST']._serialized_start = 1303
    _globals['_LISTENDPOINTPOLICIESREQUEST']._serialized_end = 1442
    _globals['_LISTENDPOINTPOLICIESRESPONSE']._serialized_start = 1445
    _globals['_LISTENDPOINTPOLICIESRESPONSE']._serialized_end = 1576
    _globals['_GETENDPOINTPOLICYREQUEST']._serialized_start = 1578
    _globals['_GETENDPOINTPOLICYREQUEST']._serialized_end = 1673
    _globals['_CREATEENDPOINTPOLICYREQUEST']._serialized_start = 1676
    _globals['_CREATEENDPOINTPOLICYREQUEST']._serialized_end = 1888
    _globals['_UPDATEENDPOINTPOLICYREQUEST']._serialized_start = 1891
    _globals['_UPDATEENDPOINTPOLICYREQUEST']._serialized_end = 2053
    _globals['_DELETEENDPOINTPOLICYREQUEST']._serialized_start = 2055
    _globals['_DELETEENDPOINTPOLICYREQUEST']._serialized_end = 2153