"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/billing/v1/cloud_catalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/billing/v1/cloud_catalog.proto\x12\x17google.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\x9d\x01\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nservice_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x1c\n\x14business_entity_name\x18\x04 \x01(\t:<\xeaA9\n#cloudbilling.googleapis.com/Service\x12\x12services/{service}"\xe2\x02\n\x03Sku\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06sku_id\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x123\n\x08category\x18\x04 \x01(\x0b2!.google.cloud.billing.v1.Category\x12\x17\n\x0fservice_regions\x18\x05 \x03(\t\x12:\n\x0cpricing_info\x18\x06 \x03(\x0b2$.google.cloud.billing.v1.PricingInfo\x12\x1d\n\x15service_provider_name\x18\x07 \x01(\t\x12:\n\x0cgeo_taxonomy\x18\x08 \x01(\x0b2$.google.cloud.billing.v1.GeoTaxonomy:C\xeaA@\n\x1fcloudbilling.googleapis.com/Sku\x12\x1dservices/{service}/skus/{sku}"m\n\x08Category\x12\x1c\n\x14service_display_name\x18\x01 \x01(\t\x12\x17\n\x0fresource_family\x18\x02 \x01(\t\x12\x16\n\x0eresource_group\x18\x03 \x01(\t\x12\x12\n\nusage_type\x18\x04 \x01(\t"\x80\x02\n\x0bPricingInfo\x122\n\x0eeffective_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12F\n\x12pricing_expression\x18\x03 \x01(\x0b2*.google.cloud.billing.v1.PricingExpression\x12B\n\x10aggregation_info\x18\x04 \x01(\x0b2(.google.cloud.billing.v1.AggregationInfo\x12 \n\x18currency_conversion_rate\x18\x05 \x01(\x01"\xd3\x02\n\x11PricingExpression\x12\x12\n\nusage_unit\x18\x01 \x01(\t\x12\x18\n\x10display_quantity\x18\x02 \x01(\x01\x12I\n\x0ctiered_rates\x18\x03 \x03(\x0b23.google.cloud.billing.v1.PricingExpression.TierRate\x12\x1e\n\x16usage_unit_description\x18\x04 \x01(\t\x12\x11\n\tbase_unit\x18\x05 \x01(\t\x12\x1d\n\x15base_unit_description\x18\x06 \x01(\t\x12#\n\x1bbase_unit_conversion_factor\x18\x07 \x01(\x01\x1aN\n\x08TierRate\x12\x1a\n\x12start_usage_amount\x18\x01 \x01(\x01\x12&\n\nunit_price\x18\x02 \x01(\x0b2\x12.google.type.Money"\x84\x03\n\x0fAggregationInfo\x12T\n\x11aggregation_level\x18\x01 \x01(\x0e29.google.cloud.billing.v1.AggregationInfo.AggregationLevel\x12Z\n\x14aggregation_interval\x18\x02 \x01(\x0e2<.google.cloud.billing.v1.AggregationInfo.AggregationInterval\x12\x19\n\x11aggregation_count\x18\x03 \x01(\x05"O\n\x10AggregationLevel\x12!\n\x1dAGGREGATION_LEVEL_UNSPECIFIED\x10\x00\x12\x0b\n\x07ACCOUNT\x10\x01\x12\x0b\n\x07PROJECT\x10\x02"S\n\x13AggregationInterval\x12$\n AGGREGATION_INTERVAL_UNSPECIFIED\x10\x00\x12\t\n\x05DAILY\x10\x01\x12\x0b\n\x07MONTHLY\x10\x02"\xa3\x01\n\x0bGeoTaxonomy\x127\n\x04type\x18\x01 \x01(\x0e2).google.cloud.billing.v1.GeoTaxonomy.Type\x12\x0f\n\x07regions\x18\x02 \x03(\t"J\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06GLOBAL\x10\x01\x12\x0c\n\x08REGIONAL\x10\x02\x12\x12\n\x0eMULTI_REGIONAL\x10\x03"<\n\x13ListServicesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"c\n\x14ListServicesResponse\x122\n\x08services\x18\x01 \x03(\x0b2 .google.cloud.billing.v1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xea\x01\n\x0fListSkusRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#cloudbilling.googleapis.com/Service\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rcurrency_code\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"W\n\x10ListSkusResponse\x12*\n\x04skus\x18\x01 \x03(\x0b2\x1c.google.cloud.billing.v1.Sku\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xde\x03\n\x0cCloudCatalog\x12\x84\x01\n\x0cListServices\x12,.google.cloud.billing.v1.ListServicesRequest\x1a-.google.cloud.billing.v1.ListServicesResponse"\x17\xdaA\x00\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/services\x12\x8e\x01\n\x08ListSkus\x12(.google.cloud.billing.v1.ListSkusRequest\x1a).google.cloud.billing.v1.ListSkusResponse"-\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{parent=services/*}/skus\x1a\xb5\x01\xcaA\x1bcloudbilling.googleapis.com\xd2A\x93\x01https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-billing.readonly,https://www.googleapis.com/auth/cloud-platformB\x8d\x01\n\x1bcom.google.cloud.billing.v1B\x11CloudCatalogProtoP\x01Z5cloud.google.com/go/billing/apiv1/billingpb;billingpb\xa2\x02\x07CLDCTLG\xaa\x02\x17Google.Cloud.Billing.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.billing.v1.cloud_catalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.billing.v1B\x11CloudCatalogProtoP\x01Z5cloud.google.com/go/billing/apiv1/billingpb;billingpb\xa2\x02\x07CLDCTLG\xaa\x02\x17Google.Cloud.Billing.V1'
    _globals['_SERVICE']._loaded_options = None
    _globals['_SERVICE']._serialized_options = b'\xeaA9\n#cloudbilling.googleapis.com/Service\x12\x12services/{service}'
    _globals['_SKU']._loaded_options = None
    _globals['_SKU']._serialized_options = b'\xeaA@\n\x1fcloudbilling.googleapis.com/Sku\x12\x1dservices/{service}/skus/{sku}'
    _globals['_LISTSKUSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSKUSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#cloudbilling.googleapis.com/Service'
    _globals['_CLOUDCATALOG']._loaded_options = None
    _globals['_CLOUDCATALOG']._serialized_options = b'\xcaA\x1bcloudbilling.googleapis.com\xd2A\x93\x01https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-billing.readonly,https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDCATALOG'].methods_by_name['ListServices']._loaded_options = None
    _globals['_CLOUDCATALOG'].methods_by_name['ListServices']._serialized_options = b'\xdaA\x00\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/services'
    _globals['_CLOUDCATALOG'].methods_by_name['ListSkus']._loaded_options = None
    _globals['_CLOUDCATALOG'].methods_by_name['ListSkus']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{parent=services/*}/skus'
    _globals['_SERVICE']._serialized_start = 246
    _globals['_SERVICE']._serialized_end = 403
    _globals['_SKU']._serialized_start = 406
    _globals['_SKU']._serialized_end = 760
    _globals['_CATEGORY']._serialized_start = 762
    _globals['_CATEGORY']._serialized_end = 871
    _globals['_PRICINGINFO']._serialized_start = 874
    _globals['_PRICINGINFO']._serialized_end = 1130
    _globals['_PRICINGEXPRESSION']._serialized_start = 1133
    _globals['_PRICINGEXPRESSION']._serialized_end = 1472
    _globals['_PRICINGEXPRESSION_TIERRATE']._serialized_start = 1394
    _globals['_PRICINGEXPRESSION_TIERRATE']._serialized_end = 1472
    _globals['_AGGREGATIONINFO']._serialized_start = 1475
    _globals['_AGGREGATIONINFO']._serialized_end = 1863
    _globals['_AGGREGATIONINFO_AGGREGATIONLEVEL']._serialized_start = 1699
    _globals['_AGGREGATIONINFO_AGGREGATIONLEVEL']._serialized_end = 1778
    _globals['_AGGREGATIONINFO_AGGREGATIONINTERVAL']._serialized_start = 1780
    _globals['_AGGREGATIONINFO_AGGREGATIONINTERVAL']._serialized_end = 1863
    _globals['_GEOTAXONOMY']._serialized_start = 1866
    _globals['_GEOTAXONOMY']._serialized_end = 2029
    _globals['_GEOTAXONOMY_TYPE']._serialized_start = 1955
    _globals['_GEOTAXONOMY_TYPE']._serialized_end = 2029
    _globals['_LISTSERVICESREQUEST']._serialized_start = 2031
    _globals['_LISTSERVICESREQUEST']._serialized_end = 2091
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 2093
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 2192
    _globals['_LISTSKUSREQUEST']._serialized_start = 2195
    _globals['_LISTSKUSREQUEST']._serialized_end = 2429
    _globals['_LISTSKUSRESPONSE']._serialized_start = 2431
    _globals['_LISTSKUSRESPONSE']._serialized_end = 2518
    _globals['_CLOUDCATALOG']._serialized_start = 2521
    _globals['_CLOUDCATALOG']._serialized_end = 2999