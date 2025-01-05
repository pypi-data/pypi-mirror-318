"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/networksecurity/v1beta1/client_tls_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networksecurity.v1beta1 import tls_pb2 as google_dot_cloud_dot_networksecurity_dot_v1beta1_dot_tls__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/networksecurity/v1beta1/client_tls_policy.proto\x12$google.cloud.networksecurity.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/networksecurity/v1beta1/tls.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfb\x04\n\x0fClientTlsPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12V\n\x06labels\x18\x05 \x03(\x0b2A.google.cloud.networksecurity.v1beta1.ClientTlsPolicy.LabelsEntryB\x03\xe0A\x01\x12\x10\n\x03sni\x18\x06 \x01(\tB\x03\xe0A\x01\x12Z\n\x12client_certificate\x18\x07 \x01(\x0b29.google.cloud.networksecurity.v1beta1.CertificateProviderB\x03\xe0A\x01\x12U\n\x14server_validation_ca\x18\x08 \x03(\x0b22.google.cloud.networksecurity.v1beta1.ValidationCAB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x82\x01\xeaA\x7f\n.networksecurity.googleapis.com/ClientTlsPolicy\x12Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}"\x80\x01\n\x1cListClientTlsPoliciesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8c\x01\n\x1dListClientTlsPoliciesResponse\x12R\n\x13client_tls_policies\x18\x01 \x03(\x0b25.google.cloud.networksecurity.v1beta1.ClientTlsPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"a\n\x19GetClientTlsPolicyRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ClientTlsPolicy"\xe0\x01\n\x1cCreateClientTlsPolicyRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.networksecurity.googleapis.com/ClientTlsPolicy\x12!\n\x14client_tls_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12U\n\x11client_tls_policy\x18\x03 \x01(\x0b25.google.cloud.networksecurity.v1beta1.ClientTlsPolicyB\x03\xe0A\x02"\xab\x01\n\x1cUpdateClientTlsPolicyRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12U\n\x11client_tls_policy\x18\x02 \x01(\x0b25.google.cloud.networksecurity.v1beta1.ClientTlsPolicyB\x03\xe0A\x02"d\n\x1cDeleteClientTlsPolicyRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ClientTlsPolicyB\x8e\x02\n(com.google.cloud.networksecurity.v1beta1B\x14ClientTlsPolicyProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02\'Google::Cloud::NetworkSecurity::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1beta1.client_tls_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.networksecurity.v1beta1B\x14ClientTlsPolicyProtoP\x01ZRcloud.google.com/go/networksecurity/apiv1beta1/networksecuritypb;networksecuritypb\xaa\x02$Google.Cloud.NetworkSecurity.V1Beta1\xca\x02$Google\\Cloud\\NetworkSecurity\\V1beta1\xea\x02'Google::Cloud::NetworkSecurity::V1beta1"
    _globals['_CLIENTTLSPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_CLIENTTLSPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['description']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['labels']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['sni']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['sni']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['client_certificate']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['client_certificate']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTLSPOLICY'].fields_by_name['server_validation_ca']._loaded_options = None
    _globals['_CLIENTTLSPOLICY'].fields_by_name['server_validation_ca']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTLSPOLICY']._loaded_options = None
    _globals['_CLIENTTLSPOLICY']._serialized_options = b'\xeaA\x7f\n.networksecurity.googleapis.com/ClientTlsPolicy\x12Mprojects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}'
    _globals['_LISTCLIENTTLSPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLIENTTLSPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETCLIENTTLSPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLIENTTLSPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ClientTlsPolicy'
    _globals['_CREATECLIENTTLSPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLIENTTLSPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.networksecurity.googleapis.com/ClientTlsPolicy'
    _globals['_CREATECLIENTTLSPOLICYREQUEST'].fields_by_name['client_tls_policy_id']._loaded_options = None
    _globals['_CREATECLIENTTLSPOLICYREQUEST'].fields_by_name['client_tls_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLIENTTLSPOLICYREQUEST'].fields_by_name['client_tls_policy']._loaded_options = None
    _globals['_CREATECLIENTTLSPOLICYREQUEST'].fields_by_name['client_tls_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECLIENTTLSPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECLIENTTLSPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECLIENTTLSPOLICYREQUEST'].fields_by_name['client_tls_policy']._loaded_options = None
    _globals['_UPDATECLIENTTLSPOLICYREQUEST'].fields_by_name['client_tls_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECLIENTTLSPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLIENTTLSPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.networksecurity.googleapis.com/ClientTlsPolicy'
    _globals['_CLIENTTLSPOLICY']._serialized_start = 278
    _globals['_CLIENTTLSPOLICY']._serialized_end = 913
    _globals['_CLIENTTLSPOLICY_LABELSENTRY']._serialized_start = 735
    _globals['_CLIENTTLSPOLICY_LABELSENTRY']._serialized_end = 780
    _globals['_LISTCLIENTTLSPOLICIESREQUEST']._serialized_start = 916
    _globals['_LISTCLIENTTLSPOLICIESREQUEST']._serialized_end = 1044
    _globals['_LISTCLIENTTLSPOLICIESRESPONSE']._serialized_start = 1047
    _globals['_LISTCLIENTTLSPOLICIESRESPONSE']._serialized_end = 1187
    _globals['_GETCLIENTTLSPOLICYREQUEST']._serialized_start = 1189
    _globals['_GETCLIENTTLSPOLICYREQUEST']._serialized_end = 1286
    _globals['_CREATECLIENTTLSPOLICYREQUEST']._serialized_start = 1289
    _globals['_CREATECLIENTTLSPOLICYREQUEST']._serialized_end = 1513
    _globals['_UPDATECLIENTTLSPOLICYREQUEST']._serialized_start = 1516
    _globals['_UPDATECLIENTTLSPOLICYREQUEST']._serialized_end = 1687
    _globals['_DELETECLIENTTLSPOLICYREQUEST']._serialized_start = 1689
    _globals['_DELETECLIENTTLSPOLICYREQUEST']._serialized_end = 1789