"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/custom_targeting_value_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import custom_targeting_value_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_custom__targeting__value__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/admanager/v1/custom_targeting_value_service.proto\x12\x17google.ads.admanager.v1\x1a=google/ads/admanager/v1/custom_targeting_value_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"e\n\x1eGetCustomTargetingValueRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-admanager.googleapis.com/CustomTargetingValue"\xd7\x01\n ListCustomTargetingValuesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+admanager.googleapis.com/CustomTargetingKey\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\xa0\x01\n!ListCustomTargetingValuesResponse\x12N\n\x17custom_targeting_values\x18\x01 \x03(\x0b2-.google.ads.admanager.v1.CustomTargetingValue\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xfd\x03\n\x1bCustomTargetingValueService\x12\xd5\x01\n\x17GetCustomTargetingValue\x127.google.ads.admanager.v1.GetCustomTargetingValueRequest\x1a-.google.ads.admanager.v1.CustomTargetingValue"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v1/{name=networks/*/customTargetingKeys/*/customTargetingValues/*}\x12\xe8\x01\n\x19ListCustomTargetingValues\x129.google.ads.admanager.v1.ListCustomTargetingValuesRequest\x1a:.google.ads.admanager.v1.ListCustomTargetingValuesResponse"T\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/v1/{parent=networks/*/customTargetingKeys/*}/customTargetingValues\x1a\x1b\xcaA\x18admanager.googleapis.comB\xd4\x01\n\x1bcom.google.ads.admanager.v1B CustomTargetingValueServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.custom_targeting_value_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B CustomTargetingValueServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETCUSTOMTARGETINGVALUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMTARGETINGVALUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-admanager.googleapis.com/CustomTargetingValue'
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+admanager.googleapis.com/CustomTargetingKey'
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMTARGETINGVALUESERVICE']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUESERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com'
    _globals['_CUSTOMTARGETINGVALUESERVICE'].methods_by_name['GetCustomTargetingValue']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUESERVICE'].methods_by_name['GetCustomTargetingValue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v1/{name=networks/*/customTargetingKeys/*/customTargetingValues/*}'
    _globals['_CUSTOMTARGETINGVALUESERVICE'].methods_by_name['ListCustomTargetingValues']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUESERVICE'].methods_by_name['ListCustomTargetingValues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/v1/{parent=networks/*/customTargetingKeys/*}/customTargetingValues'
    _globals['_GETCUSTOMTARGETINGVALUEREQUEST']._serialized_start = 267
    _globals['_GETCUSTOMTARGETINGVALUEREQUEST']._serialized_end = 368
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST']._serialized_start = 371
    _globals['_LISTCUSTOMTARGETINGVALUESREQUEST']._serialized_end = 586
    _globals['_LISTCUSTOMTARGETINGVALUESRESPONSE']._serialized_start = 589
    _globals['_LISTCUSTOMTARGETINGVALUESRESPONSE']._serialized_end = 749
    _globals['_CUSTOMTARGETINGVALUESERVICE']._serialized_start = 752
    _globals['_CUSTOMTARGETINGVALUESERVICE']._serialized_end = 1261