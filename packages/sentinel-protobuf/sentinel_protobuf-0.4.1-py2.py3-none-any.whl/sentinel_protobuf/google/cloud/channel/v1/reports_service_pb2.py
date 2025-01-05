"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/reports_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.channel.v1 import operations_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_operations__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from .....google.type import decimal_pb2 as google_dot_type_dot_decimal__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/channel/v1/reports_service.proto\x12\x17google.cloud.channel.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/channel/v1/operations.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto\x1a\x1agoogle/type/datetime.proto\x1a\x19google/type/decimal.proto\x1a\x17google/type/money.proto"\xc1\x01\n\x13RunReportJobRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"cloudchannel.googleapis.com/Report\x12;\n\ndate_range\x18\x02 \x01(\x0b2".google.cloud.channel.v1.DateRangeB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01:\x02\x18\x01"\x9b\x01\n\x14RunReportJobResponse\x126\n\nreport_job\x18\x01 \x01(\x0b2".google.cloud.channel.v1.ReportJob\x12G\n\x0freport_metadata\x18\x02 \x01(\x0b2..google.cloud.channel.v1.ReportResultsMetadata:\x02\x18\x01"\xb0\x01\n\x19FetchReportResultsRequest\x12A\n\nreport_job\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%cloudchannel.googleapis.com/ReportJob\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0epartition_keys\x18\x04 \x03(\tB\x03\xe0A\x01:\x02\x18\x01"\xae\x01\n\x1aFetchReportResultsResponse\x12G\n\x0freport_metadata\x18\x01 \x01(\x0b2..google.cloud.channel.v1.ReportResultsMetadata\x12*\n\x04rows\x18\x02 \x03(\x0b2\x1c.google.cloud.channel.v1.Row\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t:\x02\x18\x01"z\n\x12ListReportsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01:\x02\x18\x01"d\n\x13ListReportsResponse\x120\n\x07reports\x18\x01 \x03(\x0b2\x1f.google.cloud.channel.v1.Report\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t:\x02\x18\x01"\xb6\x01\n\tReportJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12<\n\rreport_status\x18\x02 \x01(\x0b2%.google.cloud.channel.v1.ReportStatus:X\x18\x01\xeaAS\n%cloudchannel.googleapis.com/ReportJob\x12*accounts/{account}/reportJobs/{report_job}"\xd9\x01\n\x15ReportResultsMetadata\x12/\n\x06report\x18\x01 \x01(\x0b2\x1f.google.cloud.channel.v1.Report\x12\x11\n\trow_count\x18\x02 \x01(\x03\x126\n\ndate_range\x18\x03 \x01(\x0b2".google.cloud.channel.v1.DateRange\x12@\n\x14preceding_date_range\x18\x04 \x01(\x0b2".google.cloud.channel.v1.DateRange:\x02\x18\x01"\xdf\x01\n\x06Column\x12\x11\n\tcolumn_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12;\n\tdata_type\x18\x03 \x01(\x0e2(.google.cloud.channel.v1.Column.DataType"k\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03INT\x10\x02\x12\x0b\n\x07DECIMAL\x10\x03\x12\t\n\x05MONEY\x10\x04\x12\x08\n\x04DATE\x10\x05\x12\r\n\tDATE_TIME\x10\x06:\x02\x18\x01"\xd5\x01\n\tDateRange\x124\n\x15usage_start_date_time\x18\x01 \x01(\x0b2\x15.google.type.DateTime\x122\n\x13usage_end_date_time\x18\x02 \x01(\x0b2\x15.google.type.DateTime\x12-\n\x12invoice_start_date\x18\x03 \x01(\x0b2\x11.google.type.Date\x12+\n\x10invoice_end_date\x18\x04 \x01(\x0b2\x11.google.type.Date:\x02\x18\x01"V\n\x03Row\x124\n\x06values\x18\x01 \x03(\x0b2$.google.cloud.channel.v1.ReportValue\x12\x15\n\rpartition_key\x18\x02 \x01(\t:\x02\x18\x01"\xfc\x01\n\x0bReportValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12-\n\rdecimal_value\x18\x03 \x01(\x0b2\x14.google.type.DecimalH\x00\x12)\n\x0bmoney_value\x18\x04 \x01(\x0b2\x12.google.type.MoneyH\x00\x12\'\n\ndate_value\x18\x05 \x01(\x0b2\x11.google.type.DateH\x00\x120\n\x0fdate_time_value\x18\x06 \x01(\x0b2\x15.google.type.DateTimeH\x00:\x02\x18\x01B\x07\n\x05value"\x81\x02\n\x0cReportStatus\x12:\n\x05state\x18\x01 \x01(\x0e2+.google.cloud.channel.v1.ReportStatus.State\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x0b\n\x07WRITING\x10\x02\x12\r\n\tAVAILABLE\x10\x03\x12\n\n\x06FAILED\x10\x04:\x02\x18\x01"\xc8\x01\n\x06Report\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x120\n\x07columns\x18\x03 \x03(\x0b2\x1f.google.cloud.channel.v1.Column\x12\x13\n\x0bdescription\x18\x04 \x01(\t:N\x18\x01\xeaAI\n"cloudchannel.googleapis.com/Report\x12#accounts/{account}/reports/{report}2\xb2\x05\n\x1aCloudChannelReportsService\x12\xba\x01\n\x0cRunReportJob\x12,.google.cloud.channel.v1.RunReportJobRequest\x1a\x1d.google.longrunning.Operation"]\x88\x02\x01\xcaA)\n\x14RunReportJobResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02("#/v1/{name=accounts/*/reports/*}:run:\x01*\x12\xd5\x01\n\x12FetchReportResults\x122.google.cloud.channel.v1.FetchReportResultsRequest\x1a3.google.cloud.channel.v1.FetchReportResultsResponse"V\x88\x02\x01\xdaA\nreport_job\x82\xd3\xe4\x93\x02@";/v1/{report_job=accounts/*/reportJobs/*}:fetchReportResults:\x01*\x12\x9d\x01\n\x0bListReports\x12+.google.cloud.channel.v1.ListReportsRequest\x1a,.google.cloud.channel.v1.ListReportsResponse"3\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=accounts/*}/reports\x1a_\x88\x02\x01\xcaA\x1bcloudchannel.googleapis.com\xd2A;https://www.googleapis.com/auth/apps.reports.usage.readonlyBk\n\x1bcom.google.cloud.channel.v1B\x13ReportsServiceProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.reports_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x13ReportsServiceProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"cloudchannel.googleapis.com/Report'
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['date_range']._loaded_options = None
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['date_range']._serialized_options = b'\xe0A\x01'
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_RUNREPORTJOBREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_RUNREPORTJOBREQUEST']._loaded_options = None
    _globals['_RUNREPORTJOBREQUEST']._serialized_options = b'\x18\x01'
    _globals['_RUNREPORTJOBRESPONSE']._loaded_options = None
    _globals['_RUNREPORTJOBRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['report_job']._loaded_options = None
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['report_job']._serialized_options = b"\xe0A\x02\xfaA'\n%cloudchannel.googleapis.com/ReportJob"
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['partition_keys']._loaded_options = None
    _globals['_FETCHREPORTRESULTSREQUEST'].fields_by_name['partition_keys']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHREPORTRESULTSREQUEST']._loaded_options = None
    _globals['_FETCHREPORTRESULTSREQUEST']._serialized_options = b'\x18\x01'
    _globals['_FETCHREPORTRESULTSRESPONSE']._loaded_options = None
    _globals['_FETCHREPORTRESULTSRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST']._loaded_options = None
    _globals['_LISTREPORTSREQUEST']._serialized_options = b'\x18\x01'
    _globals['_LISTREPORTSRESPONSE']._loaded_options = None
    _globals['_LISTREPORTSRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_REPORTJOB'].fields_by_name['name']._loaded_options = None
    _globals['_REPORTJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTJOB']._loaded_options = None
    _globals['_REPORTJOB']._serialized_options = b'\x18\x01\xeaAS\n%cloudchannel.googleapis.com/ReportJob\x12*accounts/{account}/reportJobs/{report_job}'
    _globals['_REPORTRESULTSMETADATA']._loaded_options = None
    _globals['_REPORTRESULTSMETADATA']._serialized_options = b'\x18\x01'
    _globals['_COLUMN']._loaded_options = None
    _globals['_COLUMN']._serialized_options = b'\x18\x01'
    _globals['_DATERANGE']._loaded_options = None
    _globals['_DATERANGE']._serialized_options = b'\x18\x01'
    _globals['_ROW']._loaded_options = None
    _globals['_ROW']._serialized_options = b'\x18\x01'
    _globals['_REPORTVALUE']._loaded_options = None
    _globals['_REPORTVALUE']._serialized_options = b'\x18\x01'
    _globals['_REPORTSTATUS']._loaded_options = None
    _globals['_REPORTSTATUS']._serialized_options = b'\x18\x01'
    _globals['_REPORT'].fields_by_name['name']._loaded_options = None
    _globals['_REPORT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REPORT']._loaded_options = None
    _globals['_REPORT']._serialized_options = b'\x18\x01\xeaAI\n"cloudchannel.googleapis.com/Report\x12#accounts/{account}/reports/{report}'
    _globals['_CLOUDCHANNELREPORTSSERVICE']._loaded_options = None
    _globals['_CLOUDCHANNELREPORTSSERVICE']._serialized_options = b'\x88\x02\x01\xcaA\x1bcloudchannel.googleapis.com\xd2A;https://www.googleapis.com/auth/apps.reports.usage.readonly'
    _globals['_CLOUDCHANNELREPORTSSERVICE'].methods_by_name['RunReportJob']._loaded_options = None
    _globals['_CLOUDCHANNELREPORTSSERVICE'].methods_by_name['RunReportJob']._serialized_options = b'\x88\x02\x01\xcaA)\n\x14RunReportJobResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02("#/v1/{name=accounts/*/reports/*}:run:\x01*'
    _globals['_CLOUDCHANNELREPORTSSERVICE'].methods_by_name['FetchReportResults']._loaded_options = None
    _globals['_CLOUDCHANNELREPORTSSERVICE'].methods_by_name['FetchReportResults']._serialized_options = b'\x88\x02\x01\xdaA\nreport_job\x82\xd3\xe4\x93\x02@";/v1/{report_job=accounts/*/reportJobs/*}:fetchReportResults:\x01*'
    _globals['_CLOUDCHANNELREPORTSSERVICE'].methods_by_name['ListReports']._loaded_options = None
    _globals['_CLOUDCHANNELREPORTSSERVICE'].methods_by_name['ListReports']._serialized_options = b'\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=accounts/*}/reports'
    _globals['_RUNREPORTJOBREQUEST']._serialized_start = 406
    _globals['_RUNREPORTJOBREQUEST']._serialized_end = 599
    _globals['_RUNREPORTJOBRESPONSE']._serialized_start = 602
    _globals['_RUNREPORTJOBRESPONSE']._serialized_end = 757
    _globals['_FETCHREPORTRESULTSREQUEST']._serialized_start = 760
    _globals['_FETCHREPORTRESULTSREQUEST']._serialized_end = 936
    _globals['_FETCHREPORTRESULTSRESPONSE']._serialized_start = 939
    _globals['_FETCHREPORTRESULTSRESPONSE']._serialized_end = 1113
    _globals['_LISTREPORTSREQUEST']._serialized_start = 1115
    _globals['_LISTREPORTSREQUEST']._serialized_end = 1237
    _globals['_LISTREPORTSRESPONSE']._serialized_start = 1239
    _globals['_LISTREPORTSRESPONSE']._serialized_end = 1339
    _globals['_REPORTJOB']._serialized_start = 1342
    _globals['_REPORTJOB']._serialized_end = 1524
    _globals['_REPORTRESULTSMETADATA']._serialized_start = 1527
    _globals['_REPORTRESULTSMETADATA']._serialized_end = 1744
    _globals['_COLUMN']._serialized_start = 1747
    _globals['_COLUMN']._serialized_end = 1970
    _globals['_COLUMN_DATATYPE']._serialized_start = 1859
    _globals['_COLUMN_DATATYPE']._serialized_end = 1966
    _globals['_DATERANGE']._serialized_start = 1973
    _globals['_DATERANGE']._serialized_end = 2186
    _globals['_ROW']._serialized_start = 2188
    _globals['_ROW']._serialized_end = 2274
    _globals['_REPORTVALUE']._serialized_start = 2277
    _globals['_REPORTVALUE']._serialized_end = 2529
    _globals['_REPORTSTATUS']._serialized_start = 2532
    _globals['_REPORTSTATUS']._serialized_end = 2789
    _globals['_REPORTSTATUS_STATE']._serialized_start = 2702
    _globals['_REPORTSTATUS_STATE']._serialized_end = 2785
    _globals['_REPORT']._serialized_start = 2792
    _globals['_REPORT']._serialized_end = 2992
    _globals['_CLOUDCHANNELREPORTSSERVICE']._serialized_start = 2995
    _globals['_CLOUDCHANNELREPORTSSERVICE']._serialized_end = 3685