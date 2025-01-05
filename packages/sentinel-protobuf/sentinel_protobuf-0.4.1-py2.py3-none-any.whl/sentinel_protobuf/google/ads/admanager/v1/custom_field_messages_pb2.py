"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/custom_field_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import custom_field_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_custom__field__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/admanager/v1/custom_field_messages.proto\x12\x17google.ads.admanager.v1\x1a0google/ads/admanager/v1/custom_field_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xac\x05\n\x0bCustomField\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1c\n\x0fcustom_field_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12U\n\x06status\x18\x05 \x01(\x0e2@.google.ads.admanager.v1.CustomFieldStatusEnum.CustomFieldStatusB\x03\xe0A\x03\x12b\n\x0bentity_type\x18\x07 \x01(\x0e2H.google.ads.admanager.v1.CustomFieldEntityTypeEnum.CustomFieldEntityTypeB\x03\xe0A\x02\x12\\\n\tdata_type\x18\x08 \x01(\x0e2D.google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataTypeB\x03\xe0A\x02\x12a\n\nvisibility\x18\t \x01(\x0e2H.google.ads.admanager.v1.CustomFieldVisibilityEnum.CustomFieldVisibilityB\x03\xe0A\x02\x12@\n\x07options\x18\n \x03(\x0b2*.google.ads.admanager.v1.CustomFieldOptionB\x03\xe0A\x01:y\xeaAv\n$admanager.googleapis.com/CustomField\x123networks/{network_code}/customFields/{custom_field}*\x0ccustomFields2\x0bcustomField"S\n\x11CustomFieldOption\x12#\n\x16custom_field_option_id\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02B\xcc\x01\n\x1bcom.google.ads.admanager.v1B\x18CustomFieldMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.custom_field_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x18CustomFieldMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_CUSTOMFIELD'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CUSTOMFIELD'].fields_by_name['custom_field_id']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['custom_field_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMFIELD'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMFIELD'].fields_by_name['description']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMFIELD'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMFIELD'].fields_by_name['entity_type']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMFIELD'].fields_by_name['data_type']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['data_type']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMFIELD'].fields_by_name['visibility']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['visibility']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMFIELD'].fields_by_name['options']._loaded_options = None
    _globals['_CUSTOMFIELD'].fields_by_name['options']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMFIELD']._loaded_options = None
    _globals['_CUSTOMFIELD']._serialized_options = b'\xeaAv\n$admanager.googleapis.com/CustomField\x123networks/{network_code}/customFields/{custom_field}*\x0ccustomFields2\x0bcustomField'
    _globals['_CUSTOMFIELDOPTION'].fields_by_name['custom_field_option_id']._loaded_options = None
    _globals['_CUSTOMFIELDOPTION'].fields_by_name['custom_field_option_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMFIELDOPTION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMFIELDOPTION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMFIELD']._serialized_start = 191
    _globals['_CUSTOMFIELD']._serialized_end = 875
    _globals['_CUSTOMFIELDOPTION']._serialized_start = 877
    _globals['_CUSTOMFIELDOPTION']._serialized_end = 960