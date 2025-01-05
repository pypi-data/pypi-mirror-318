"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/privatecatalog/v1beta1/private_catalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/privatecatalog/v1beta1/private_catalog.proto\x12#google.cloud.privatecatalog.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"d\n\x15SearchCatalogsRequest\x12\x15\n\x08resource\x18\x01 \x01(\tB\x03\xe0A\x02\x12\r\n\x05query\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"q\n\x16SearchCatalogsResponse\x12>\n\x08catalogs\x18\x01 \x03(\x0b2,.google.cloud.privatecatalog.v1beta1.Catalog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"d\n\x15SearchProductsRequest\x12\x15\n\x08resource\x18\x01 \x01(\tB\x03\xe0A\x02\x12\r\n\x05query\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"q\n\x16SearchProductsResponse\x12>\n\x08products\x18\x01 \x03(\x0b2,.google.cloud.privatecatalog.v1beta1.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"i\n\x15SearchVersionsRequest\x12\x15\n\x08resource\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"q\n\x16SearchVersionsResponse\x12>\n\x08versions\x18\x01 \x03(\x0b2,.google.cloud.privatecatalog.v1beta1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x82\x02\n\x07Catalog\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:C\xeaA@\n*cloudprivatecatalog.googleapis.com/Catalog\x12\x12catalogs/{catalog}"\x8c\x03\n\x07Product\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nasset_type\x18\x02 \x01(\tB\x03\xe0A\x03\x129\n\x10display_metadata\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x06\xe0A\x02\xe0A\x03\x12\x15\n\x08icon_uri\x18\x04 \x01(\tB\x03\xe0A\x03\x12R\n\x10asset_references\x18\n \x03(\x0b23.google.cloud.privatecatalog.v1beta1.AssetReferenceB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:C\xeaA@\n*cloudprivatecatalog.googleapis.com/Product\x12\x12products/{product}"\xde\x05\n\x0eAssetReference\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03\x12@\n\x06inputs\x18\x06 \x01(\x0b2+.google.cloud.privatecatalog.v1beta1.InputsB\x03\xe0A\x03\x12h\n\x11validation_status\x18\x07 \x01(\x0e2H.google.cloud.privatecatalog.v1beta1.AssetReference.AssetValidationStateB\x03\xe0A\x03\x12@\n\x14validation_operation\x18\x08 \x01(\x0b2\x1d.google.longrunning.OperationB\x03\xe0A\x03\x12\x14\n\x05asset\x18\n \x01(\tB\x03\xe0A\x03H\x00\x12\x19\n\x08gcs_path\x18\x0b \x01(\tB\x05\x18\x01\xe0A\x03H\x00\x12I\n\ngit_source\x18\x0f \x01(\x0b2..google.cloud.privatecatalog.v1beta1.GitSourceB\x03\xe0A\x03H\x00\x12G\n\ngcs_source\x18\x10 \x01(\x0b2..google.cloud.privatecatalog.v1beta1.GcsSourceB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x07version\x18\x0e \x01(\tB\x02\x18\x01"c\n\x14AssetValidationState\x12&\n"ASSET_VALIDATION_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\t\n\x05VALID\x10\x02\x12\x0b\n\x07INVALID\x10\x03B\x08\n\x06source":\n\x06Inputs\x120\n\nparameters\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03"q\n\tGcsSource\x12\x15\n\x08gcs_path\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\ngeneration\x18\x02 \x01(\x03B\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"`\n\tGitSource\x12\x0c\n\x04repo\x18\x01 \x01(\t\x12\x0b\n\x03dir\x18\x02 \x01(\t\x12\x10\n\x06commit\x18\x03 \x01(\tH\x00\x12\x10\n\x06branch\x18\x04 \x01(\tH\x00\x12\r\n\x03tag\x18\x05 \x01(\tH\x00B\x05\n\x03ref"\xba\x02\n\x07Version\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03\x12+\n\x05asset\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:i\xeaAf\n*cloudprivatecatalog.googleapis.com/Version\x128catalogs/{catalog}/products/{product}/versions/{version}2\xf2\x07\n\x0ePrivateCatalog\x12\xab\x02\n\x0eSearchCatalogs\x12:.google.cloud.privatecatalog.v1beta1.SearchCatalogsRequest\x1a;.google.cloud.privatecatalog.v1beta1.SearchCatalogsResponse"\x9f\x01\x82\xd3\xe4\x93\x02\x98\x01\x12./v1beta1/{resource=projects/*}/catalogs:searchZ5\x123/v1beta1/{resource=organizations/*}/catalogs:searchZ/\x12-/v1beta1/{resource=folders/*}/catalogs:search\x12\xab\x02\n\x0eSearchProducts\x12:.google.cloud.privatecatalog.v1beta1.SearchProductsRequest\x1a;.google.cloud.privatecatalog.v1beta1.SearchProductsResponse"\x9f\x01\x82\xd3\xe4\x93\x02\x98\x01\x12./v1beta1/{resource=projects/*}/products:searchZ5\x123/v1beta1/{resource=organizations/*}/products:searchZ/\x12-/v1beta1/{resource=folders/*}/products:search\x12\xab\x02\n\x0eSearchVersions\x12:.google.cloud.privatecatalog.v1beta1.SearchVersionsRequest\x1a;.google.cloud.privatecatalog.v1beta1.SearchVersionsResponse"\x9f\x01\x82\xd3\xe4\x93\x02\x98\x01\x12./v1beta1/{resource=projects/*}/versions:searchZ5\x123/v1beta1/{resource=organizations/*}/versions:searchZ/\x12-/v1beta1/{resource=folders/*}/versions:search\x1aV\xcaA"cloudprivatecatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x86\x02\n\'com.google.cloud.privatecatalog.v1beta1B\x13PrivateCatalogProtoP\x01ZOcloud.google.com/go/privatecatalog/apiv1beta1/privatecatalogpb;privatecatalogpb\xaa\x02#Google.Cloud.PrivateCatalog.V1Beta1\xca\x02#Google\\Cloud\\PrivateCatalog\\V1beta1\xea\x02&Google::Cloud::PrivateCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.privatecatalog.v1beta1.private_catalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.privatecatalog.v1beta1B\x13PrivateCatalogProtoP\x01ZOcloud.google.com/go/privatecatalog/apiv1beta1/privatecatalogpb;privatecatalogpb\xaa\x02#Google.Cloud.PrivateCatalog.V1Beta1\xca\x02#Google\\Cloud\\PrivateCatalog\\V1beta1\xea\x02&Google::Cloud::PrivateCatalog::V1beta1"
    _globals['_SEARCHCATALOGSREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_SEARCHCATALOGSREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHPRODUCTSREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_SEARCHPRODUCTSREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVERSIONSREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_SEARCHVERSIONSREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVERSIONSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHVERSIONSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOG'].fields_by_name['name']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['display_name']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['description']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['create_time']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG'].fields_by_name['update_time']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOG']._loaded_options = None
    _globals['_CATALOG']._serialized_options = b'\xeaA@\n*cloudprivatecatalog.googleapis.com/Catalog\x12\x12catalogs/{catalog}'
    _globals['_PRODUCT'].fields_by_name['name']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['asset_type']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['asset_type']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['display_metadata']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['display_metadata']._serialized_options = b'\xe0A\x02\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['icon_uri']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['icon_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['asset_references']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['asset_references']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['create_time']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['update_time']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT']._loaded_options = None
    _globals['_PRODUCT']._serialized_options = b'\xeaA@\n*cloudprivatecatalog.googleapis.com/Product\x12\x12products/{product}'
    _globals['_ASSETREFERENCE'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['description']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['inputs']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['inputs']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['validation_status']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['validation_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['validation_operation']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['validation_operation']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['asset']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['gcs_path']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['gcs_path']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['git_source']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['git_source']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETREFERENCE'].fields_by_name['version']._loaded_options = None
    _globals['_ASSETREFERENCE'].fields_by_name['version']._serialized_options = b'\x18\x01'
    _globals['_INPUTS'].fields_by_name['parameters']._loaded_options = None
    _globals['_INPUTS'].fields_by_name['parameters']._serialized_options = b'\xe0A\x03'
    _globals['_GCSSOURCE'].fields_by_name['gcs_path']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['gcs_path']._serialized_options = b'\xe0A\x03'
    _globals['_GCSSOURCE'].fields_by_name['generation']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['generation']._serialized_options = b'\xe0A\x03'
    _globals['_GCSSOURCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['name']._loaded_options = None
    _globals['_VERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['description']._loaded_options = None
    _globals['_VERSION'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['asset']._loaded_options = None
    _globals['_VERSION'].fields_by_name['asset']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_VERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_VERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_VERSION']._loaded_options = None
    _globals['_VERSION']._serialized_options = b'\xeaAf\n*cloudprivatecatalog.googleapis.com/Version\x128catalogs/{catalog}/products/{product}/versions/{version}'
    _globals['_PRIVATECATALOG']._loaded_options = None
    _globals['_PRIVATECATALOG']._serialized_options = b'\xcaA"cloudprivatecatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PRIVATECATALOG'].methods_by_name['SearchCatalogs']._loaded_options = None
    _globals['_PRIVATECATALOG'].methods_by_name['SearchCatalogs']._serialized_options = b'\x82\xd3\xe4\x93\x02\x98\x01\x12./v1beta1/{resource=projects/*}/catalogs:searchZ5\x123/v1beta1/{resource=organizations/*}/catalogs:searchZ/\x12-/v1beta1/{resource=folders/*}/catalogs:search'
    _globals['_PRIVATECATALOG'].methods_by_name['SearchProducts']._loaded_options = None
    _globals['_PRIVATECATALOG'].methods_by_name['SearchProducts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x98\x01\x12./v1beta1/{resource=projects/*}/products:searchZ5\x123/v1beta1/{resource=organizations/*}/products:searchZ/\x12-/v1beta1/{resource=folders/*}/products:search'
    _globals['_PRIVATECATALOG'].methods_by_name['SearchVersions']._loaded_options = None
    _globals['_PRIVATECATALOG'].methods_by_name['SearchVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x98\x01\x12./v1beta1/{resource=projects/*}/versions:searchZ5\x123/v1beta1/{resource=organizations/*}/versions:searchZ/\x12-/v1beta1/{resource=folders/*}/versions:search'
    _globals['_SEARCHCATALOGSREQUEST']._serialized_start = 313
    _globals['_SEARCHCATALOGSREQUEST']._serialized_end = 413
    _globals['_SEARCHCATALOGSRESPONSE']._serialized_start = 415
    _globals['_SEARCHCATALOGSRESPONSE']._serialized_end = 528
    _globals['_SEARCHPRODUCTSREQUEST']._serialized_start = 530
    _globals['_SEARCHPRODUCTSREQUEST']._serialized_end = 630
    _globals['_SEARCHPRODUCTSRESPONSE']._serialized_start = 632
    _globals['_SEARCHPRODUCTSRESPONSE']._serialized_end = 745
    _globals['_SEARCHVERSIONSREQUEST']._serialized_start = 747
    _globals['_SEARCHVERSIONSREQUEST']._serialized_end = 852
    _globals['_SEARCHVERSIONSRESPONSE']._serialized_start = 854
    _globals['_SEARCHVERSIONSRESPONSE']._serialized_end = 967
    _globals['_CATALOG']._serialized_start = 970
    _globals['_CATALOG']._serialized_end = 1228
    _globals['_PRODUCT']._serialized_start = 1231
    _globals['_PRODUCT']._serialized_end = 1627
    _globals['_ASSETREFERENCE']._serialized_start = 1630
    _globals['_ASSETREFERENCE']._serialized_end = 2364
    _globals['_ASSETREFERENCE_ASSETVALIDATIONSTATE']._serialized_start = 2255
    _globals['_ASSETREFERENCE_ASSETVALIDATIONSTATE']._serialized_end = 2354
    _globals['_INPUTS']._serialized_start = 2366
    _globals['_INPUTS']._serialized_end = 2424
    _globals['_GCSSOURCE']._serialized_start = 2426
    _globals['_GCSSOURCE']._serialized_end = 2539
    _globals['_GITSOURCE']._serialized_start = 2541
    _globals['_GITSOURCE']._serialized_end = 2637
    _globals['_VERSION']._serialized_start = 2640
    _globals['_VERSION']._serialized_end = 2954
    _globals['_PRIVATECATALOG']._serialized_start = 2957
    _globals['_PRIVATECATALOG']._serialized_end = 3967