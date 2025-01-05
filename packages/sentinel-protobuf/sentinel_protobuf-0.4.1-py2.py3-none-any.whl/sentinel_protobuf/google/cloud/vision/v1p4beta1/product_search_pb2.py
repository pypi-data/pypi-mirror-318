"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p4beta1/product_search.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.vision.v1p4beta1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1p4beta1_dot_geometry__pb2
from .....google.cloud.vision.v1p4beta1 import product_search_service_pb2 as google_dot_cloud_dot_vision_dot_v1p4beta1_dot_product__search__service__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/vision/v1p4beta1/product_search.proto\x12\x1dgoogle.cloud.vision.v1p4beta1\x1a\x19google/api/resource.proto\x1a,google/cloud/vision/v1p4beta1/geometry.proto\x1a:google/cloud/vision/v1p4beta1/product_search_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc1\x01\n\x13ProductSearchParams\x12B\n\rbounding_poly\x18\t \x01(\x0b2+.google.cloud.vision.v1p4beta1.BoundingPoly\x12:\n\x0bproduct_set\x18\x06 \x01(\tB%\xfaA"\n vision.googleapis.com/ProductSet\x12\x1a\n\x12product_categories\x18\x07 \x03(\t\x12\x0e\n\x06filter\x18\x08 \x01(\t"\xb2\x05\n\x14ProductSearchResults\x12.\n\nindex_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12K\n\x07results\x18\x05 \x03(\x0b2:.google.cloud.vision.v1p4beta1.ProductSearchResults.Result\x12b\n\x17product_grouped_results\x18\x06 \x03(\x0b2A.google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult\x1a_\n\x06Result\x127\n\x07product\x18\x01 \x01(\x0b2&.google.cloud.vision.v1p4beta1.Product\x12\r\n\x05score\x18\x02 \x01(\x02\x12\r\n\x05image\x18\x03 \x01(\t\x1aS\n\x10ObjectAnnotation\x12\x0b\n\x03mid\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x02\x1a\x82\x02\n\rGroupedResult\x12B\n\rbounding_poly\x18\x01 \x01(\x0b2+.google.cloud.vision.v1p4beta1.BoundingPoly\x12K\n\x07results\x18\x02 \x03(\x0b2:.google.cloud.vision.v1p4beta1.ProductSearchResults.Result\x12`\n\x12object_annotations\x18\x03 \x03(\x0b2D.google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotationB~\n!com.google.cloud.vision.v1p4beta1B\x12ProductSearchProtoP\x01Z9cloud.google.com/go/vision/apiv1p4beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p4beta1.product_search_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p4beta1B\x12ProductSearchProtoP\x01Z9cloud.google.com/go/vision/apiv1p4beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_PRODUCTSEARCHPARAMS'].fields_by_name['product_set']._loaded_options = None
    _globals['_PRODUCTSEARCHPARAMS'].fields_by_name['product_set']._serialized_options = b'\xfaA"\n vision.googleapis.com/ProductSet'
    _globals['_PRODUCTSEARCHPARAMS']._serialized_start = 252
    _globals['_PRODUCTSEARCHPARAMS']._serialized_end = 445
    _globals['_PRODUCTSEARCHRESULTS']._serialized_start = 448
    _globals['_PRODUCTSEARCHRESULTS']._serialized_end = 1138
    _globals['_PRODUCTSEARCHRESULTS_RESULT']._serialized_start = 697
    _globals['_PRODUCTSEARCHRESULTS_RESULT']._serialized_end = 792
    _globals['_PRODUCTSEARCHRESULTS_OBJECTANNOTATION']._serialized_start = 794
    _globals['_PRODUCTSEARCHRESULTS_OBJECTANNOTATION']._serialized_end = 877
    _globals['_PRODUCTSEARCHRESULTS_GROUPEDRESULT']._serialized_start = 880
    _globals['_PRODUCTSEARCHRESULTS_GROUPEDRESULT']._serialized_end = 1138