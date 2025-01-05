"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/search.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/datacatalog/v1beta1/search.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xee\x01\n\x13SearchCatalogResult\x12N\n\x12search_result_type\x18\x01 \x01(\x0e22.google.cloud.datacatalog.v1beta1.SearchResultType\x12\x1d\n\x15search_result_subtype\x18\x02 \x01(\t\x12\x1e\n\x16relative_resource_name\x18\x03 \x01(\t\x12\x17\n\x0flinked_resource\x18\x04 \x01(\t\x12/\n\x0bmodify_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp*d\n\x10SearchResultType\x12"\n\x1eSEARCH_RESULT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ENTRY\x10\x01\x12\x10\n\x0cTAG_TEMPLATE\x10\x02\x12\x0f\n\x0bENTRY_GROUP\x10\x03B\xdc\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.search_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_SEARCHRESULTTYPE']._serialized_start = 390
    _globals['_SEARCHRESULTTYPE']._serialized_end = 490
    _globals['_SEARCHCATALOGRESULT']._serialized_start = 150
    _globals['_SEARCHCATALOGRESULT']._serialized_end = 388