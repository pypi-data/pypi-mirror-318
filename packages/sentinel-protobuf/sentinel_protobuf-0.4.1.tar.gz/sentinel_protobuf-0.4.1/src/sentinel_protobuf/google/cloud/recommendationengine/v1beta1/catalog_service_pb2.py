"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/catalog_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.recommendationengine.v1beta1 import catalog_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_catalog__pb2
from .....google.cloud.recommendationengine.v1beta1 import import_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_import__pb2
from .....google.cloud.recommendationengine.v1beta1 import recommendationengine_resources_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_recommendationengine__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/recommendationengine/v1beta1/catalog_service.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/recommendationengine/v1beta1/catalog.proto\x1a6google/cloud/recommendationengine/v1beta1/import.proto\x1aNgoogle/cloud/recommendationengine/v1beta1/recommendationengine_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb2\x01\n\x18CreateCatalogItemRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+recommendationengine.googleapis.com/Catalog\x12Q\n\x0ccatalog_item\x18\x02 \x01(\x0b26.google.cloud.recommendationengine.v1beta1.CatalogItemB\x03\xe0A\x02"b\n\x15GetCatalogItemRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3recommendationengine.googleapis.com/CatalogItemPath"\xa4\x01\n\x17ListCatalogItemsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+recommendationengine.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x18ListCatalogItemsResponse\x12M\n\rcatalog_items\x18\x01 \x03(\x0b26.google.cloud.recommendationengine.v1beta1.CatalogItem\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe9\x01\n\x18UpdateCatalogItemRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3recommendationengine.googleapis.com/CatalogItemPath\x12Q\n\x0ccatalog_item\x18\x02 \x01(\x0b26.google.cloud.recommendationengine.v1beta1.CatalogItemB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"e\n\x18DeleteCatalogItemRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3recommendationengine.googleapis.com/CatalogItemPath2\x96\r\n\x0eCatalogService\x12\xfe\x01\n\x11CreateCatalogItem\x12C.google.cloud.recommendationengine.v1beta1.CreateCatalogItemRequest\x1a6.google.cloud.recommendationengine.v1beta1.CatalogItem"l\xdaA\x13parent,catalog_item\x82\xd3\xe4\x93\x02P"@/v1beta1/{parent=projects/*/locations/*/catalogs/*}/catalogItems:\x0ccatalog_item\x12\xdc\x01\n\x0eGetCatalogItem\x12@.google.cloud.recommendationengine.v1beta1.GetCatalogItemRequest\x1a6.google.cloud.recommendationengine.v1beta1.CatalogItem"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1beta1/{name=projects/*/locations/*/catalogs/*/catalogItems/**}\x12\xf5\x01\n\x10ListCatalogItems\x12B.google.cloud.recommendationengine.v1beta1.ListCatalogItemsRequest\x1aC.google.cloud.recommendationengine.v1beta1.ListCatalogItemsResponse"X\xdaA\rparent,filter\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*/catalogs/*}/catalogItems\x12\x89\x02\n\x11UpdateCatalogItem\x12C.google.cloud.recommendationengine.v1beta1.UpdateCatalogItemRequest\x1a6.google.cloud.recommendationengine.v1beta1.CatalogItem"w\xdaA\x1dname,catalog_item,update_mask\x82\xd3\xe4\x93\x02Q2A/v1beta1/{name=projects/*/locations/*/catalogs/*/catalogItems/**}:\x0ccatalog_item\x12\xc2\x01\n\x11DeleteCatalogItem\x12C.google.cloud.recommendationengine.v1beta1.DeleteCatalogItemRequest\x1a\x16.google.protobuf.Empty"P\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1beta1/{name=projects/*/locations/*/catalogs/*/catalogItems/**}\x12\x81\x03\n\x12ImportCatalogItems\x12D.google.cloud.recommendationengine.v1beta1.ImportCatalogItemsRequest\x1a\x1d.google.longrunning.Operation"\x85\x02\xcaA\x80\x01\nDgoogle.cloud.recommendationengine.v1beta1.ImportCatalogItemsResponse\x128google.cloud.recommendationengine.v1beta1.ImportMetadata\xdaA,parent,request_id,input_config,errors_config\x82\xd3\xe4\x93\x02L"G/v1beta1/{parent=projects/*/locations/*/catalogs/*}/catalogItems:import:\x01*\x1aW\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.catalog_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_CREATECATALOGITEMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECATALOGITEMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+recommendationengine.googleapis.com/Catalog'
    _globals['_CREATECATALOGITEMREQUEST'].fields_by_name['catalog_item']._loaded_options = None
    _globals['_CREATECATALOGITEMREQUEST'].fields_by_name['catalog_item']._serialized_options = b'\xe0A\x02'
    _globals['_GETCATALOGITEMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCATALOGITEMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3recommendationengine.googleapis.com/CatalogItemPath'
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+recommendationengine.googleapis.com/Catalog'
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCATALOGITEMSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECATALOGITEMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATECATALOGITEMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3recommendationengine.googleapis.com/CatalogItemPath'
    _globals['_UPDATECATALOGITEMREQUEST'].fields_by_name['catalog_item']._loaded_options = None
    _globals['_UPDATECATALOGITEMREQUEST'].fields_by_name['catalog_item']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECATALOGITEMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECATALOGITEMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3recommendationengine.googleapis.com/CatalogItemPath'
    _globals['_CATALOGSERVICE']._loaded_options = None
    _globals['_CATALOGSERVICE']._serialized_options = b'\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CATALOGSERVICE'].methods_by_name['CreateCatalogItem']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['CreateCatalogItem']._serialized_options = b'\xdaA\x13parent,catalog_item\x82\xd3\xe4\x93\x02P"@/v1beta1/{parent=projects/*/locations/*/catalogs/*}/catalogItems:\x0ccatalog_item'
    _globals['_CATALOGSERVICE'].methods_by_name['GetCatalogItem']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetCatalogItem']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1beta1/{name=projects/*/locations/*/catalogs/*/catalogItems/**}'
    _globals['_CATALOGSERVICE'].methods_by_name['ListCatalogItems']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['ListCatalogItems']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*/catalogs/*}/catalogItems'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCatalogItem']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCatalogItem']._serialized_options = b'\xdaA\x1dname,catalog_item,update_mask\x82\xd3\xe4\x93\x02Q2A/v1beta1/{name=projects/*/locations/*/catalogs/*/catalogItems/**}:\x0ccatalog_item'
    _globals['_CATALOGSERVICE'].methods_by_name['DeleteCatalogItem']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['DeleteCatalogItem']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1beta1/{name=projects/*/locations/*/catalogs/*/catalogItems/**}'
    _globals['_CATALOGSERVICE'].methods_by_name['ImportCatalogItems']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['ImportCatalogItems']._serialized_options = b'\xcaA\x80\x01\nDgoogle.cloud.recommendationengine.v1beta1.ImportCatalogItemsResponse\x128google.cloud.recommendationengine.v1beta1.ImportMetadata\xdaA,parent,request_id,input_config,errors_config\x82\xd3\xe4\x93\x02L"G/v1beta1/{parent=projects/*/locations/*/catalogs/*}/catalogItems:import:\x01*'
    _globals['_CREATECATALOGITEMREQUEST']._serialized_start = 519
    _globals['_CREATECATALOGITEMREQUEST']._serialized_end = 697
    _globals['_GETCATALOGITEMREQUEST']._serialized_start = 699
    _globals['_GETCATALOGITEMREQUEST']._serialized_end = 797
    _globals['_LISTCATALOGITEMSREQUEST']._serialized_start = 800
    _globals['_LISTCATALOGITEMSREQUEST']._serialized_end = 964
    _globals['_LISTCATALOGITEMSRESPONSE']._serialized_start = 967
    _globals['_LISTCATALOGITEMSRESPONSE']._serialized_end = 1097
    _globals['_UPDATECATALOGITEMREQUEST']._serialized_start = 1100
    _globals['_UPDATECATALOGITEMREQUEST']._serialized_end = 1333
    _globals['_DELETECATALOGITEMREQUEST']._serialized_start = 1335
    _globals['_DELETECATALOGITEMREQUEST']._serialized_end = 1436
    _globals['_CATALOGSERVICE']._serialized_start = 1439
    _globals['_CATALOGSERVICE']._serialized_end = 3125