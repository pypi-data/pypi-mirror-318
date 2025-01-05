"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2beta/export_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/retail/v2beta/export_config.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xe8\x02\n\x0cOutputConfig\x12R\n\x0fgcs_destination\x18\x01 \x01(\x0b27.google.cloud.retail.v2beta.OutputConfig.GcsDestinationH\x00\x12\\\n\x14bigquery_destination\x18\x02 \x01(\x0b2<.google.cloud.retail.v2beta.OutputConfig.BigQueryDestinationH\x00\x1a0\n\x0eGcsDestination\x12\x1e\n\x11output_uri_prefix\x18\x01 \x01(\tB\x03\xe0A\x02\x1ae\n\x13BigQueryDestination\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0ftable_id_prefix\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\ntable_type\x18\x03 \x01(\tB\x03\xe0A\x02B\r\n\x0bdestination"9\n\x12ExportErrorsConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\xa3\x01\n\x15ExportProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12D\n\routput_config\x18\x02 \x01(\x0b2(.google.cloud.retail.v2beta.OutputConfigB\x03\xe0A\x02\x12\x0e\n\x06filter\x18\x03 \x01(\t"\xa6\x01\n\x17ExportUserEventsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12D\n\routput_config\x18\x02 \x01(\x0b2(.google.cloud.retail.v2beta.OutputConfigB\x03\xe0A\x02\x12\x0e\n\x06filter\x18\x03 \x01(\t"\x8b\x01\n\x1dExportAnalyticsMetricsRequest\x12\x14\n\x07catalog\x18\x01 \x01(\tB\x03\xe0A\x02\x12D\n\routput_config\x18\x02 \x01(\x0b2(.google.cloud.retail.v2beta.OutputConfigB\x03\xe0A\x02\x12\x0e\n\x06filter\x18\x03 \x01(\t"r\n\x0eExportMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xcb\x01\n\x16ExportProductsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12E\n\rerrors_config\x18\x02 \x01(\x0b2..google.cloud.retail.v2beta.ExportErrorsConfig\x12?\n\routput_result\x18\x03 \x01(\x0b2(.google.cloud.retail.v2beta.OutputResult"\xcd\x01\n\x18ExportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12E\n\rerrors_config\x18\x02 \x01(\x0b2..google.cloud.retail.v2beta.ExportErrorsConfig\x12?\n\routput_result\x18\x03 \x01(\x0b2(.google.cloud.retail.v2beta.OutputResult"\xd3\x01\n\x1eExportAnalyticsMetricsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12E\n\rerrors_config\x18\x02 \x01(\x0b2..google.cloud.retail.v2beta.ExportErrorsConfig\x12?\n\routput_result\x18\x03 \x01(\x0b2(.google.cloud.retail.v2beta.OutputResult"\x9a\x01\n\x0cOutputResult\x12I\n\x0fbigquery_result\x18\x01 \x03(\x0b20.google.cloud.retail.v2beta.BigQueryOutputResult\x12?\n\ngcs_result\x18\x02 \x03(\x0b2+.google.cloud.retail.v2beta.GcsOutputResult"<\n\x14BigQueryOutputResult\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x10\n\x08table_id\x18\x02 \x01(\t"%\n\x0fGcsOutputResult\x12\x12\n\noutput_uri\x18\x01 \x01(\tB\xd0\x01\n\x1ecom.google.cloud.retail.v2betaB\x11ExportConfigProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.export_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x11ExportConfigProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_OUTPUTCONFIG_GCSDESTINATION'].fields_by_name['output_uri_prefix']._loaded_options = None
    _globals['_OUTPUTCONFIG_GCSDESTINATION'].fields_by_name['output_uri_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_id_prefix']._loaded_options = None
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_id_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_type']._loaded_options = None
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION'].fields_by_name['table_type']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_EXPORTPRODUCTSREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTPRODUCTSREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_EXPORTUSEREVENTSREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTUSEREVENTSREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTANALYTICSMETRICSREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG']._serialized_start = 197
    _globals['_OUTPUTCONFIG']._serialized_end = 557
    _globals['_OUTPUTCONFIG_GCSDESTINATION']._serialized_start = 391
    _globals['_OUTPUTCONFIG_GCSDESTINATION']._serialized_end = 439
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION']._serialized_start = 441
    _globals['_OUTPUTCONFIG_BIGQUERYDESTINATION']._serialized_end = 542
    _globals['_EXPORTERRORSCONFIG']._serialized_start = 559
    _globals['_EXPORTERRORSCONFIG']._serialized_end = 616
    _globals['_EXPORTPRODUCTSREQUEST']._serialized_start = 619
    _globals['_EXPORTPRODUCTSREQUEST']._serialized_end = 782
    _globals['_EXPORTUSEREVENTSREQUEST']._serialized_start = 785
    _globals['_EXPORTUSEREVENTSREQUEST']._serialized_end = 951
    _globals['_EXPORTANALYTICSMETRICSREQUEST']._serialized_start = 954
    _globals['_EXPORTANALYTICSMETRICSREQUEST']._serialized_end = 1093
    _globals['_EXPORTMETADATA']._serialized_start = 1095
    _globals['_EXPORTMETADATA']._serialized_end = 1209
    _globals['_EXPORTPRODUCTSRESPONSE']._serialized_start = 1212
    _globals['_EXPORTPRODUCTSRESPONSE']._serialized_end = 1415
    _globals['_EXPORTUSEREVENTSRESPONSE']._serialized_start = 1418
    _globals['_EXPORTUSEREVENTSRESPONSE']._serialized_end = 1623
    _globals['_EXPORTANALYTICSMETRICSRESPONSE']._serialized_start = 1626
    _globals['_EXPORTANALYTICSMETRICSRESPONSE']._serialized_end = 1837
    _globals['_OUTPUTRESULT']._serialized_start = 1840
    _globals['_OUTPUTRESULT']._serialized_end = 1994
    _globals['_BIGQUERYOUTPUTRESULT']._serialized_start = 1996
    _globals['_BIGQUERYOUTPUTRESULT']._serialized_end = 2056
    _globals['_GCSOUTPUTRESULT']._serialized_start = 2058
    _globals['_GCSOUTPUTRESULT']._serialized_end = 2095