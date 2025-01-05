"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1/dataplex_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.datacatalog.v1 import common_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_common__pb2
from .....google.cloud.datacatalog.v1 import physical_schema_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_physical__schema__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/datacatalog/v1/dataplex_spec.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a(google/cloud/datacatalog/v1/common.proto\x1a1google/cloud/datacatalog/v1/physical_schema.proto"\x8f\x01\n\x0cDataplexSpec\x12\r\n\x05asset\x18\x01 \x01(\t\x12@\n\x0bdata_format\x18\x02 \x01(\x0b2+.google.cloud.datacatalog.v1.PhysicalSchema\x12\x1a\n\x12compression_format\x18\x03 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t"W\n\x13DataplexFilesetSpec\x12@\n\rdataplex_spec\x18\x01 \x01(\x0b2).google.cloud.datacatalog.v1.DataplexSpec"\xb8\x01\n\x11DataplexTableSpec\x12K\n\x0fexternal_tables\x18\x01 \x03(\x0b22.google.cloud.datacatalog.v1.DataplexExternalTable\x12@\n\rdataplex_spec\x18\x02 \x01(\x0b2).google.cloud.datacatalog.v1.DataplexSpec\x12\x14\n\x0cuser_managed\x18\x03 \x01(\x08"\xaf\x01\n\x15DataplexExternalTable\x12=\n\x06system\x18\x01 \x01(\x0e2-.google.cloud.datacatalog.v1.IntegratedSystem\x12\x1c\n\x14fully_qualified_name\x18\x1c \x01(\t\x12\x1d\n\x15google_cloud_resource\x18\x03 \x01(\t\x12\x1a\n\x12data_catalog_entry\x18\x04 \x01(\tB\xd6\x01\n\x1fcom.google.cloud.datacatalog.v1B\x11DataplexSpecProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.dataplex_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1B\x11DataplexSpecProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_DATAPLEXSPEC']._serialized_start = 174
    _globals['_DATAPLEXSPEC']._serialized_end = 317
    _globals['_DATAPLEXFILESETSPEC']._serialized_start = 319
    _globals['_DATAPLEXFILESETSPEC']._serialized_end = 406
    _globals['_DATAPLEXTABLESPEC']._serialized_start = 409
    _globals['_DATAPLEXTABLESPEC']._serialized_end = 593
    _globals['_DATAPLEXEXTERNALTABLE']._serialized_start = 596
    _globals['_DATAPLEXEXTERNALTABLE']._serialized_end = 771