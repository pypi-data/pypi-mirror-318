"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/table_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/datacatalog/v1beta1/table_spec.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf7\x01\n\x11BigQueryTableSpec\x12Q\n\x11table_source_type\x18\x01 \x01(\x0e21.google.cloud.datacatalog.v1beta1.TableSourceTypeB\x03\xe0A\x03\x12?\n\tview_spec\x18\x02 \x01(\x0b2*.google.cloud.datacatalog.v1beta1.ViewSpecH\x00\x12A\n\ntable_spec\x18\x03 \x01(\x0b2+.google.cloud.datacatalog.v1beta1.TableSpecH\x00B\x0b\n\ttype_spec"#\n\x08ViewSpec\x12\x17\n\nview_query\x18\x01 \x01(\tB\x03\xe0A\x03"L\n\tTableSpec\x12?\n\rgrouped_entry\x18\x01 \x01(\tB(\xe0A\x03\xfaA"\n datacatalog.googleapis.com/Entry"\x89\x01\n\x17BigQueryDateShardedSpec\x129\n\x07dataset\x18\x01 \x01(\tB(\xe0A\x03\xfaA"\n datacatalog.googleapis.com/Entry\x12\x19\n\x0ctable_prefix\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bshard_count\x18\x03 \x01(\x03B\x03\xe0A\x03*{\n\x0fTableSourceType\x12!\n\x1dTABLE_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rBIGQUERY_VIEW\x10\x02\x12\x12\n\x0eBIGQUERY_TABLE\x10\x05\x12\x1e\n\x1aBIGQUERY_MATERIALIZED_VIEW\x10\x07B\xdc\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.table_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_BIGQUERYTABLESPEC'].fields_by_name['table_source_type']._loaded_options = None
    _globals['_BIGQUERYTABLESPEC'].fields_by_name['table_source_type']._serialized_options = b'\xe0A\x03'
    _globals['_VIEWSPEC'].fields_by_name['view_query']._loaded_options = None
    _globals['_VIEWSPEC'].fields_by_name['view_query']._serialized_options = b'\xe0A\x03'
    _globals['_TABLESPEC'].fields_by_name['grouped_entry']._loaded_options = None
    _globals['_TABLESPEC'].fields_by_name['grouped_entry']._serialized_options = b'\xe0A\x03\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_BIGQUERYDATESHARDEDSPEC'].fields_by_name['dataset']._loaded_options = None
    _globals['_BIGQUERYDATESHARDEDSPEC'].fields_by_name['dataset']._serialized_options = b'\xe0A\x03\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_BIGQUERYDATESHARDEDSPEC'].fields_by_name['table_prefix']._loaded_options = None
    _globals['_BIGQUERYDATESHARDEDSPEC'].fields_by_name['table_prefix']._serialized_options = b'\xe0A\x03'
    _globals['_BIGQUERYDATESHARDEDSPEC'].fields_by_name['shard_count']._loaded_options = None
    _globals['_BIGQUERYDATESHARDEDSPEC'].fields_by_name['shard_count']._serialized_options = b'\xe0A\x03'
    _globals['_TABLESOURCETYPE']._serialized_start = 652
    _globals['_TABLESOURCETYPE']._serialized_end = 775
    _globals['_BIGQUERYTABLESPEC']._serialized_start = 148
    _globals['_BIGQUERYTABLESPEC']._serialized_end = 395
    _globals['_VIEWSPEC']._serialized_start = 397
    _globals['_VIEWSPEC']._serialized_end = 432
    _globals['_TABLESPEC']._serialized_start = 434
    _globals['_TABLESPEC']._serialized_end = 510
    _globals['_BIGQUERYDATESHARDEDSPEC']._serialized_start = 513
    _globals['_BIGQUERYDATESHARDEDSPEC']._serialized_end = 650