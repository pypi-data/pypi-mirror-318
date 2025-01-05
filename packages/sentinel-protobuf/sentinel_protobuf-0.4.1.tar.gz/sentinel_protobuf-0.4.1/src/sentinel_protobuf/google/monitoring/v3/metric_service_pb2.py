"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/metric_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from ....google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
from ....google.monitoring.v3 import metric_pb2 as google_dot_monitoring_dot_v3_dot_metric__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/monitoring/v3/metric_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/api/metric.proto\x1a#google/api/monitored_resource.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/common.proto\x1a!google/monitoring/v3/metric.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto"\xad\x01\n\'ListMonitoredResourceDescriptorsRequest\x12K\n\x04name\x18\x05 \x01(\tB=\xe0A\x02\xfaA7\x125monitoring.googleapis.com/MonitoredResourceDescriptor\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"\x8a\x01\n(ListMonitoredResourceDescriptorsResponse\x12E\n\x14resource_descriptors\x18\x01 \x03(\x0b2\'.google.api.MonitoredResourceDescriptor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"t\n%GetMonitoredResourceDescriptorRequest\x12K\n\x04name\x18\x03 \x01(\tB=\xe0A\x02\xfaA7\n5monitoring.googleapis.com/MonitoredResourceDescriptor"\xa6\x01\n\x1cListMetricDescriptorsRequest\x12@\n\x04name\x18\x05 \x01(\tB2\xe0A\x02\xfaA,\x12*monitoring.googleapis.com/MetricDescriptor\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"r\n\x1dListMetricDescriptorsResponse\x128\n\x12metric_descriptors\x18\x01 \x03(\x0b2\x1c.google.api.MetricDescriptor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"^\n\x1aGetMetricDescriptorRequest\x12@\n\x04name\x18\x03 \x01(\tB2\xe0A\x02\xfaA,\n*monitoring.googleapis.com/MetricDescriptor"\x9f\x01\n\x1dCreateMetricDescriptorRequest\x12@\n\x04name\x18\x03 \x01(\tB2\xe0A\x02\xfaA,\x12*monitoring.googleapis.com/MetricDescriptor\x12<\n\x11metric_descriptor\x18\x02 \x01(\x0b2\x1c.google.api.MetricDescriptorB\x03\xe0A\x02"a\n\x1dDeleteMetricDescriptorRequest\x12@\n\x04name\x18\x03 \x01(\tB2\xe0A\x02\xfaA,\n*monitoring.googleapis.com/MetricDescriptor"\xce\x03\n\x15ListTimeSeriesRequest\x12:\n\x04name\x18\n \x01(\tB,\xe0A\x02\xfaA&\x12$monitoring.googleapis.com/TimeSeries\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x08interval\x18\x04 \x01(\x0b2".google.monitoring.v3.TimeIntervalB\x03\xe0A\x02\x126\n\x0baggregation\x18\x05 \x01(\x0b2!.google.monitoring.v3.Aggregation\x12@\n\x15secondary_aggregation\x18\x0b \x01(\x0b2!.google.monitoring.v3.Aggregation\x12\x10\n\x08order_by\x18\x06 \x01(\t\x12M\n\x04view\x18\x07 \x01(\x0e2:.google.monitoring.v3.ListTimeSeriesRequest.TimeSeriesViewB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x08 \x01(\x05\x12\x12\n\npage_token\x18\t \x01(\t"\'\n\x0eTimeSeriesView\x12\x08\n\x04FULL\x10\x00\x12\x0b\n\x07HEADERS\x10\x01"\xa4\x01\n\x16ListTimeSeriesResponse\x125\n\x0btime_series\x18\x01 \x03(\x0b2 .google.monitoring.v3.TimeSeries\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12,\n\x10execution_errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status\x12\x0c\n\x04unit\x18\x05 \x01(\t"\x98\x01\n\x17CreateTimeSeriesRequest\x12A\n\x04name\x18\x03 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12:\n\x0btime_series\x18\x02 \x03(\x0b2 .google.monitoring.v3.TimeSeriesB\x03\xe0A\x02"z\n\x15CreateTimeSeriesError\x129\n\x0btime_series\x18\x01 \x01(\x0b2 .google.monitoring.v3.TimeSeriesB\x02\x18\x01\x12&\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.StatusB\x02\x18\x01"\xd8\x01\n\x17CreateTimeSeriesSummary\x12\x19\n\x11total_point_count\x18\x01 \x01(\x05\x12\x1b\n\x13success_point_count\x18\x02 \x01(\x05\x12C\n\x06errors\x18\x03 \x03(\x0b23.google.monitoring.v3.CreateTimeSeriesSummary.Error\x1a@\n\x05Error\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12\x13\n\x0bpoint_count\x18\x02 \x01(\x05"j\n\x16QueryTimeSeriesRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05query\x18\x07 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\t \x01(\x05\x12\x12\n\npage_token\x18\n \x01(\t:\x02\x18\x01"\xee\x01\n\x17QueryTimeSeriesResponse\x12J\n\x16time_series_descriptor\x18\x08 \x01(\x0b2*.google.monitoring.v3.TimeSeriesDescriptor\x12>\n\x10time_series_data\x18\t \x03(\x0b2$.google.monitoring.v3.TimeSeriesData\x12\x17\n\x0fnext_page_token\x18\n \x01(\t\x12*\n\x0epartial_errors\x18\x0b \x03(\x0b2\x12.google.rpc.Status:\x02\x18\x01"Y\n\x0eQueryErrorList\x120\n\x06errors\x18\x01 \x03(\x0b2 .google.monitoring.v3.QueryError\x12\x15\n\rerror_summary\x18\x02 \x01(\t2\xbc\x0f\n\rMetricService\x12\xe4\x01\n ListMonitoredResourceDescriptors\x12=.google.monitoring.v3.ListMonitoredResourceDescriptorsRequest\x1a>.google.monitoring.v3.ListMonitoredResourceDescriptorsResponse"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v3/{name=projects/*}/monitoredResourceDescriptors\x12\xcc\x01\n\x1eGetMonitoredResourceDescriptor\x12;.google.monitoring.v3.GetMonitoredResourceDescriptorRequest\x1a\'.google.api.MonitoredResourceDescriptor"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v3/{name=projects/*/monitoredResourceDescriptors/**}\x12\xb8\x01\n\x15ListMetricDescriptors\x122.google.monitoring.v3.ListMetricDescriptorsRequest\x1a3.google.monitoring.v3.ListMetricDescriptorsResponse"6\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12\'/v3/{name=projects/*}/metricDescriptors\x12\xa0\x01\n\x13GetMetricDescriptor\x120.google.monitoring.v3.GetMetricDescriptorRequest\x1a\x1c.google.api.MetricDescriptor"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*/metricDescriptors/**}\x12\xc8\x01\n\x16CreateMetricDescriptor\x123.google.monitoring.v3.CreateMetricDescriptorRequest\x1a\x1c.google.api.MetricDescriptor"[\xdaA\x16name,metric_descriptor\x82\xd3\xe4\x93\x02<"\'/v3/{name=projects/*}/metricDescriptors:\x11metric_descriptor\x12\xa0\x01\n\x16DeleteMetricDescriptor\x123.google.monitoring.v3.DeleteMetricDescriptorRequest\x1a\x16.google.protobuf.Empty"9\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v3/{name=projects/*/metricDescriptors/**}\x12\xfe\x01\n\x0eListTimeSeries\x12+.google.monitoring.v3.ListTimeSeriesRequest\x1a,.google.monitoring.v3.ListTimeSeriesResponse"\x90\x01\xdaA\x19name,filter,interval,view\x82\xd3\xe4\x93\x02n\x12 /v3/{name=projects/*}/timeSeriesZ\'\x12%/v3/{name=organizations/*}/timeSeriesZ!\x12\x1f/v3/{name=folders/*}/timeSeries\x12\x99\x01\n\x10CreateTimeSeries\x12-.google.monitoring.v3.CreateTimeSeriesRequest\x1a\x16.google.protobuf.Empty">\xdaA\x10name,time_series\x82\xd3\xe4\x93\x02%" /v3/{name=projects/*}/timeSeries:\x01*\x12\xae\x01\n\x17CreateServiceTimeSeries\x12-.google.monitoring.v3.CreateTimeSeriesRequest\x1a\x16.google.protobuf.Empty"L\xdaA\x10name,time_series\x82\xd3\xe4\x93\x023"./v3/{name=projects/*}/timeSeries:createService:\x01*\x1a\xda\x01\xcaA\x19monitoring.googleapis.com\xd2A\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.writeB\x89\x08\n\x18com.google.monitoring.v3B\x12MetricServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3\xeaA\xf0\x01\n*monitoring.googleapis.com/MetricDescriptor\x12;projects/{project}/metricDescriptors/{metric_descriptor=**}\x12Eorganizations/{organization}/metricDescriptors/{metric_descriptor=**}\x129folders/{folder}/metricDescriptors/{metric_descriptor=**}\x12\x01* \x01\xeaA\xb7\x02\n5monitoring.googleapis.com/MonitoredResourceDescriptor\x12Oprojects/{project}/monitoredResourceDescriptors/{monitored_resource_descriptor}\x12Yorganizations/{organization}/monitoredResourceDescriptors/{monitored_resource_descriptor}\x12Mfolders/{folder}/monitoredResourceDescriptors/{monitored_resource_descriptor}\x12\x01* \x01\xeaAQ\n#monitoring.googleapis.com/Workspace\x12\x12projects/{project}\x12\x16workspaces/{workspace}\xeaA\xb5\x01\n$monitoring.googleapis.com/TimeSeries\x12+projects/{project}/timeSeries/{time_series}\x125organizations/{organization}/timeSeries/{time_series}\x12)folders/{folder}/timeSeries/{time_series}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.metric_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x12MetricServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3\xeaA\xf0\x01\n*monitoring.googleapis.com/MetricDescriptor\x12;projects/{project}/metricDescriptors/{metric_descriptor=**}\x12Eorganizations/{organization}/metricDescriptors/{metric_descriptor=**}\x129folders/{folder}/metricDescriptors/{metric_descriptor=**}\x12\x01* \x01\xeaA\xb7\x02\n5monitoring.googleapis.com/MonitoredResourceDescriptor\x12Oprojects/{project}/monitoredResourceDescriptors/{monitored_resource_descriptor}\x12Yorganizations/{organization}/monitoredResourceDescriptors/{monitored_resource_descriptor}\x12Mfolders/{folder}/monitoredResourceDescriptors/{monitored_resource_descriptor}\x12\x01* \x01\xeaAQ\n#monitoring.googleapis.com/Workspace\x12\x12projects/{project}\x12\x16workspaces/{workspace}\xeaA\xb5\x01\n$monitoring.googleapis.com/TimeSeries\x12+projects/{project}/timeSeries/{time_series}\x125organizations/{organization}/timeSeries/{time_series}\x12)folders/{folder}/timeSeries/{time_series}'
    _globals['_LISTMONITOREDRESOURCEDESCRIPTORSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTMONITOREDRESOURCEDESCRIPTORSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA7\x125monitoring.googleapis.com/MonitoredResourceDescriptor'
    _globals['_GETMONITOREDRESOURCEDESCRIPTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMONITOREDRESOURCEDESCRIPTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA7\n5monitoring.googleapis.com/MonitoredResourceDescriptor'
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\x12*monitoring.googleapis.com/MetricDescriptor'
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMETRICDESCRIPTORSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETMETRICDESCRIPTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMETRICDESCRIPTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*monitoring.googleapis.com/MetricDescriptor'
    _globals['_CREATEMETRICDESCRIPTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CREATEMETRICDESCRIPTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\x12*monitoring.googleapis.com/MetricDescriptor'
    _globals['_CREATEMETRICDESCRIPTORREQUEST'].fields_by_name['metric_descriptor']._loaded_options = None
    _globals['_CREATEMETRICDESCRIPTORREQUEST'].fields_by_name['metric_descriptor']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEMETRICDESCRIPTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMETRICDESCRIPTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*monitoring.googleapis.com/MetricDescriptor'
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\x12$monitoring.googleapis.com/TimeSeries'
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['interval']._loaded_options = None
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['interval']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTTIMESERIESREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETIMESERIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CREATETIMESERIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATETIMESERIESREQUEST'].fields_by_name['time_series']._loaded_options = None
    _globals['_CREATETIMESERIESREQUEST'].fields_by_name['time_series']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETIMESERIESERROR'].fields_by_name['time_series']._loaded_options = None
    _globals['_CREATETIMESERIESERROR'].fields_by_name['time_series']._serialized_options = b'\x18\x01'
    _globals['_CREATETIMESERIESERROR'].fields_by_name['status']._loaded_options = None
    _globals['_CREATETIMESERIESERROR'].fields_by_name['status']._serialized_options = b'\x18\x01'
    _globals['_QUERYTIMESERIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYTIMESERIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYTIMESERIESREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_QUERYTIMESERIESREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYTIMESERIESREQUEST']._loaded_options = None
    _globals['_QUERYTIMESERIESREQUEST']._serialized_options = b'\x18\x01'
    _globals['_QUERYTIMESERIESRESPONSE']._loaded_options = None
    _globals['_QUERYTIMESERIESRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_METRICSERVICE']._loaded_options = None
    _globals['_METRICSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.write'
    _globals['_METRICSERVICE'].methods_by_name['ListMonitoredResourceDescriptors']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['ListMonitoredResourceDescriptors']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v3/{name=projects/*}/monitoredResourceDescriptors'
    _globals['_METRICSERVICE'].methods_by_name['GetMonitoredResourceDescriptor']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['GetMonitoredResourceDescriptor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v3/{name=projects/*/monitoredResourceDescriptors/**}'
    _globals['_METRICSERVICE'].methods_by_name['ListMetricDescriptors']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['ListMetricDescriptors']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12'/v3/{name=projects/*}/metricDescriptors"
    _globals['_METRICSERVICE'].methods_by_name['GetMetricDescriptor']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['GetMetricDescriptor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*/metricDescriptors/**}'
    _globals['_METRICSERVICE'].methods_by_name['CreateMetricDescriptor']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['CreateMetricDescriptor']._serialized_options = b'\xdaA\x16name,metric_descriptor\x82\xd3\xe4\x93\x02<"\'/v3/{name=projects/*}/metricDescriptors:\x11metric_descriptor'
    _globals['_METRICSERVICE'].methods_by_name['DeleteMetricDescriptor']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['DeleteMetricDescriptor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v3/{name=projects/*/metricDescriptors/**}'
    _globals['_METRICSERVICE'].methods_by_name['ListTimeSeries']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['ListTimeSeries']._serialized_options = b"\xdaA\x19name,filter,interval,view\x82\xd3\xe4\x93\x02n\x12 /v3/{name=projects/*}/timeSeriesZ'\x12%/v3/{name=organizations/*}/timeSeriesZ!\x12\x1f/v3/{name=folders/*}/timeSeries"
    _globals['_METRICSERVICE'].methods_by_name['CreateTimeSeries']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['CreateTimeSeries']._serialized_options = b'\xdaA\x10name,time_series\x82\xd3\xe4\x93\x02%" /v3/{name=projects/*}/timeSeries:\x01*'
    _globals['_METRICSERVICE'].methods_by_name['CreateServiceTimeSeries']._loaded_options = None
    _globals['_METRICSERVICE'].methods_by_name['CreateServiceTimeSeries']._serialized_options = b'\xdaA\x10name,time_series\x82\xd3\xe4\x93\x023"./v3/{name=projects/*}/timeSeries:createService:\x01*'
    _globals['_LISTMONITOREDRESOURCEDESCRIPTORSREQUEST']._serialized_start = 369
    _globals['_LISTMONITOREDRESOURCEDESCRIPTORSREQUEST']._serialized_end = 542
    _globals['_LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE']._serialized_start = 545
    _globals['_LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE']._serialized_end = 683
    _globals['_GETMONITOREDRESOURCEDESCRIPTORREQUEST']._serialized_start = 685
    _globals['_GETMONITOREDRESOURCEDESCRIPTORREQUEST']._serialized_end = 801
    _globals['_LISTMETRICDESCRIPTORSREQUEST']._serialized_start = 804
    _globals['_LISTMETRICDESCRIPTORSREQUEST']._serialized_end = 970
    _globals['_LISTMETRICDESCRIPTORSRESPONSE']._serialized_start = 972
    _globals['_LISTMETRICDESCRIPTORSRESPONSE']._serialized_end = 1086
    _globals['_GETMETRICDESCRIPTORREQUEST']._serialized_start = 1088
    _globals['_GETMETRICDESCRIPTORREQUEST']._serialized_end = 1182
    _globals['_CREATEMETRICDESCRIPTORREQUEST']._serialized_start = 1185
    _globals['_CREATEMETRICDESCRIPTORREQUEST']._serialized_end = 1344
    _globals['_DELETEMETRICDESCRIPTORREQUEST']._serialized_start = 1346
    _globals['_DELETEMETRICDESCRIPTORREQUEST']._serialized_end = 1443
    _globals['_LISTTIMESERIESREQUEST']._serialized_start = 1446
    _globals['_LISTTIMESERIESREQUEST']._serialized_end = 1908
    _globals['_LISTTIMESERIESREQUEST_TIMESERIESVIEW']._serialized_start = 1869
    _globals['_LISTTIMESERIESREQUEST_TIMESERIESVIEW']._serialized_end = 1908
    _globals['_LISTTIMESERIESRESPONSE']._serialized_start = 1911
    _globals['_LISTTIMESERIESRESPONSE']._serialized_end = 2075
    _globals['_CREATETIMESERIESREQUEST']._serialized_start = 2078
    _globals['_CREATETIMESERIESREQUEST']._serialized_end = 2230
    _globals['_CREATETIMESERIESERROR']._serialized_start = 2232
    _globals['_CREATETIMESERIESERROR']._serialized_end = 2354
    _globals['_CREATETIMESERIESSUMMARY']._serialized_start = 2357
    _globals['_CREATETIMESERIESSUMMARY']._serialized_end = 2573
    _globals['_CREATETIMESERIESSUMMARY_ERROR']._serialized_start = 2509
    _globals['_CREATETIMESERIESSUMMARY_ERROR']._serialized_end = 2573
    _globals['_QUERYTIMESERIESREQUEST']._serialized_start = 2575
    _globals['_QUERYTIMESERIESREQUEST']._serialized_end = 2681
    _globals['_QUERYTIMESERIESRESPONSE']._serialized_start = 2684
    _globals['_QUERYTIMESERIESRESPONSE']._serialized_end = 2922
    _globals['_QUERYERRORLIST']._serialized_start = 2924
    _globals['_QUERYERRORLIST']._serialized_end = 3013
    _globals['_METRICSERVICE']._serialized_start = 3016
    _globals['_METRICSERVICE']._serialized_end = 4996