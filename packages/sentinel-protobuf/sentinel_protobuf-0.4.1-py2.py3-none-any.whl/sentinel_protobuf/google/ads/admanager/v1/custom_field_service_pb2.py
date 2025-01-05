"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/custom_field_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import custom_field_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_custom__field__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/admanager/v1/custom_field_service.proto\x12\x17google.ads.admanager.v1\x1a3google/ads/admanager/v1/custom_field_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"S\n\x15GetCustomFieldRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$admanager.googleapis.com/CustomField"\xc3\x01\n\x17ListCustomFieldsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\x84\x01\n\x18ListCustomFieldsResponse\x12;\n\rcustom_fields\x18\x01 \x03(\x0b2$.google.ads.admanager.v1.CustomField\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\x80\x03\n\x12CustomFieldService\x12\x9b\x01\n\x0eGetCustomField\x12..google.ads.admanager.v1.GetCustomFieldRequest\x1a$.google.ads.admanager.v1.CustomField"3\xdaA\x04name\x82\xd3\xe4\x93\x02&\x12$/v1/{name=networks/*/customFields/*}\x12\xae\x01\n\x10ListCustomFields\x120.google.ads.admanager.v1.ListCustomFieldsRequest\x1a1.google.ads.admanager.v1.ListCustomFieldsResponse"5\xdaA\x06parent\x82\xd3\xe4\x93\x02&\x12$/v1/{parent=networks/*}/customFields\x1a\x1b\xcaA\x18admanager.googleapis.comB\xcb\x01\n\x1bcom.google.ads.admanager.v1B\x17CustomFieldServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.custom_field_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x17CustomFieldServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETCUSTOMFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$admanager.googleapis.com/CustomField'
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTCUSTOMFIELDSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMFIELDSERVICE']._loaded_options = None
    _globals['_CUSTOMFIELDSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com'
    _globals['_CUSTOMFIELDSERVICE'].methods_by_name['GetCustomField']._loaded_options = None
    _globals['_CUSTOMFIELDSERVICE'].methods_by_name['GetCustomField']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02&\x12$/v1/{name=networks/*/customFields/*}'
    _globals['_CUSTOMFIELDSERVICE'].methods_by_name['ListCustomFields']._loaded_options = None
    _globals['_CUSTOMFIELDSERVICE'].methods_by_name['ListCustomFields']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02&\x12$/v1/{parent=networks/*}/customFields'
    _globals['_GETCUSTOMFIELDREQUEST']._serialized_start = 247
    _globals['_GETCUSTOMFIELDREQUEST']._serialized_end = 330
    _globals['_LISTCUSTOMFIELDSREQUEST']._serialized_start = 333
    _globals['_LISTCUSTOMFIELDSREQUEST']._serialized_end = 528
    _globals['_LISTCUSTOMFIELDSRESPONSE']._serialized_start = 531
    _globals['_LISTCUSTOMFIELDSRESPONSE']._serialized_end = 663
    _globals['_CUSTOMFIELDSERVICE']._serialized_start = 666
    _globals['_CUSTOMFIELDSERVICE']._serialized_end = 1050