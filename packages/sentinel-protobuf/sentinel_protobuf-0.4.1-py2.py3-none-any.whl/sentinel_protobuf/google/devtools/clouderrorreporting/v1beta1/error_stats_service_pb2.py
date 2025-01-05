"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/clouderrorreporting/v1beta1/error_stats_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.clouderrorreporting.v1beta1 import common_pb2 as google_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/devtools/clouderrorreporting/v1beta1/error_stats_service.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/devtools/clouderrorreporting/v1beta1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x05\n\x15ListGroupStatsRequest\x12I\n\x0cproject_name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x15\n\x08group_id\x18\x02 \x03(\tB\x03\xe0A\x01\x12^\n\x0eservice_filter\x18\x03 \x01(\x0b2A.google.devtools.clouderrorreporting.v1beta1.ServiceContextFilterB\x03\xe0A\x01\x12T\n\ntime_range\x18\x05 \x01(\x0b2;.google.devtools.clouderrorreporting.v1beta1.QueryTimeRangeB\x03\xe0A\x01\x12<\n\x14timed_count_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12X\n\talignment\x18\x07 \x01(\x0e2@.google.devtools.clouderrorreporting.v1beta1.TimedCountAlignmentB\x03\xe0A\x01\x127\n\x0ealignment_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12P\n\x05order\x18\t \x01(\x0e2<.google.devtools.clouderrorreporting.v1beta1.ErrorGroupOrderB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x0b \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x0c \x01(\tB\x03\xe0A\x01"\xc0\x01\n\x16ListGroupStatsResponse\x12W\n\x11error_group_stats\x18\x01 \x03(\x0b2<.google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x124\n\x10time_range_begin\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x86\x04\n\x0fErrorGroupStats\x12F\n\x05group\x18\x01 \x01(\x0b27.google.devtools.clouderrorreporting.v1beta1.ErrorGroup\x12\r\n\x05count\x18\x02 \x01(\x03\x12\x1c\n\x14affected_users_count\x18\x03 \x01(\x03\x12M\n\x0ctimed_counts\x18\x04 \x03(\x0b27.google.devtools.clouderrorreporting.v1beta1.TimedCount\x123\n\x0ffirst_seen_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x0elast_seen_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12V\n\x11affected_services\x18\x07 \x03(\x0b2;.google.devtools.clouderrorreporting.v1beta1.ServiceContext\x12\x1d\n\x15num_affected_services\x18\x08 \x01(\x05\x12O\n\x0erepresentative\x18\t \x01(\x0b27.google.devtools.clouderrorreporting.v1beta1.ErrorEvent"y\n\nTimedCount\x12\r\n\x05count\x18\x01 \x01(\x03\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xdc\x02\n\x11ListEventsRequest\x12I\n\x0cproject_name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x15\n\x08group_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12^\n\x0eservice_filter\x18\x03 \x01(\x0b2A.google.devtools.clouderrorreporting.v1beta1.ServiceContextFilterB\x03\xe0A\x01\x12T\n\ntime_range\x18\x04 \x01(\x0b2;.google.devtools.clouderrorreporting.v1beta1.QueryTimeRangeB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x06 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x07 \x01(\tB\x03\xe0A\x01"\xb2\x01\n\x12ListEventsResponse\x12M\n\x0cerror_events\x18\x01 \x03(\x0b27.google.devtools.clouderrorreporting.v1beta1.ErrorEvent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x124\n\x10time_range_begin\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xe7\x01\n\x0eQueryTimeRange\x12R\n\x06period\x18\x01 \x01(\x0e2B.google.devtools.clouderrorreporting.v1beta1.QueryTimeRange.Period"\x80\x01\n\x06Period\x12\x16\n\x12PERIOD_UNSPECIFIED\x10\x00\x12\x11\n\rPERIOD_1_HOUR\x10\x01\x12\x12\n\x0ePERIOD_6_HOURS\x10\x02\x12\x10\n\x0cPERIOD_1_DAY\x10\x03\x12\x11\n\rPERIOD_1_WEEK\x10\x04\x12\x12\n\x0ePERIOD_30_DAYS\x10\x05"^\n\x14ServiceContextFilter\x12\x14\n\x07service\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07version\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rresource_type\x18\x04 \x01(\tB\x03\xe0A\x01"`\n\x13DeleteEventsRequest\x12I\n\x0cproject_name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"\x16\n\x14DeleteEventsResponse*u\n\x13TimedCountAlignment\x12%\n!ERROR_COUNT_ALIGNMENT_UNSPECIFIED\x10\x00\x12\x1b\n\x17ALIGNMENT_EQUAL_ROUNDED\x10\x01\x12\x1a\n\x16ALIGNMENT_EQUAL_AT_END\x10\x02*}\n\x0fErrorGroupOrder\x12\x1b\n\x17GROUP_ORDER_UNSPECIFIED\x10\x00\x12\x0e\n\nCOUNT_DESC\x10\x01\x12\x12\n\x0eLAST_SEEN_DESC\x10\x02\x12\x10\n\x0cCREATED_DESC\x10\x03\x12\x17\n\x13AFFECTED_USERS_DESC\x10\x042\xbc\x07\n\x11ErrorStatsService\x12\xa8\x02\n\x0eListGroupStats\x12B.google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest\x1aC.google.devtools.clouderrorreporting.v1beta1.ListGroupStatsResponse"\x8c\x01\xdaA\x17project_name,time_range\x82\xd3\xe4\x93\x02l\x12-/v1beta1/{project_name=projects/*}/groupStatsZ;\x129/v1beta1/{project_name=projects/*/locations/*}/groupStats\x12\x92\x02\n\nListEvents\x12>.google.devtools.clouderrorreporting.v1beta1.ListEventsRequest\x1a?.google.devtools.clouderrorreporting.v1beta1.ListEventsResponse"\x82\x01\xdaA\x15project_name,group_id\x82\xd3\xe4\x93\x02d\x12)/v1beta1/{project_name=projects/*}/eventsZ7\x125/v1beta1/{project_name=projects/*/locations/*}/events\x12\x8e\x02\n\x0cDeleteEvents\x12@.google.devtools.clouderrorreporting.v1beta1.DeleteEventsRequest\x1aA.google.devtools.clouderrorreporting.v1beta1.DeleteEventsResponse"y\xdaA\x0cproject_name\x82\xd3\xe4\x93\x02d*)/v1beta1/{project_name=projects/*}/eventsZ7*5/v1beta1/{project_name=projects/*/locations/*}/events\x1aV\xcaA"clouderrorreporting.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x94\x02\n/com.google.devtools.clouderrorreporting.v1beta1B\x16ErrorStatsServiceProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.devtools.clouderrorreporting.v1beta1B\x16ErrorStatsServiceProtoP\x01ZOcloud.google.com/go/errorreporting/apiv1beta1/errorreportingpb;errorreportingpb\xf8\x01\x01\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1\xca\x02#Google\\Cloud\\ErrorReporting\\V1beta1\xea\x02&Google::Cloud::ErrorReporting::V1beta1'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['project_name']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['project_name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['group_id']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['group_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['service_filter']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['service_filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['time_range']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['time_range']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['timed_count_duration']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['timed_count_duration']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['alignment']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['alignment']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['alignment_time']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['alignment_time']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['order']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['order']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTGROUPSTATSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['project_name']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['project_name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['group_id']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['group_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['service_filter']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['service_filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['time_range']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['time_range']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICECONTEXTFILTER'].fields_by_name['service']._loaded_options = None
    _globals['_SERVICECONTEXTFILTER'].fields_by_name['service']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICECONTEXTFILTER'].fields_by_name['version']._loaded_options = None
    _globals['_SERVICECONTEXTFILTER'].fields_by_name['version']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICECONTEXTFILTER'].fields_by_name['resource_type']._loaded_options = None
    _globals['_SERVICECONTEXTFILTER'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEEVENTSREQUEST'].fields_by_name['project_name']._loaded_options = None
    _globals['_DELETEEVENTSREQUEST'].fields_by_name['project_name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_ERRORSTATSSERVICE']._loaded_options = None
    _globals['_ERRORSTATSSERVICE']._serialized_options = b'\xcaA"clouderrorreporting.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ERRORSTATSSERVICE'].methods_by_name['ListGroupStats']._loaded_options = None
    _globals['_ERRORSTATSSERVICE'].methods_by_name['ListGroupStats']._serialized_options = b'\xdaA\x17project_name,time_range\x82\xd3\xe4\x93\x02l\x12-/v1beta1/{project_name=projects/*}/groupStatsZ;\x129/v1beta1/{project_name=projects/*/locations/*}/groupStats'
    _globals['_ERRORSTATSSERVICE'].methods_by_name['ListEvents']._loaded_options = None
    _globals['_ERRORSTATSSERVICE'].methods_by_name['ListEvents']._serialized_options = b'\xdaA\x15project_name,group_id\x82\xd3\xe4\x93\x02d\x12)/v1beta1/{project_name=projects/*}/eventsZ7\x125/v1beta1/{project_name=projects/*/locations/*}/events'
    _globals['_ERRORSTATSSERVICE'].methods_by_name['DeleteEvents']._loaded_options = None
    _globals['_ERRORSTATSSERVICE'].methods_by_name['DeleteEvents']._serialized_options = b'\xdaA\x0cproject_name\x82\xd3\xe4\x93\x02d*)/v1beta1/{project_name=projects/*}/eventsZ7*5/v1beta1/{project_name=projects/*/locations/*}/events'
    _globals['_TIMEDCOUNTALIGNMENT']._serialized_start = 2825
    _globals['_TIMEDCOUNTALIGNMENT']._serialized_end = 2942
    _globals['_ERRORGROUPORDER']._serialized_start = 2944
    _globals['_ERRORGROUPORDER']._serialized_end = 3069
    _globals['_LISTGROUPSTATSREQUEST']._serialized_start = 357
    _globals['_LISTGROUPSTATSREQUEST']._serialized_end = 1000
    _globals['_LISTGROUPSTATSRESPONSE']._serialized_start = 1003
    _globals['_LISTGROUPSTATSRESPONSE']._serialized_end = 1195
    _globals['_ERRORGROUPSTATS']._serialized_start = 1198
    _globals['_ERRORGROUPSTATS']._serialized_end = 1716
    _globals['_TIMEDCOUNT']._serialized_start = 1718
    _globals['_TIMEDCOUNT']._serialized_end = 1839
    _globals['_LISTEVENTSREQUEST']._serialized_start = 1842
    _globals['_LISTEVENTSREQUEST']._serialized_end = 2190
    _globals['_LISTEVENTSRESPONSE']._serialized_start = 2193
    _globals['_LISTEVENTSRESPONSE']._serialized_end = 2371
    _globals['_QUERYTIMERANGE']._serialized_start = 2374
    _globals['_QUERYTIMERANGE']._serialized_end = 2605
    _globals['_QUERYTIMERANGE_PERIOD']._serialized_start = 2477
    _globals['_QUERYTIMERANGE_PERIOD']._serialized_end = 2605
    _globals['_SERVICECONTEXTFILTER']._serialized_start = 2607
    _globals['_SERVICECONTEXTFILTER']._serialized_end = 2701
    _globals['_DELETEEVENTSREQUEST']._serialized_start = 2703
    _globals['_DELETEEVENTSREQUEST']._serialized_end = 2799
    _globals['_DELETEEVENTSRESPONSE']._serialized_start = 2801
    _globals['_DELETEEVENTSRESPONSE']._serialized_end = 2823
    _globals['_ERRORSTATSSERVICE']._serialized_start = 3072
    _globals['_ERRORSTATSSERVICE']._serialized_end = 4028