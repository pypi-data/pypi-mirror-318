"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/taxonomy_category_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import taxonomy_type_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_taxonomy__type__enum__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/admanager/v1/taxonomy_category_messages.proto\x12\x17google.ads.admanager.v1\x1a0google/ads/admanager/v1/taxonomy_type_enum.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdf\x03\n\x10TaxonomyCategory\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12!\n\x14taxonomy_category_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rgrouping_only\x18\x05 \x01(\x08B\x03\xe0A\x03\x12(\n\x1bparent_taxonomy_category_id\x18\x06 \x01(\x03B\x03\xe0A\x03\x12R\n\rtaxonomy_type\x18\t \x01(\x0e26.google.ads.admanager.v1.TaxonomyTypeEnum.TaxonomyTypeB\x03\xe0A\x03\x12\x1b\n\x0eancestor_names\x18\x07 \x03(\tB\x03\xe0A\x03\x12+\n\x1eancestor_taxonomy_category_ids\x18\x08 \x03(\x03B\x03\xe0A\x03:\x95\x01\xeaA\x91\x01\n)admanager.googleapis.com/TaxonomyCategory\x12>networks/{network_code}/taxonomyCategories/{taxonomy_category}*\x12taxonomyCategories2\x10taxonomyCategoryB\xd1\x01\n\x1bcom.google.ads.admanager.v1B\x1dTaxonomyCategoryMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.taxonomy_category_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1dTaxonomyCategoryMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['name']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['taxonomy_category_id']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['taxonomy_category_id']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['display_name']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['grouping_only']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['grouping_only']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['parent_taxonomy_category_id']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['parent_taxonomy_category_id']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['taxonomy_type']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['taxonomy_type']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['ancestor_names']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['ancestor_names']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY'].fields_by_name['ancestor_taxonomy_category_ids']._loaded_options = None
    _globals['_TAXONOMYCATEGORY'].fields_by_name['ancestor_taxonomy_category_ids']._serialized_options = b'\xe0A\x03'
    _globals['_TAXONOMYCATEGORY']._loaded_options = None
    _globals['_TAXONOMYCATEGORY']._serialized_options = b'\xeaA\x91\x01\n)admanager.googleapis.com/TaxonomyCategory\x12>networks/{network_code}/taxonomyCategories/{taxonomy_category}*\x12taxonomyCategories2\x10taxonomyCategory'
    _globals['_TAXONOMYCATEGORY']._serialized_start = 196
    _globals['_TAXONOMYCATEGORY']._serialized_end = 675