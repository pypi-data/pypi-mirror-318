"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/search.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.datacatalog.v1 import common_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/datacatalog/v1/search.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/datacatalog/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xae\x03\n\x13SearchCatalogResult\x12I\n\x12search_result_type\x18\x01 \x01(\x0e2-.google.cloud.datacatalog.v1.SearchResultType\x12\x1d\n\x15search_result_subtype\x18\x02 \x01(\t\x12\x1e\n\x16relative_resource_name\x18\x03 \x01(\t\x12\x17\n\x0flinked_resource\x18\x04 \x01(\t\x12/\n\x0bmodify_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12O\n\x11integrated_system\x18\x08 \x01(\x0e2-.google.cloud.datacatalog.v1.IntegratedSystemB\x03\xe0A\x03H\x00\x12\x1f\n\x15user_specified_system\x18\t \x01(\tH\x00\x12\x1c\n\x14fully_qualified_name\x18\n \x01(\t\x12\x14\n\x0cdisplay_name\x18\x0c \x01(\t\x12\x13\n\x0bdescription\x18\r \x01(\tB\x08\n\x06system*d\n\x10SearchResultType\x12"\n\x1eSEARCH_RESULT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ENTRY\x10\x01\x12\x10\n\x0cTAG_TEMPLATE\x10\x02\x12\x0f\n\x0bENTRY_GROUP\x10\x03B\xc3\x01\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.search_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_SEARCHCATALOGRESULT'].fields_by_name['integrated_system']._loaded_options = None
    _globals['_SEARCHCATALOGRESULT'].fields_by_name['integrated_system']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHRESULTTYPE']._serialized_start = 614
    _globals['_SEARCHRESULTTYPE']._serialized_end = 714
    _globals['_SEARCHCATALOGRESULT']._serialized_start = 182
    _globals['_SEARCHCATALOGRESULT']._serialized_end = 612