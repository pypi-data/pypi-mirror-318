"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/custom_column.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import custom_column_render_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_custom__column__render__type__pb2
from ......google.ads.searchads360.v0.enums import custom_column_value_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_custom__column__value__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/searchads360/v0/resources/custom_column.proto\x12$google.ads.searchads360.v0.resources\x1a@google/ads/searchads360/v0/enums/custom_column_render_type.proto\x1a?google/ads/searchads360/v0/enums/custom_column_value_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xde\x04\n\x0cCustomColumn\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x05\xfaA*\n(searchads360.googleapis.com/CustomColumn\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x03\x12j\n\nvalue_type\x18\x05 \x01(\x0e2Q.google.ads.searchads360.v0.enums.CustomColumnValueTypeEnum.CustomColumnValueTypeB\x03\xe0A\x03\x12"\n\x15references_attributes\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x1f\n\x12references_metrics\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x16\n\tqueryable\x18\x08 \x01(\x08B\x03\xe0A\x03\x12&\n\x19referenced_system_columns\x18\t \x03(\tB\x03\xe0A\x03\x12m\n\x0brender_type\x18\n \x01(\x0e2S.google.ads.searchads360.v0.enums.CustomColumnRenderTypeEnum.CustomColumnRenderTypeB\x03\xe0A\x03:g\xeaAd\n(searchads360.googleapis.com/CustomColumn\x128customers/{customer_id}/customColumns/{custom_column_id}B\x91\x02\n(com.google.ads.searchads360.v0.resourcesB\x11CustomColumnProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.custom_column_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x11CustomColumnProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CUSTOMCOLUMN'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA*\n(searchads360.googleapis.com/CustomColumn'
    _globals['_CUSTOMCOLUMN'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['description']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['value_type']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['value_type']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['references_attributes']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['references_attributes']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['references_metrics']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['references_metrics']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['queryable']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['queryable']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['referenced_system_columns']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['referenced_system_columns']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN'].fields_by_name['render_type']._loaded_options = None
    _globals['_CUSTOMCOLUMN'].fields_by_name['render_type']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCOLUMN']._loaded_options = None
    _globals['_CUSTOMCOLUMN']._serialized_options = b'\xeaAd\n(searchads360.googleapis.com/CustomColumn\x128customers/{customer_id}/customColumns/{custom_column_id}'
    _globals['_CUSTOMCOLUMN']._serialized_start = 290
    _globals['_CUSTOMCOLUMN']._serialized_end = 896