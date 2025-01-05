"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networksecurity/v1beta1/server_tls_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networksecurity.v1beta1 import tls_pb2 as google_dot_cloud_dot_networksecurity_dot_v1beta1_dot_tls__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/networksecurity/v1beta1/server_tls_policy.proto\x12$google.cloud.networksecurity.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/networksecurity/v1beta1/tls.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x05\n\x0fServerTlsPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Q\n\x06labels\x18\x05 \x03(\x0b2A.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.LabelsEntry\x12\x12\n\nallow_open\x18\x06 \x01(\x08\x12U\n\x12server_certificate\x18\x07 \x01(\x0b29.google.cloud.networksecurity.v1beta1.CertificateProvider\x12U\n\x0bmtls_policy\x18\x08 \x01(\x0b2@.google.cloud.networksecurity.v1beta1.ServerTlsPolicy.MTLSPolicy\x1a^\n\nMTLSPolicy\x12P\n\x14client_validation_ca\x18\x01 \x03(\x0b22.google.cloud.networksecurity.v1beta1.ValidationCA\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x82\x01\xeaA\x7f\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}"\x80\x01\n\x1cListServerTlsPoliciesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8c\x01\n\x1dListServerTlsPoliciesResponse\x12R\n\x13server_tls_policies\x18\x01 \x03(\x0b25.google.cloud.networksecurity.v1beta1.ServerTlsPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"a\n\x19GetServerTlsPolicyRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy"\xe0\x01\n\x1cCreateServerTlsPolicyRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.networksecurity.googleapis.com/ServerTlsPolicy\x12!\n\x14server_tls_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12U\n\x11server_tls_policy\x18\x03 \x01(\x0b25.google.cloud.networksecurity.v1beta1.ServerTlsPolicyB\x03\xe0A\x02"\xab\x01\n\x1cUpdateServerTlsPolicyRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12U\n\x11server_tls_policy\x18\x02 \x01(\x0b25.google.cloud.networksecurity.v1beta1.ServerTlsPolicyB\x03\xe0A\x02"d\n\x1cDeleteServerTlsPolicyRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicyB\x8e\x02\n(com.google.cloud.networksecurity.v1beta1B\x14ServerTlsPolicyProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02\'Google::Cloud::NetworkSecurity::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1beta1.server_tls_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.networksecurity.v1beta1B\x14ServerTlsPolicyProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02'Google::Cloud::NetworkSecurity::V1beta1"
    _globals['_SERVERTLSPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_SERVERTLSPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVERTLSPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_SERVERTLSPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SERVERTLSPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_SERVERTLSPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVERTLSPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_SERVERTLSPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVERTLSPOLICY']._loaded_options = None
    _globals['_SERVERTLSPOLICY']._serialized_options = b'\xeaA\x7f\n.networksecurity.googleapis.com/ServerTlsPolicy\x12Mprojects/{project}/locations/{location}/serverTlsPolicies/{server_tls_policy}'
    _globals['_LISTSERVERTLSPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVERTLSPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETSERVERTLSPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVERTLSPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy'
    _globals['_CREATESERVERTLSPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVERTLSPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.networksecurity.googleapis.com/ServerTlsPolicy'
    _globals['_CREATESERVERTLSPOLICYREQUEST'].fields_by_name['server_tls_policy_id']._loaded_options = None
    _globals['_CREATESERVERTLSPOLICYREQUEST'].fields_by_name['server_tls_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVERTLSPOLICYREQUEST'].fields_by_name['server_tls_policy']._loaded_options = None
    _globals['_CREATESERVERTLSPOLICYREQUEST'].fields_by_name['server_tls_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVERTLSPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESERVERTLSPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESERVERTLSPOLICYREQUEST'].fields_by_name['server_tls_policy']._loaded_options = None
    _globals['_UPDATESERVERTLSPOLICYREQUEST'].fields_by_name['server_tls_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVERTLSPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVERTLSPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy'
    _globals['_SERVERTLSPOLICY']._serialized_start = 278
    _globals['_SERVERTLSPOLICY']._serialized_end = 996
    _globals['_SERVERTLSPOLICY_MTLSPOLICY']._serialized_start = 722
    _globals['_SERVERTLSPOLICY_MTLSPOLICY']._serialized_end = 816
    _globals['_SERVERTLSPOLICY_LABELSENTRY']._serialized_start = 818
    _globals['_SERVERTLSPOLICY_LABELSENTRY']._serialized_end = 863
    _globals['_LISTSERVERTLSPOLICIESREQUEST']._serialized_start = 999
    _globals['_LISTSERVERTLSPOLICIESREQUEST']._serialized_end = 1127
    _globals['_LISTSERVERTLSPOLICIESRESPONSE']._serialized_start = 1130
    _globals['_LISTSERVERTLSPOLICIESRESPONSE']._serialized_end = 1270
    _globals['_GETSERVERTLSPOLICYREQUEST']._serialized_start = 1272
    _globals['_GETSERVERTLSPOLICYREQUEST']._serialized_end = 1369
    _globals['_CREATESERVERTLSPOLICYREQUEST']._serialized_start = 1372
    _globals['_CREATESERVERTLSPOLICYREQUEST']._serialized_end = 1596
    _globals['_UPDATESERVERTLSPOLICYREQUEST']._serialized_start = 1599
    _globals['_UPDATESERVERTLSPOLICYREQUEST']._serialized_end = 1770
    _globals['_DELETESERVERTLSPOLICYREQUEST']._serialized_start = 1772
    _globals['_DELETESERVERTLSPOLICYREQUEST']._serialized_end = 1872