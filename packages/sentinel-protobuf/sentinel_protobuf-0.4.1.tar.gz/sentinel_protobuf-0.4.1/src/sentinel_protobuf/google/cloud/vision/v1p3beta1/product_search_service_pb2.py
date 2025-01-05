"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p3beta1/product_search_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.vision.v1p3beta1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1p3beta1_dot_geometry__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/vision/v1p3beta1/product_search_service.proto\x12\x1dgoogle.cloud.vision.v1p3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/vision/v1p3beta1/geometry.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xb2\x02\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x1d\n\x10product_category\x18\x04 \x01(\tB\x03\xe0A\x05\x12G\n\x0eproduct_labels\x18\x05 \x03(\x0b2/.google.cloud.vision.v1p3beta1.Product.KeyValue\x1a&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:^\xeaA[\n\x1dvision.googleapis.com/Product\x12:projects/{project}/locations/{location}/products/{product}"\xfd\x01\n\nProductSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x123\n\nindex_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12,\n\x0bindex_error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03:h\xeaAe\n vision.googleapis.com/ProductSet\x12Aprojects/{project}/locations/{location}/productSets/{product_set}"\x85\x02\n\x0eReferenceImage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\x0ebounding_polys\x18\x03 \x03(\x0b2+.google.cloud.vision.v1p3beta1.BoundingPolyB\x03\xe0A\x01:\x88\x01\xeaA\x84\x01\n$vision.googleapis.com/ReferenceImage\x12\\projects/{project}/locations/{location}/products/{product}/referenceImages/{reference_image}"\xa3\x01\n\x14CreateProductRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12<\n\x07product\x18\x02 \x01(\x0b2&.google.cloud.vision.v1p3beta1.ProductB\x03\xe0A\x02\x12\x12\n\nproduct_id\x18\x03 \x01(\t"w\n\x13ListProductsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"i\n\x14ListProductsResponse\x128\n\x08products\x18\x01 \x03(\x0b2&.google.cloud.vision.v1p3beta1.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\x11GetProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product"\x85\x01\n\x14UpdateProductRequest\x12<\n\x07product\x18\x01 \x01(\x0b2&.google.cloud.vision.v1p3beta1.ProductB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x14DeleteProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product"\xb1\x01\n\x17CreateProductSetRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12C\n\x0bproduct_set\x18\x02 \x01(\x0b2).google.cloud.vision.v1p3beta1.ProductSetB\x03\xe0A\x02\x12\x16\n\x0eproduct_set_id\x18\x03 \x01(\t"z\n\x16ListProductSetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"s\n\x17ListProductSetsResponse\x12?\n\x0cproduct_sets\x18\x01 \x03(\x0b2).google.cloud.vision.v1p3beta1.ProductSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x14GetProductSetRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet"\x8f\x01\n\x17UpdateProductSetRequest\x12C\n\x0bproduct_set\x18\x01 \x01(\x0b2).google.cloud.vision.v1p3beta1.ProductSetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"Q\n\x17DeleteProductSetRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet"\xbd\x01\n\x1bCreateReferenceImageRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product\x12K\n\x0freference_image\x18\x02 \x01(\x0b2-.google.cloud.vision.v1p3beta1.ReferenceImageB\x03\xe0A\x02\x12\x1a\n\x12reference_image_id\x18\x03 \x01(\t"z\n\x1aListReferenceImagesRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x92\x01\n\x1bListReferenceImagesResponse\x12G\n\x10reference_images\x18\x01 \x03(\x0b2-.google.cloud.vision.v1p3beta1.ReferenceImage\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"V\n\x18GetReferenceImageRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$vision.googleapis.com/ReferenceImage"Y\n\x1bDeleteReferenceImageRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$vision.googleapis.com/ReferenceImage"\x8f\x01\n\x1dAddProductToProductSetRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet\x126\n\x07product\x18\x02 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product"\x94\x01\n"RemoveProductFromProductSetRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet\x126\n\x07product\x18\x02 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product"\x80\x01\n\x1fListProductsInProductSetRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"u\n ListProductsInProductSetResponse\x128\n\x08products\x18\x01 \x03(\x0b2&.google.cloud.vision.v1p3beta1.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"2\n\x1aImportProductSetsGcsSource\x12\x14\n\x0ccsv_file_uri\x18\x01 \x01(\t"y\n\x1cImportProductSetsInputConfig\x12O\n\ngcs_source\x18\x01 \x01(\x0b29.google.cloud.vision.v1p3beta1.ImportProductSetsGcsSourceH\x00B\x08\n\x06source"\xad\x01\n\x18ImportProductSetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12V\n\x0cinput_config\x18\x02 \x01(\x0b2;.google.cloud.vision.v1p3beta1.ImportProductSetsInputConfigB\x03\xe0A\x02"\x8a\x01\n\x19ImportProductSetsResponse\x12G\n\x10reference_images\x18\x01 \x03(\x0b2-.google.cloud.vision.v1p3beta1.ReferenceImage\x12$\n\x08statuses\x18\x02 \x03(\x0b2\x12.google.rpc.Status"\x9e\x02\n\x16BatchOperationMetadata\x12J\n\x05state\x18\x01 \x01(\x0e2;.google.cloud.vision.v1p3beta1.BatchOperationMetadata.State\x12/\n\x0bsubmit_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"Y\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\x0e\n\nSUCCESSFUL\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\r\n\tCANCELLED\x10\x042\xeb\x1e\n\rProductSearch\x12\xe6\x01\n\x10CreateProductSet\x126.google.cloud.vision.v1p3beta1.CreateProductSetRequest\x1a).google.cloud.vision.v1p3beta1.ProductSet"o\xdaA!parent,product_set,product_set_id\x82\xd3\xe4\x93\x02E"6/v1p3beta1/{parent=projects/*/locations/*}/productSets:\x0bproduct_set\x12\xc9\x01\n\x0fListProductSets\x125.google.cloud.vision.v1p3beta1.ListProductSetsRequest\x1a6.google.cloud.vision.v1p3beta1.ListProductSetsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1p3beta1/{parent=projects/*/locations/*}/productSets\x12\xb6\x01\n\rGetProductSet\x123.google.cloud.vision.v1p3beta1.GetProductSetRequest\x1a).google.cloud.vision.v1p3beta1.ProductSet"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1p3beta1/{name=projects/*/locations/*/productSets/*}\x12\xe8\x01\n\x10UpdateProductSet\x126.google.cloud.vision.v1p3beta1.UpdateProductSetRequest\x1a).google.cloud.vision.v1p3beta1.ProductSet"q\xdaA\x17product_set,update_mask\x82\xd3\xe4\x93\x02Q2B/v1p3beta1/{product_set.name=projects/*/locations/*/productSets/*}:\x0bproduct_set\x12\xa9\x01\n\x10DeleteProductSet\x126.google.cloud.vision.v1p3beta1.DeleteProductSetRequest\x1a\x16.google.protobuf.Empty"E\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1p3beta1/{name=projects/*/locations/*/productSets/*}\x12\xce\x01\n\rCreateProduct\x123.google.cloud.vision.v1p3beta1.CreateProductRequest\x1a&.google.cloud.vision.v1p3beta1.Product"`\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02>"3/v1p3beta1/{parent=projects/*/locations/*}/products:\x07product\x12\xbd\x01\n\x0cListProducts\x122.google.cloud.vision.v1p3beta1.ListProductsRequest\x1a3.google.cloud.vision.v1p3beta1.ListProductsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1p3beta1/{parent=projects/*/locations/*}/products\x12\xaa\x01\n\nGetProduct\x120.google.cloud.vision.v1p3beta1.GetProductRequest\x1a&.google.cloud.vision.v1p3beta1.Product"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1p3beta1/{name=projects/*/locations/*/products/*}\x12\xd0\x01\n\rUpdateProduct\x123.google.cloud.vision.v1p3beta1.UpdateProductRequest\x1a&.google.cloud.vision.v1p3beta1.Product"b\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02F2;/v1p3beta1/{product.name=projects/*/locations/*/products/*}:\x07product\x12\xa0\x01\n\rDeleteProduct\x123.google.cloud.vision.v1p3beta1.DeleteProductRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1p3beta1/{name=projects/*/locations/*/products/*}\x12\x8e\x02\n\x14CreateReferenceImage\x12:.google.cloud.vision.v1p3beta1.CreateReferenceImageRequest\x1a-.google.cloud.vision.v1p3beta1.ReferenceImage"\x8a\x01\xdaA)parent,reference_image,reference_image_id\x82\xd3\xe4\x93\x02X"E/v1p3beta1/{parent=projects/*/locations/*/products/*}/referenceImages:\x0freference_image\x12\xc0\x01\n\x14DeleteReferenceImage\x12:.google.cloud.vision.v1p3beta1.DeleteReferenceImageRequest\x1a\x16.google.protobuf.Empty"T\xdaA\x04name\x82\xd3\xe4\x93\x02G*E/v1p3beta1/{name=projects/*/locations/*/products/*/referenceImages/*}\x12\xe4\x01\n\x13ListReferenceImages\x129.google.cloud.vision.v1p3beta1.ListReferenceImagesRequest\x1a:.google.cloud.vision.v1p3beta1.ListReferenceImagesResponse"V\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1p3beta1/{parent=projects/*/locations/*/products/*}/referenceImages\x12\xd1\x01\n\x11GetReferenceImage\x127.google.cloud.vision.v1p3beta1.GetReferenceImageRequest\x1a-.google.cloud.vision.v1p3beta1.ReferenceImage"T\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1p3beta1/{name=projects/*/locations/*/products/*/referenceImages/*}\x12\xcb\x01\n\x16AddProductToProductSet\x12<.google.cloud.vision.v1p3beta1.AddProductToProductSetRequest\x1a\x16.google.protobuf.Empty"[\xdaA\x0cname,product\x82\xd3\xe4\x93\x02F"A/v1p3beta1/{name=projects/*/locations/*/productSets/*}:addProduct:\x01*\x12\xd8\x01\n\x1bRemoveProductFromProductSet\x12A.google.cloud.vision.v1p3beta1.RemoveProductFromProductSetRequest\x1a\x16.google.protobuf.Empty"^\xdaA\x0cname,product\x82\xd3\xe4\x93\x02I"D/v1p3beta1/{name=projects/*/locations/*/productSets/*}:removeProduct:\x01*\x12\xeb\x01\n\x18ListProductsInProductSet\x12>.google.cloud.vision.v1p3beta1.ListProductsInProductSetRequest\x1a?.google.cloud.vision.v1p3beta1.ListProductsInProductSetResponse"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1p3beta1/{name=projects/*/locations/*/productSets/*}/products\x12\x82\x02\n\x11ImportProductSets\x127.google.cloud.vision.v1p3beta1.ImportProductSetsRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaA3\n\x19ImportProductSetsResponse\x12\x16BatchOperationMetadata\xdaA\x13parent,input_config\x82\xd3\xe4\x93\x02B"=/v1p3beta1/{parent=projects/*/locations/*}/productSets:import:\x01*\x1av\xcaA\x15vision.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-visionB~\n!com.google.cloud.vision.v1p3beta1B\x19ProductSearchServiceProtoP\x01Z9cloud.google.com/go/vision/apiv1p3beta1/visionpb;visionpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p3beta1.product_search_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p3beta1B\x19ProductSearchServiceProtoP\x01Z9cloud.google.com/go/vision/apiv1p3beta1/visionpb;visionpb\xf8\x01\x01'
    _globals['_PRODUCT'].fields_by_name['product_category']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['product_category']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCT']._loaded_options = None
    _globals['_PRODUCT']._serialized_options = b'\xeaA[\n\x1dvision.googleapis.com/Product\x12:projects/{project}/locations/{location}/products/{product}'
    _globals['_PRODUCTSET'].fields_by_name['index_time']._loaded_options = None
    _globals['_PRODUCTSET'].fields_by_name['index_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTSET'].fields_by_name['index_error']._loaded_options = None
    _globals['_PRODUCTSET'].fields_by_name['index_error']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTSET']._loaded_options = None
    _globals['_PRODUCTSET']._serialized_options = b'\xeaAe\n vision.googleapis.com/ProductSet\x12Aprojects/{project}/locations/{location}/productSets/{product_set}'
    _globals['_REFERENCEIMAGE'].fields_by_name['uri']._loaded_options = None
    _globals['_REFERENCEIMAGE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCEIMAGE'].fields_by_name['bounding_polys']._loaded_options = None
    _globals['_REFERENCEIMAGE'].fields_by_name['bounding_polys']._serialized_options = b'\xe0A\x01'
    _globals['_REFERENCEIMAGE']._loaded_options = None
    _globals['_REFERENCEIMAGE']._serialized_options = b'\xeaA\x84\x01\n$vision.googleapis.com/ReferenceImage\x12\\projects/{project}/locations/{location}/products/{product}/referenceImages/{reference_image}'
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product'
    _globals['_UPDATEPRODUCTREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_UPDATEPRODUCTREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product'
    _globals['_CREATEPRODUCTSETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRODUCTSETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEPRODUCTSETREQUEST'].fields_by_name['product_set']._loaded_options = None
    _globals['_CREATEPRODUCTSETREQUEST'].fields_by_name['product_set']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPRODUCTSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRODUCTSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETPRODUCTSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRODUCTSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet'
    _globals['_UPDATEPRODUCTSETREQUEST'].fields_by_name['product_set']._loaded_options = None
    _globals['_UPDATEPRODUCTSETREQUEST'].fields_by_name['product_set']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPRODUCTSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRODUCTSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet'
    _globals['_CREATEREFERENCEIMAGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREFERENCEIMAGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product'
    _globals['_CREATEREFERENCEIMAGEREQUEST'].fields_by_name['reference_image']._loaded_options = None
    _globals['_CREATEREFERENCEIMAGEREQUEST'].fields_by_name['reference_image']._serialized_options = b'\xe0A\x02'
    _globals['_LISTREFERENCEIMAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREFERENCEIMAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product'
    _globals['_GETREFERENCEIMAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREFERENCEIMAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$vision.googleapis.com/ReferenceImage'
    _globals['_DELETEREFERENCEIMAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREFERENCEIMAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$vision.googleapis.com/ReferenceImage'
    _globals['_ADDPRODUCTTOPRODUCTSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ADDPRODUCTTOPRODUCTSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet'
    _globals['_ADDPRODUCTTOPRODUCTSETREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_ADDPRODUCTTOPRODUCTSETREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product'
    _globals['_REMOVEPRODUCTFROMPRODUCTSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REMOVEPRODUCTFROMPRODUCTSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet'
    _globals['_REMOVEPRODUCTFROMPRODUCTSETREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_REMOVEPRODUCTFROMPRODUCTSETREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvision.googleapis.com/Product'
    _globals['_LISTPRODUCTSINPRODUCTSETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTPRODUCTSINPRODUCTSETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n vision.googleapis.com/ProductSet'
    _globals['_IMPORTPRODUCTSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTPRODUCTSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_IMPORTPRODUCTSETSREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTPRODUCTSETSREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTSEARCH']._loaded_options = None
    _globals['_PRODUCTSEARCH']._serialized_options = b'\xcaA\x15vision.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-vision'
    _globals['_PRODUCTSEARCH'].methods_by_name['CreateProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['CreateProductSet']._serialized_options = b'\xdaA!parent,product_set,product_set_id\x82\xd3\xe4\x93\x02E"6/v1p3beta1/{parent=projects/*/locations/*}/productSets:\x0bproduct_set'
    _globals['_PRODUCTSEARCH'].methods_by_name['ListProductSets']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['ListProductSets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1p3beta1/{parent=projects/*/locations/*}/productSets'
    _globals['_PRODUCTSEARCH'].methods_by_name['GetProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['GetProductSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1p3beta1/{name=projects/*/locations/*/productSets/*}'
    _globals['_PRODUCTSEARCH'].methods_by_name['UpdateProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['UpdateProductSet']._serialized_options = b'\xdaA\x17product_set,update_mask\x82\xd3\xe4\x93\x02Q2B/v1p3beta1/{product_set.name=projects/*/locations/*/productSets/*}:\x0bproduct_set'
    _globals['_PRODUCTSEARCH'].methods_by_name['DeleteProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['DeleteProductSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1p3beta1/{name=projects/*/locations/*/productSets/*}'
    _globals['_PRODUCTSEARCH'].methods_by_name['CreateProduct']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['CreateProduct']._serialized_options = b'\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02>"3/v1p3beta1/{parent=projects/*/locations/*}/products:\x07product'
    _globals['_PRODUCTSEARCH'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1p3beta1/{parent=projects/*/locations/*}/products'
    _globals['_PRODUCTSEARCH'].methods_by_name['GetProduct']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1p3beta1/{name=projects/*/locations/*/products/*}'
    _globals['_PRODUCTSEARCH'].methods_by_name['UpdateProduct']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['UpdateProduct']._serialized_options = b'\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02F2;/v1p3beta1/{product.name=projects/*/locations/*/products/*}:\x07product'
    _globals['_PRODUCTSEARCH'].methods_by_name['DeleteProduct']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['DeleteProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1p3beta1/{name=projects/*/locations/*/products/*}'
    _globals['_PRODUCTSEARCH'].methods_by_name['CreateReferenceImage']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['CreateReferenceImage']._serialized_options = b'\xdaA)parent,reference_image,reference_image_id\x82\xd3\xe4\x93\x02X"E/v1p3beta1/{parent=projects/*/locations/*/products/*}/referenceImages:\x0freference_image'
    _globals['_PRODUCTSEARCH'].methods_by_name['DeleteReferenceImage']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['DeleteReferenceImage']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G*E/v1p3beta1/{name=projects/*/locations/*/products/*/referenceImages/*}'
    _globals['_PRODUCTSEARCH'].methods_by_name['ListReferenceImages']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['ListReferenceImages']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1p3beta1/{parent=projects/*/locations/*/products/*}/referenceImages'
    _globals['_PRODUCTSEARCH'].methods_by_name['GetReferenceImage']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['GetReferenceImage']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1p3beta1/{name=projects/*/locations/*/products/*/referenceImages/*}'
    _globals['_PRODUCTSEARCH'].methods_by_name['AddProductToProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['AddProductToProductSet']._serialized_options = b'\xdaA\x0cname,product\x82\xd3\xe4\x93\x02F"A/v1p3beta1/{name=projects/*/locations/*/productSets/*}:addProduct:\x01*'
    _globals['_PRODUCTSEARCH'].methods_by_name['RemoveProductFromProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['RemoveProductFromProductSet']._serialized_options = b'\xdaA\x0cname,product\x82\xd3\xe4\x93\x02I"D/v1p3beta1/{name=projects/*/locations/*/productSets/*}:removeProduct:\x01*'
    _globals['_PRODUCTSEARCH'].methods_by_name['ListProductsInProductSet']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['ListProductsInProductSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1p3beta1/{name=projects/*/locations/*/productSets/*}/products'
    _globals['_PRODUCTSEARCH'].methods_by_name['ImportProductSets']._loaded_options = None
    _globals['_PRODUCTSEARCH'].methods_by_name['ImportProductSets']._serialized_options = b'\xcaA3\n\x19ImportProductSetsResponse\x12\x16BatchOperationMetadata\xdaA\x13parent,input_config\x82\xd3\xe4\x93\x02B"=/v1p3beta1/{parent=projects/*/locations/*}/productSets:import:\x01*'
    _globals['_PRODUCT']._serialized_start = 413
    _globals['_PRODUCT']._serialized_end = 719
    _globals['_PRODUCT_KEYVALUE']._serialized_start = 585
    _globals['_PRODUCT_KEYVALUE']._serialized_end = 623
    _globals['_PRODUCTSET']._serialized_start = 722
    _globals['_PRODUCTSET']._serialized_end = 975
    _globals['_REFERENCEIMAGE']._serialized_start = 978
    _globals['_REFERENCEIMAGE']._serialized_end = 1239
    _globals['_CREATEPRODUCTREQUEST']._serialized_start = 1242
    _globals['_CREATEPRODUCTREQUEST']._serialized_end = 1405
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 1407
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 1526
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 1528
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 1633
    _globals['_GETPRODUCTREQUEST']._serialized_start = 1635
    _globals['_GETPRODUCTREQUEST']._serialized_end = 1707
    _globals['_UPDATEPRODUCTREQUEST']._serialized_start = 1710
    _globals['_UPDATEPRODUCTREQUEST']._serialized_end = 1843
    _globals['_DELETEPRODUCTREQUEST']._serialized_start = 1845
    _globals['_DELETEPRODUCTREQUEST']._serialized_end = 1920
    _globals['_CREATEPRODUCTSETREQUEST']._serialized_start = 1923
    _globals['_CREATEPRODUCTSETREQUEST']._serialized_end = 2100
    _globals['_LISTPRODUCTSETSREQUEST']._serialized_start = 2102
    _globals['_LISTPRODUCTSETSREQUEST']._serialized_end = 2224
    _globals['_LISTPRODUCTSETSRESPONSE']._serialized_start = 2226
    _globals['_LISTPRODUCTSETSRESPONSE']._serialized_end = 2341
    _globals['_GETPRODUCTSETREQUEST']._serialized_start = 2343
    _globals['_GETPRODUCTSETREQUEST']._serialized_end = 2421
    _globals['_UPDATEPRODUCTSETREQUEST']._serialized_start = 2424
    _globals['_UPDATEPRODUCTSETREQUEST']._serialized_end = 2567
    _globals['_DELETEPRODUCTSETREQUEST']._serialized_start = 2569
    _globals['_DELETEPRODUCTSETREQUEST']._serialized_end = 2650
    _globals['_CREATEREFERENCEIMAGEREQUEST']._serialized_start = 2653
    _globals['_CREATEREFERENCEIMAGEREQUEST']._serialized_end = 2842
    _globals['_LISTREFERENCEIMAGESREQUEST']._serialized_start = 2844
    _globals['_LISTREFERENCEIMAGESREQUEST']._serialized_end = 2966
    _globals['_LISTREFERENCEIMAGESRESPONSE']._serialized_start = 2969
    _globals['_LISTREFERENCEIMAGESRESPONSE']._serialized_end = 3115
    _globals['_GETREFERENCEIMAGEREQUEST']._serialized_start = 3117
    _globals['_GETREFERENCEIMAGEREQUEST']._serialized_end = 3203
    _globals['_DELETEREFERENCEIMAGEREQUEST']._serialized_start = 3205
    _globals['_DELETEREFERENCEIMAGEREQUEST']._serialized_end = 3294
    _globals['_ADDPRODUCTTOPRODUCTSETREQUEST']._serialized_start = 3297
    _globals['_ADDPRODUCTTOPRODUCTSETREQUEST']._serialized_end = 3440
    _globals['_REMOVEPRODUCTFROMPRODUCTSETREQUEST']._serialized_start = 3443
    _globals['_REMOVEPRODUCTFROMPRODUCTSETREQUEST']._serialized_end = 3591
    _globals['_LISTPRODUCTSINPRODUCTSETREQUEST']._serialized_start = 3594
    _globals['_LISTPRODUCTSINPRODUCTSETREQUEST']._serialized_end = 3722
    _globals['_LISTPRODUCTSINPRODUCTSETRESPONSE']._serialized_start = 3724
    _globals['_LISTPRODUCTSINPRODUCTSETRESPONSE']._serialized_end = 3841
    _globals['_IMPORTPRODUCTSETSGCSSOURCE']._serialized_start = 3843
    _globals['_IMPORTPRODUCTSETSGCSSOURCE']._serialized_end = 3893
    _globals['_IMPORTPRODUCTSETSINPUTCONFIG']._serialized_start = 3895
    _globals['_IMPORTPRODUCTSETSINPUTCONFIG']._serialized_end = 4016
    _globals['_IMPORTPRODUCTSETSREQUEST']._serialized_start = 4019
    _globals['_IMPORTPRODUCTSETSREQUEST']._serialized_end = 4192
    _globals['_IMPORTPRODUCTSETSRESPONSE']._serialized_start = 4195
    _globals['_IMPORTPRODUCTSETSRESPONSE']._serialized_end = 4333
    _globals['_BATCHOPERATIONMETADATA']._serialized_start = 4336
    _globals['_BATCHOPERATIONMETADATA']._serialized_end = 4622
    _globals['_BATCHOPERATIONMETADATA_STATE']._serialized_start = 4533
    _globals['_BATCHOPERATIONMETADATA_STATE']._serialized_end = 4622
    _globals['_PRODUCTSEARCH']._serialized_start = 4625
    _globals['_PRODUCTSEARCH']._serialized_end = 8572