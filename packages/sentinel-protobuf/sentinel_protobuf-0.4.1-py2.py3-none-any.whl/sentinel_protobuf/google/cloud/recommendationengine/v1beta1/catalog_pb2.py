"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/catalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.recommendationengine.v1beta1 import common_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/recommendationengine/v1beta1/catalog.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a6google/cloud/recommendationengine/v1beta1/common.proto"\xfe\x03\n\x0bCatalogItem\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x12k\n\x14category_hierarchies\x18\x02 \x03(\x0b2H.google.cloud.recommendationengine.v1beta1.CatalogItem.CategoryHierarchyB\x03\xe0A\x02\x12\x12\n\x05title\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12S\n\x0fitem_attributes\x18\x05 \x01(\x0b25.google.cloud.recommendationengine.v1beta1.FeatureMapB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04tags\x18\x08 \x03(\tB\x03\xe0A\x01\x12\x1a\n\ritem_group_id\x18\t \x01(\tB\x03\xe0A\x01\x12^\n\x10product_metadata\x18\n \x01(\x0b2=.google.cloud.recommendationengine.v1beta1.ProductCatalogItemB\x03\xe0A\x01H\x00\x1a,\n\x11CategoryHierarchy\x12\x17\n\ncategories\x18\x01 \x03(\tB\x03\xe0A\x02B\x15\n\x13recommendation_type"\xe6\x06\n\x12ProductCatalogItem\x12d\n\x0bexact_price\x18\x01 \x01(\x0b2H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.ExactPriceB\x03\xe0A\x01H\x00\x12d\n\x0bprice_range\x18\x02 \x01(\x0b2H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.PriceRangeB\x03\xe0A\x01H\x00\x12\\\n\x05costs\x18\x03 \x03(\x0b2H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.CostsEntryB\x03\xe0A\x01\x12\x1a\n\rcurrency_code\x18\x04 \x01(\tB\x03\xe0A\x01\x12b\n\x0bstock_state\x18\x05 \x01(\x0e2H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.StockStateB\x03\xe0A\x01\x12\x1f\n\x12available_quantity\x18\x06 \x01(\x03B\x03\xe0A\x01\x12"\n\x15canonical_product_uri\x18\x07 \x01(\tB\x03\xe0A\x01\x12E\n\x06images\x18\x08 \x03(\x0b20.google.cloud.recommendationengine.v1beta1.ImageB\x03\xe0A\x01\x1aE\n\nExactPrice\x12\x1a\n\rdisplay_price\x18\x01 \x01(\x02B\x03\xe0A\x01\x12\x1b\n\x0eoriginal_price\x18\x02 \x01(\x02B\x03\xe0A\x01\x1a0\n\nPriceRange\x12\x10\n\x03min\x18\x01 \x01(\x02B\x03\xe0A\x02\x12\x10\n\x03max\x18\x02 \x01(\x02B\x03\xe0A\x02\x1a,\n\nCostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x028\x01"j\n\nStockState\x12\x1b\n\x17STOCK_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_STOCK\x10\x00\x12\x10\n\x0cOUT_OF_STOCK\x10\x01\x12\x0c\n\x08PREORDER\x10\x02\x12\r\n\tBACKORDER\x10\x03\x1a\x02\x10\x01B\x07\n\x05price"B\n\x05Image\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06height\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x12\n\x05width\x18\x03 \x01(\x05B\x03\xe0A\x01B\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.catalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_CATALOGITEM_CATEGORYHIERARCHY'].fields_by_name['categories']._loaded_options = None
    _globals['_CATALOGITEM_CATEGORYHIERARCHY'].fields_by_name['categories']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGITEM'].fields_by_name['id']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGITEM'].fields_by_name['category_hierarchies']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['category_hierarchies']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGITEM'].fields_by_name['title']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGITEM'].fields_by_name['description']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CATALOGITEM'].fields_by_name['item_attributes']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['item_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_CATALOGITEM'].fields_by_name['language_code']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_CATALOGITEM'].fields_by_name['tags']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_CATALOGITEM'].fields_by_name['item_group_id']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['item_group_id']._serialized_options = b'\xe0A\x01'
    _globals['_CATALOGITEM'].fields_by_name['product_metadata']._loaded_options = None
    _globals['_CATALOGITEM'].fields_by_name['product_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM_EXACTPRICE'].fields_by_name['display_price']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM_EXACTPRICE'].fields_by_name['display_price']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM_EXACTPRICE'].fields_by_name['original_price']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM_EXACTPRICE'].fields_by_name['original_price']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM_PRICERANGE'].fields_by_name['min']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM_PRICERANGE'].fields_by_name['min']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTCATALOGITEM_PRICERANGE'].fields_by_name['max']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM_PRICERANGE'].fields_by_name['max']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTCATALOGITEM_COSTSENTRY']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM_COSTSENTRY']._serialized_options = b'8\x01'
    _globals['_PRODUCTCATALOGITEM_STOCKSTATE']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM_STOCKSTATE']._serialized_options = b'\x10\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['exact_price']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['exact_price']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['price_range']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['price_range']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['costs']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['costs']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['currency_code']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['stock_state']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['stock_state']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['available_quantity']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['available_quantity']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['canonical_product_uri']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['canonical_product_uri']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['images']._loaded_options = None
    _globals['_PRODUCTCATALOGITEM'].fields_by_name['images']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGE'].fields_by_name['uri']._loaded_options = None
    _globals['_IMAGE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_IMAGE'].fields_by_name['height']._loaded_options = None
    _globals['_IMAGE'].fields_by_name['height']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGE'].fields_by_name['width']._loaded_options = None
    _globals['_IMAGE'].fields_by_name['width']._serialized_options = b'\xe0A\x01'
    _globals['_CATALOGITEM']._serialized_start = 192
    _globals['_CATALOGITEM']._serialized_end = 702
    _globals['_CATALOGITEM_CATEGORYHIERARCHY']._serialized_start = 635
    _globals['_CATALOGITEM_CATEGORYHIERARCHY']._serialized_end = 679
    _globals['_PRODUCTCATALOGITEM']._serialized_start = 705
    _globals['_PRODUCTCATALOGITEM']._serialized_end = 1575
    _globals['_PRODUCTCATALOGITEM_EXACTPRICE']._serialized_start = 1293
    _globals['_PRODUCTCATALOGITEM_EXACTPRICE']._serialized_end = 1362
    _globals['_PRODUCTCATALOGITEM_PRICERANGE']._serialized_start = 1364
    _globals['_PRODUCTCATALOGITEM_PRICERANGE']._serialized_end = 1412
    _globals['_PRODUCTCATALOGITEM_COSTSENTRY']._serialized_start = 1414
    _globals['_PRODUCTCATALOGITEM_COSTSENTRY']._serialized_end = 1458
    _globals['_PRODUCTCATALOGITEM_STOCKSTATE']._serialized_start = 1460
    _globals['_PRODUCTCATALOGITEM_STOCKSTATE']._serialized_end = 1566
    _globals['_IMAGE']._serialized_start = 1577
    _globals['_IMAGE']._serialized_end = 1643