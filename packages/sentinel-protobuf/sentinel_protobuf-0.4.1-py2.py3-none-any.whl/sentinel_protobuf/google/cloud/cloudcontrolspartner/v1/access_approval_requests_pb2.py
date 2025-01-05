"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1/access_approval_requests.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/cloudcontrolspartner/v1/access_approval_requests.proto\x12$google.cloud.cloudcontrolspartner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe9\x03\n\x15AccessApprovalRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x120\n\x0crequest_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12L\n\x10requested_reason\x18\x03 \x01(\x0b22.google.cloud.cloudcontrolspartner.v1.AccessReason\x12=\n\x19requested_expiration_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp:\xfd\x01\xeaA\xf9\x01\n9cloudcontrolspartner.googleapis.com/AccessApprovalRequest\x12\x8c\x01organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/accessApprovalRequests/{access_approval_request}*\x16accessApprovalRequests2\x15accessApprovalRequest"\xd3\x01\n!ListAccessApprovalRequestsRequest\x12Q\n\x06parent\x18\x01 \x01(\tBA\xe0A\x02\xfaA;\x129cloudcontrolspartner.googleapis.com/AccessApprovalRequest\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xb1\x01\n"ListAccessApprovalRequestsResponse\x12]\n\x18access_approval_requests\x18\x01 \x03(\x0b2;.google.cloud.cloudcontrolspartner.v1.AccessApprovalRequest\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xc2\x02\n\x0cAccessReason\x12E\n\x04type\x18\x01 \x01(\x0e27.google.cloud.cloudcontrolspartner.v1.AccessReason.Type\x12\x0e\n\x06detail\x18\x02 \x01(\t"\xda\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aCUSTOMER_INITIATED_SUPPORT\x10\x01\x12\x1c\n\x18GOOGLE_INITIATED_SERVICE\x10\x02\x12\x1b\n\x17GOOGLE_INITIATED_REVIEW\x10\x03\x12\x1c\n\x18THIRD_PARTY_DATA_REQUEST\x10\x04\x12\'\n#GOOGLE_RESPONSE_TO_PRODUCTION_ALERT\x10\x05\x12\x1a\n\x16CLOUD_INITIATED_ACCESS\x10\x06B\x9f\x02\n(com.google.cloud.cloudcontrolspartner.v1B\x1bAccessApprovalRequestsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02\'Google::Cloud::CloudControlsPartner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1.access_approval_requests_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.cloudcontrolspartner.v1B\x1bAccessApprovalRequestsProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02'Google::Cloud::CloudControlsPartner::V1"
    _globals['_ACCESSAPPROVALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSAPPROVALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCESSAPPROVALREQUEST']._loaded_options = None
    _globals['_ACCESSAPPROVALREQUEST']._serialized_options = b'\xeaA\xf9\x01\n9cloudcontrolspartner.googleapis.com/AccessApprovalRequest\x12\x8c\x01organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/accessApprovalRequests/{access_approval_request}*\x16accessApprovalRequests2\x15accessApprovalRequest'
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA;\x129cloudcontrolspartner.googleapis.com/AccessApprovalRequest'
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_ACCESSAPPROVALREQUEST']._serialized_start = 203
    _globals['_ACCESSAPPROVALREQUEST']._serialized_end = 692
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST']._serialized_start = 695
    _globals['_LISTACCESSAPPROVALREQUESTSREQUEST']._serialized_end = 906
    _globals['_LISTACCESSAPPROVALREQUESTSRESPONSE']._serialized_start = 909
    _globals['_LISTACCESSAPPROVALREQUESTSRESPONSE']._serialized_end = 1086
    _globals['_ACCESSREASON']._serialized_start = 1089
    _globals['_ACCESSREASON']._serialized_end = 1411
    _globals['_ACCESSREASON_TYPE']._serialized_start = 1193
    _globals['_ACCESSREASON_TYPE']._serialized_end = 1411