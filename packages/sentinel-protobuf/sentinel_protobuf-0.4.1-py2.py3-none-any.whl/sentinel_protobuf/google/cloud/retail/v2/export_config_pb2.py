"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2/export_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/retail/v2/export_config.proto\x12\x16google.cloud.retail.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xe0\x02\n\x0cOutputConfig\x12N\n\x0fgcs_destination\x18\x01 \x01(\x0b23.google.cloud.retail.v2.OutputConfig.GcsDestinationH\x00\x12X\n\x14bigquery_destination\x18\x02 \x01(\x0b28.google.cloud.retail.v2.OutputConfig.BigQueryDestinationH\x00\x1a0\n\x0eGcsDestination\x12\x1e\n\x11output_uri_prefix\x18\x01 \x01(\tB\x03\xe0A\x02\x1ae\n\x13BigQueryDestination\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0ftable_id_prefix\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\ntable_type\x18\x03 \x01(\tB\x03\xe0A\x02B\r\n\x0bdestination"9\n\x12ExportErrorsConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\x87\x01\n\x1dExportAnalyticsMetricsRequest\x12\x14\n\x07catalog\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\routput_config\x18\x02 \x01(\x0b2$.google.cloud.retail.v2.OutputConfigB\x03\xe0A\x02\x12\x0e\n\x06filter\x18\x03 \x01(\t"r\n\x0eExportMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xcb\x01\n\x1eExportAnalyticsMetricsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12A\n\rerrors_config\x18\x02 \x01(\x0b2*.google.cloud.retail.v2.ExportErrorsConfig\x12;\n\routput_result\x18\x03 \x01(\x0b2$.google.cloud.retail.v2.OutputResult"\x92\x01\n\x0cOutputResult\x12E\n\x0fbigquery_result\x18\x01 \x03(\x0b2,.google.cloud.retail.v2.BigQueryOutputResult\x12;\n\ngcs_result\x18\x02 \x03(\x0b2\'.google.cloud.retail.v2.GcsOutputResult"<\n\x14BigQueryOutputResult\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x10\n\x08table_id\x18\x02 \x01(\t"%\n\x0fGcsOutputResult\x12\x12\n\noutput_uri\x18\x01 \x01(\tB\xbc\x01\n\x1acom.google.cloud.retail.v2B\x11ExportConfigProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.export_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x11ExportConfigProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_OUTPUTCONFIG_GCSDESTINATION'].fields_by_name['output_uri_prefix']._loaded_options = None
    _globals['_OUTPUTCONFIG_GCSDESTINATION'].fields_by_name['output_uri_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_id_prefix']._loaded_options = None
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_id_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_type']._loaded_options = None
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_type']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG']._serialized_start = 189
    _globals['_OUTPUTCONFIG']._serialized_end = 541
    _globals['_OUTPUTCONFIG_GCSDESTINATION']._serialized_start = 375
    _globals['_OUTPUTCONFIG_GCSDESTINATION']._serialized_end = 423
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION']._serialized_start = 425
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION']._serialized_end = 526
    _globals['_EXPORTERRORSCONFIG']._serialized_start = 543
    _globals['_EXPORTERRORSCONFIG']._serialized_end = 600
    _globals['_EXPORTANALYTICSMETRICSREQUEST']._serialized_start = 603
    _globals['_EXPORTANALYTICSMETRICSREQUEST']._serialized_end = 738
    _globals['_EXPORTMETADATA']._serialized_start = 740
    _globals['_EXPORTMETADATA']._serialized_end = 854
    _globals['_EXPORTANALYTICSMETRICSRESPONSE']._serialized_start = 857
    _globals['_EXPORTANALYTICSMETRICSRESPONSE']._serialized_end = 1060
    _globals['_OUTPUTRESULT']._serialized_start = 1063
    _globals['_OUTPUTRESULT']._serialized_end = 1209
    _globals['_BIGQUERYOUTPUTRESULT']._serialized_start = 1211
    _globals['_BIGQUERYOUTPUTRESULT']._serialized_end = 1271
    _globals['_GCSOUTPUTRESULT']._serialized_start = 1273
    _globals['_GCSOUTPUTRESULT']._serialized_end = 1310