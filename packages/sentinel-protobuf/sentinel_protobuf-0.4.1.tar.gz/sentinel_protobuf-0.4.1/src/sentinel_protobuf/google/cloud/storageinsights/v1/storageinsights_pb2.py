"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/storageinsights/v1/storageinsights.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/storageinsights/v1/storageinsights.proto\x12\x1fgoogle.cloud.storageinsights.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto\x1a\x1agoogle/type/datetime.proto"\xa8\x01\n\x18ListReportConfigsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+storageinsights.googleapis.com/ReportConfig\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x90\x01\n\x19ListReportConfigsResponse\x12E\n\x0ereport_configs\x18\x01 \x03(\x0b2-.google.cloud.storageinsights.v1.ReportConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"[\n\x16GetReportConfigRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+storageinsights.googleapis.com/ReportConfig"\xc4\x01\n\x19CreateReportConfigRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+storageinsights.googleapis.com/ReportConfig\x12I\n\rreport_config\x18\x03 \x01(\x0b2-.google.cloud.storageinsights.v1.ReportConfigB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xb5\x01\n\x19UpdateReportConfigRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12I\n\rreport_config\x18\x02 \x01(\x0b2-.google.cloud.storageinsights.v1.ReportConfigB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x8b\x01\n\x19DeleteReportConfigRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+storageinsights.googleapis.com/ReportConfig\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\xe3\x04\n\x0cReportDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x121\n\rsnapshot_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1a\n\x12report_path_prefix\x18\x08 \x01(\t\x12\x14\n\x0cshards_count\x18\t \x01(\x03\x12"\n\x06status\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x12I\n\x06labels\x18\x05 \x03(\x0b29.google.cloud.storageinsights.v1.ReportDetail.LabelsEntry\x12.\n\x0ftarget_datetime\x18\x06 \x01(\x0b2\x15.google.type.DateTime\x12M\n\x0ereport_metrics\x18\x07 \x01(\x0b25.google.cloud.storageinsights.v1.ReportDetail.Metrics\x1a*\n\x07Metrics\x12\x1f\n\x17processed_records_count\x18\x01 \x01(\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x96\x01\xeaA\x92\x01\n+storageinsights.googleapis.com/ReportDetail\x12cprojects/{project}/locations/{location}/reportConfigs/{report_config}/reportDetails/{report_detail}"\xa8\x01\n\x18ListReportDetailsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+storageinsights.googleapis.com/ReportDetail\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x90\x01\n\x19ListReportDetailsResponse\x12E\n\x0ereport_details\x18\x01 \x03(\x0b2-.google.cloud.storageinsights.v1.ReportDetail\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"[\n\x16GetReportDetailRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+storageinsights.googleapis.com/ReportDetail"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"\xed\x01\n\x10FrequencyOptions\x12N\n\tfrequency\x18\x01 \x01(\x0e2;.google.cloud.storageinsights.v1.FrequencyOptions.Frequency\x12%\n\nstart_date\x18\x02 \x01(\x0b2\x11.google.type.Date\x12#\n\x08end_date\x18\x03 \x01(\x0b2\x11.google.type.Date"=\n\tFrequency\x12\x19\n\x15FREQUENCY_UNSPECIFIED\x10\x00\x12\t\n\x05DAILY\x10\x01\x12\n\n\x06WEEKLY\x10\x02"R\n\nCSVOptions\x12\x18\n\x10record_separator\x18\x01 \x01(\t\x12\x11\n\tdelimiter\x18\x02 \x01(\t\x12\x17\n\x0fheader_required\x18\x03 \x01(\x08"\x10\n\x0eParquetOptions"%\n\x13CloudStorageFilters\x12\x0e\n\x06bucket\x18\x01 \x01(\t"J\n\x1eCloudStorageDestinationOptions\x12\x0e\n\x06bucket\x18\x01 \x01(\t\x12\x18\n\x10destination_path\x18\x02 \x01(\t"\x90\x02\n\x1bObjectMetadataReportOptions\x12\x17\n\x0fmetadata_fields\x18\x01 \x03(\t\x12O\n\x0fstorage_filters\x18\x02 \x01(\x0b24.google.cloud.storageinsights.v1.CloudStorageFiltersH\x00\x12f\n\x1bstorage_destination_options\x18\x03 \x01(\x0b2?.google.cloud.storageinsights.v1.CloudStorageDestinationOptionsH\x01B\x08\n\x06filterB\x15\n\x13destination_options"\xf7\x05\n\x0cReportConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12L\n\x11frequency_options\x18\x05 \x01(\x0b21.google.cloud.storageinsights.v1.FrequencyOptions\x12B\n\x0bcsv_options\x18\x06 \x01(\x0b2+.google.cloud.storageinsights.v1.CSVOptionsH\x00\x12J\n\x0fparquet_options\x18\x07 \x01(\x0b2/.google.cloud.storageinsights.v1.ParquetOptionsH\x00\x12f\n\x1eobject_metadata_report_options\x18\x08 \x01(\x0b2<.google.cloud.storageinsights.v1.ObjectMetadataReportOptionsH\x01\x12I\n\x06labels\x18\n \x03(\x0b29.google.cloud.storageinsights.v1.ReportConfig.LabelsEntry\x12\x14\n\x0cdisplay_name\x18\x0b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:w\xeaAt\n+storageinsights.googleapis.com/ReportConfig\x12Eprojects/{project}/locations/{location}/reportConfigs/{report_config}B\x0f\n\rreport_formatB\r\n\x0breport_kind2\xa9\x0c\n\x0fStorageInsights\x12\xce\x01\n\x11ListReportConfigs\x129.google.cloud.storageinsights.v1.ListReportConfigsRequest\x1a:.google.cloud.storageinsights.v1.ListReportConfigsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/reportConfigs\x12\xbb\x01\n\x0fGetReportConfig\x127.google.cloud.storageinsights.v1.GetReportConfigRequest\x1a-.google.cloud.storageinsights.v1.ReportConfig"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/reportConfigs/*}\x12\xe0\x01\n\x12CreateReportConfig\x12:.google.cloud.storageinsights.v1.CreateReportConfigRequest\x1a-.google.cloud.storageinsights.v1.ReportConfig"_\xdaA\x14parent,report_config\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/reportConfigs:\rreport_config\x12\xf3\x01\n\x12UpdateReportConfig\x12:.google.cloud.storageinsights.v1.UpdateReportConfigRequest\x1a-.google.cloud.storageinsights.v1.ReportConfig"r\xdaA\x19report_config,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{report_config.name=projects/*/locations/*/reportConfigs/*}:\rreport_config\x12\xaa\x01\n\x12DeleteReportConfig\x12:.google.cloud.storageinsights.v1.DeleteReportConfigRequest\x1a\x16.google.protobuf.Empty"@\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/reportConfigs/*}\x12\xde\x01\n\x11ListReportDetails\x129.google.cloud.storageinsights.v1.ListReportDetailsRequest\x1a:.google.cloud.storageinsights.v1.ListReportDetailsResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*/reportConfigs/*}/reportDetails\x12\xcb\x01\n\x0fGetReportDetail\x127.google.cloud.storageinsights.v1.GetReportDetailRequest\x1a-.google.cloud.storageinsights.v1.ReportDetail"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/reportConfigs/*/reportDetails/*}\x1aR\xcaA\x1estorageinsights.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe8\x01\n#com.google.cloud.storageinsights.v1B\x07V1ProtoP\x01ZMcloud.google.com/go/storageinsights/apiv1/storageinsightspb;storageinsightspb\xaa\x02\x1fGoogle.Cloud.StorageInsights.V1\xca\x02\x1fGoogle\\Cloud\\StorageInsights\\V1\xea\x02"Google::Cloud::StorageInsights::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.storageinsights.v1.storageinsights_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.storageinsights.v1B\x07V1ProtoP\x01ZMcloud.google.com/go/storageinsights/apiv1/storageinsightspb;storageinsightspb\xaa\x02\x1fGoogle.Cloud.StorageInsights.V1\xca\x02\x1fGoogle\\Cloud\\StorageInsights\\V1\xea\x02"Google::Cloud::StorageInsights::V1'
    _globals['_LISTREPORTCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPORTCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+storageinsights.googleapis.com/ReportConfig'
    _globals['_GETREPORTCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREPORTCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+storageinsights.googleapis.com/ReportConfig'
    _globals['_CREATEREPORTCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREPORTCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+storageinsights.googleapis.com/ReportConfig'
    _globals['_CREATEREPORTCONFIGREQUEST'].fields_by_name['report_config']._loaded_options = None
    _globals['_CREATEREPORTCONFIGREQUEST'].fields_by_name['report_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREPORTCONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEREPORTCONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEREPORTCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREPORTCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREPORTCONFIGREQUEST'].fields_by_name['report_config']._loaded_options = None
    _globals['_UPDATEREPORTCONFIGREQUEST'].fields_by_name['report_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREPORTCONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEREPORTCONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEREPORTCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREPORTCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+storageinsights.googleapis.com/ReportConfig'
    _globals['_DELETEREPORTCONFIGREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEREPORTCONFIGREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEREPORTCONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEREPORTCONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTDETAIL_LABELSENTRY']._loaded_options = None
    _globals['_REPORTDETAIL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_REPORTDETAIL']._loaded_options = None
    _globals['_REPORTDETAIL']._serialized_options = b'\xeaA\x92\x01\n+storageinsights.googleapis.com/ReportDetail\x12cprojects/{project}/locations/{location}/reportConfigs/{report_config}/reportDetails/{report_detail}'
    _globals['_LISTREPORTDETAILSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPORTDETAILSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+storageinsights.googleapis.com/ReportDetail'
    _globals['_GETREPORTDETAILREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREPORTDETAILREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+storageinsights.googleapis.com/ReportDetail'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_REPORTCONFIG_LABELSENTRY']._loaded_options = None
    _globals['_REPORTCONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_REPORTCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_REPORTCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_REPORTCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_REPORTCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_REPORTCONFIG']._loaded_options = None
    _globals['_REPORTCONFIG']._serialized_options = b'\xeaAt\n+storageinsights.googleapis.com/ReportConfig\x12Eprojects/{project}/locations/{location}/reportConfigs/{report_config}'
    _globals['_STORAGEINSIGHTS']._loaded_options = None
    _globals['_STORAGEINSIGHTS']._serialized_options = b'\xcaA\x1estorageinsights.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_STORAGEINSIGHTS'].methods_by_name['ListReportConfigs']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['ListReportConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/reportConfigs'
    _globals['_STORAGEINSIGHTS'].methods_by_name['GetReportConfig']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['GetReportConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/reportConfigs/*}'
    _globals['_STORAGEINSIGHTS'].methods_by_name['CreateReportConfig']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['CreateReportConfig']._serialized_options = b'\xdaA\x14parent,report_config\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/reportConfigs:\rreport_config'
    _globals['_STORAGEINSIGHTS'].methods_by_name['UpdateReportConfig']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['UpdateReportConfig']._serialized_options = b'\xdaA\x19report_config,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{report_config.name=projects/*/locations/*/reportConfigs/*}:\rreport_config'
    _globals['_STORAGEINSIGHTS'].methods_by_name['DeleteReportConfig']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['DeleteReportConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/reportConfigs/*}'
    _globals['_STORAGEINSIGHTS'].methods_by_name['ListReportDetails']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['ListReportDetails']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*/reportConfigs/*}/reportDetails'
    _globals['_STORAGEINSIGHTS'].methods_by_name['GetReportDetail']._loaded_options = None
    _globals['_STORAGEINSIGHTS'].methods_by_name['GetReportDetail']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/reportConfigs/*/reportDetails/*}'
    _globals['_LISTREPORTCONFIGSREQUEST']._serialized_start = 379
    _globals['_LISTREPORTCONFIGSREQUEST']._serialized_end = 547
    _globals['_LISTREPORTCONFIGSRESPONSE']._serialized_start = 550
    _globals['_LISTREPORTCONFIGSRESPONSE']._serialized_end = 694
    _globals['_GETREPORTCONFIGREQUEST']._serialized_start = 696
    _globals['_GETREPORTCONFIGREQUEST']._serialized_end = 787
    _globals['_CREATEREPORTCONFIGREQUEST']._serialized_start = 790
    _globals['_CREATEREPORTCONFIGREQUEST']._serialized_end = 986
    _globals['_UPDATEREPORTCONFIGREQUEST']._serialized_start = 989
    _globals['_UPDATEREPORTCONFIGREQUEST']._serialized_end = 1170
    _globals['_DELETEREPORTCONFIGREQUEST']._serialized_start = 1173
    _globals['_DELETEREPORTCONFIGREQUEST']._serialized_end = 1312
    _globals['_REPORTDETAIL']._serialized_start = 1315
    _globals['_REPORTDETAIL']._serialized_end = 1926
    _globals['_REPORTDETAIL_METRICS']._serialized_start = 1684
    _globals['_REPORTDETAIL_METRICS']._serialized_end = 1726
    _globals['_REPORTDETAIL_LABELSENTRY']._serialized_start = 1728
    _globals['_REPORTDETAIL_LABELSENTRY']._serialized_end = 1773
    _globals['_LISTREPORTDETAILSREQUEST']._serialized_start = 1929
    _globals['_LISTREPORTDETAILSREQUEST']._serialized_end = 2097
    _globals['_LISTREPORTDETAILSRESPONSE']._serialized_start = 2100
    _globals['_LISTREPORTDETAILSRESPONSE']._serialized_end = 2244
    _globals['_GETREPORTDETAILREQUEST']._serialized_start = 2246
    _globals['_GETREPORTDETAILREQUEST']._serialized_end = 2337
    _globals['_OPERATIONMETADATA']._serialized_start = 2340
    _globals['_OPERATIONMETADATA']._serialized_end = 2596
    _globals['_FREQUENCYOPTIONS']._serialized_start = 2599
    _globals['_FREQUENCYOPTIONS']._serialized_end = 2836
    _globals['_FREQUENCYOPTIONS_FREQUENCY']._serialized_start = 2775
    _globals['_FREQUENCYOPTIONS_FREQUENCY']._serialized_end = 2836
    _globals['_CSVOPTIONS']._serialized_start = 2838
    _globals['_CSVOPTIONS']._serialized_end = 2920
    _globals['_PARQUETOPTIONS']._serialized_start = 2922
    _globals['_PARQUETOPTIONS']._serialized_end = 2938
    _globals['_CLOUDSTORAGEFILTERS']._serialized_start = 2940
    _globals['_CLOUDSTORAGEFILTERS']._serialized_end = 2977
    _globals['_CLOUDSTORAGEDESTINATIONOPTIONS']._serialized_start = 2979
    _globals['_CLOUDSTORAGEDESTINATIONOPTIONS']._serialized_end = 3053
    _globals['_OBJECTMETADATAREPORTOPTIONS']._serialized_start = 3056
    _globals['_OBJECTMETADATAREPORTOPTIONS']._serialized_end = 3328
    _globals['_REPORTCONFIG']._serialized_start = 3331
    _globals['_REPORTCONFIG']._serialized_end = 4090
    _globals['_REPORTCONFIG_LABELSENTRY']._serialized_start = 1728
    _globals['_REPORTCONFIG_LABELSENTRY']._serialized_end = 1773
    _globals['_STORAGEINSIGHTS']._serialized_start = 4093
    _globals['_STORAGEINSIGHTS']._serialized_end = 5670