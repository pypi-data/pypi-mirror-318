"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/dataset_metadata.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/aiplatform/v1beta1/schema/dataset_metadata.proto\x12&google.cloud.aiplatform.v1beta1.schema"H\n\x14ImageDatasetMetadata\x12\x1c\n\x14data_item_schema_uri\x18\x01 \x01(\t\x12\x12\n\ngcs_bucket\x18\x02 \x01(\t"G\n\x13TextDatasetMetadata\x12\x1c\n\x14data_item_schema_uri\x18\x01 \x01(\t\x12\x12\n\ngcs_bucket\x18\x02 \x01(\t"H\n\x14VideoDatasetMetadata\x12\x1c\n\x14data_item_schema_uri\x18\x01 \x01(\t\x12\x12\n\ngcs_bucket\x18\x02 \x01(\t"\x93\x03\n\x15TablesDatasetMetadata\x12_\n\x0cinput_config\x18\x01 \x01(\x0b2I.google.cloud.aiplatform.v1beta1.schema.TablesDatasetMetadata.InputConfig\x1a\xdf\x01\n\x0bInputConfig\x12]\n\ngcs_source\x18\x01 \x01(\x0b2G.google.cloud.aiplatform.v1beta1.schema.TablesDatasetMetadata.GcsSourceH\x00\x12g\n\x0fbigquery_source\x18\x02 \x01(\x0b2L.google.cloud.aiplatform.v1beta1.schema.TablesDatasetMetadata.BigQuerySourceH\x00B\x08\n\x06source\x1a\x18\n\tGcsSource\x12\x0b\n\x03uri\x18\x01 \x03(\t\x1a\x1d\n\x0eBigQuerySource\x12\x0b\n\x03uri\x18\x01 \x01(\t"\xdf\x03\n\x19TimeSeriesDatasetMetadata\x12c\n\x0cinput_config\x18\x01 \x01(\x0b2M.google.cloud.aiplatform.v1beta1.schema.TimeSeriesDatasetMetadata.InputConfig\x12%\n\x1dtime_series_identifier_column\x18\x02 \x01(\t\x12\x13\n\x0btime_column\x18\x03 \x01(\t\x1a\xe7\x01\n\x0bInputConfig\x12a\n\ngcs_source\x18\x01 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.schema.TimeSeriesDatasetMetadata.GcsSourceH\x00\x12k\n\x0fbigquery_source\x18\x02 \x01(\x0b2P.google.cloud.aiplatform.v1beta1.schema.TimeSeriesDatasetMetadata.BigQuerySourceH\x00B\x08\n\x06source\x1a\x18\n\tGcsSource\x12\x0b\n\x03uri\x18\x01 \x03(\t\x1a\x1d\n\x0eBigQuerySource\x12\x0b\n\x03uri\x18\x01 \x01(\tB\x87\x02\n*com.google.cloud.aiplatform.v1beta1.schemaB\x14DatasetMetadataProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schemab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.dataset_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.aiplatform.v1beta1.schemaB\x14DatasetMetadataProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schema'
    _globals['_IMAGEDATASETMETADATA']._serialized_start = 105
    _globals['_IMAGEDATASETMETADATA']._serialized_end = 177
    _globals['_TEXTDATASETMETADATA']._serialized_start = 179
    _globals['_TEXTDATASETMETADATA']._serialized_end = 250
    _globals['_VIDEODATASETMETADATA']._serialized_start = 252
    _globals['_VIDEODATASETMETADATA']._serialized_end = 324
    _globals['_TABLESDATASETMETADATA']._serialized_start = 327
    _globals['_TABLESDATASETMETADATA']._serialized_end = 730
    _globals['_TABLESDATASETMETADATA_INPUTCONFIG']._serialized_start = 450
    _globals['_TABLESDATASETMETADATA_INPUTCONFIG']._serialized_end = 673
    _globals['_TABLESDATASETMETADATA_GCSSOURCE']._serialized_start = 675
    _globals['_TABLESDATASETMETADATA_GCSSOURCE']._serialized_end = 699
    _globals['_TABLESDATASETMETADATA_BIGQUERYSOURCE']._serialized_start = 701
    _globals['_TABLESDATASETMETADATA_BIGQUERYSOURCE']._serialized_end = 730
    _globals['_TIMESERIESDATASETMETADATA']._serialized_start = 733
    _globals['_TIMESERIESDATASETMETADATA']._serialized_end = 1212
    _globals['_TIMESERIESDATASETMETADATA_INPUTCONFIG']._serialized_start = 924
    _globals['_TIMESERIESDATASETMETADATA_INPUTCONFIG']._serialized_end = 1155
    _globals['_TIMESERIESDATASETMETADATA_GCSSOURCE']._serialized_start = 675
    _globals['_TIMESERIESDATASETMETADATA_GCSSOURCE']._serialized_end = 699
    _globals['_TIMESERIESDATASETMETADATA_BIGQUERYSOURCE']._serialized_start = 701
    _globals['_TIMESERIESDATASETMETADATA_BIGQUERYSOURCE']._serialized_end = 730