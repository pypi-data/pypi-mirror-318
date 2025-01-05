"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/quota/v1beta/quota.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/shopping/merchant/quota/v1beta/quota.proto\x12%google.shopping.merchant.quota.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaf\x02\n\nQuotaGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bquota_usage\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bquota_limit\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12quota_minute_limit\x18\x05 \x01(\x03B\x03\xe0A\x03\x12Q\n\x0emethod_details\x18\x04 \x03(\x0b24.google.shopping.merchant.quota.v1beta.MethodDetailsB\x03\xe0A\x03:f\xeaAc\n%merchantapi.googleapis.com/QuotaGroup\x12!accounts/{account}/groups/{group}*\x0bquotaGroups2\nquotaGroup"b\n\rMethodDetails\x12\x13\n\x06method\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07version\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06subapi\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04path\x18\x04 \x01(\tB\x03\xe0A\x03"\x88\x01\n\x16ListQuotaGroupsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%merchantapi.googleapis.com/QuotaGroup\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"{\n\x17ListQuotaGroupsResponse\x12G\n\x0cquota_groups\x18\x01 \x03(\x0b21.google.shopping.merchant.quota.v1beta.QuotaGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa5\x02\n\x0cQuotaService\x12\xcb\x01\n\x0fListQuotaGroups\x12=.google.shopping.merchant.quota.v1beta.ListQuotaGroupsRequest\x1a>.google.shopping.merchant.quota.v1beta.ListQuotaGroupsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/quota/v1beta/{parent=accounts/*}/quotas\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xbb\x01\n)com.google.shopping.merchant.quota.v1betaB\nQuotaProtoP\x01ZEcloud.google.com/go/shopping/merchant/quota/apiv1beta/quotapb;quotapb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.quota.v1beta.quota_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.shopping.merchant.quota.v1betaB\nQuotaProtoP\x01ZEcloud.google.com/go/shopping/merchant/quota/apiv1beta/quotapb;quotapb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_QUOTAGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_QUOTAGROUP'].fields_by_name['quota_usage']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['quota_usage']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP'].fields_by_name['quota_limit']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['quota_limit']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP'].fields_by_name['quota_minute_limit']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['quota_minute_limit']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP'].fields_by_name['method_details']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['method_details']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP']._loaded_options = None
    _globals['_QUOTAGROUP']._serialized_options = b'\xeaAc\n%merchantapi.googleapis.com/QuotaGroup\x12!accounts/{account}/groups/{group}*\x0bquotaGroups2\nquotaGroup'
    _globals['_METHODDETAILS'].fields_by_name['method']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['method']._serialized_options = b'\xe0A\x03'
    _globals['_METHODDETAILS'].fields_by_name['version']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['version']._serialized_options = b'\xe0A\x03'
    _globals['_METHODDETAILS'].fields_by_name['subapi']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['subapi']._serialized_options = b'\xe0A\x03'
    _globals['_METHODDETAILS'].fields_by_name['path']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['path']._serialized_options = b'\xe0A\x03'
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%merchantapi.googleapis.com/QuotaGroup"
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTASERVICE']._loaded_options = None
    _globals['_QUOTASERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_QUOTASERVICE'].methods_by_name['ListQuotaGroups']._loaded_options = None
    _globals['_QUOTASERVICE'].methods_by_name['ListQuotaGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/quota/v1beta/{parent=accounts/*}/quotas'
    _globals['_QUOTAGROUP']._serialized_start = 208
    _globals['_QUOTAGROUP']._serialized_end = 511
    _globals['_METHODDETAILS']._serialized_start = 513
    _globals['_METHODDETAILS']._serialized_end = 611
    _globals['_LISTQUOTAGROUPSREQUEST']._serialized_start = 614
    _globals['_LISTQUOTAGROUPSREQUEST']._serialized_end = 750
    _globals['_LISTQUOTAGROUPSRESPONSE']._serialized_start = 752
    _globals['_LISTQUOTAGROUPSRESPONSE']._serialized_end = 875
    _globals['_QUOTASERVICE']._serialized_start = 878
    _globals['_QUOTASERVICE']._serialized_end = 1171