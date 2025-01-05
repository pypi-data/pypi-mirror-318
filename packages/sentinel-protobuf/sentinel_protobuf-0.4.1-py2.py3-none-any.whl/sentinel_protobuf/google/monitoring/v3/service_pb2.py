"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....google.type import calendar_period_pb2 as google_dot_type_dot_calendar__period__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/monitoring/v3/service.proto\x12\x14google.monitoring.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a!google/type/calendar_period.proto"\x94\x11\n\x07Service\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x126\n\x06custom\x18\x06 \x01(\x0b2$.google.monitoring.v3.Service.CustomH\x00\x12=\n\napp_engine\x18\x07 \x01(\x0b2\'.google.monitoring.v3.Service.AppEngineH\x00\x12G\n\x0fcloud_endpoints\x18\x08 \x01(\x0b2,.google.monitoring.v3.Service.CloudEndpointsH\x00\x12C\n\rcluster_istio\x18\t \x01(\x0b2*.google.monitoring.v3.Service.ClusterIstioH\x00\x12=\n\nmesh_istio\x18\n \x01(\x0b2\'.google.monitoring.v3.Service.MeshIstioH\x00\x12V\n\x17istio_canonical_service\x18\x0b \x01(\x0b23.google.monitoring.v3.Service.IstioCanonicalServiceH\x00\x12;\n\tcloud_run\x18\x0c \x01(\x0b2&.google.monitoring.v3.Service.CloudRunH\x00\x12C\n\rgke_namespace\x18\x0f \x01(\x0b2*.google.monitoring.v3.Service.GkeNamespaceH\x00\x12A\n\x0cgke_workload\x18\x10 \x01(\x0b2).google.monitoring.v3.Service.GkeWorkloadH\x00\x12?\n\x0bgke_service\x18\x11 \x01(\x0b2(.google.monitoring.v3.Service.GkeServiceH\x00\x12A\n\rbasic_service\x18\x13 \x01(\x0b2*.google.monitoring.v3.Service.BasicService\x12:\n\ttelemetry\x18\r \x01(\x0b2\'.google.monitoring.v3.Service.Telemetry\x12B\n\x0buser_labels\x18\x0e \x03(\x0b2-.google.monitoring.v3.Service.UserLabelsEntry\x1a\x08\n\x06Custom\x1a\x1e\n\tAppEngine\x12\x11\n\tmodule_id\x18\x01 \x01(\t\x1a!\n\x0eCloudEndpoints\x12\x0f\n\x07service\x18\x01 \x01(\t\x1ag\n\x0cClusterIstio\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x14\n\x0ccluster_name\x18\x02 \x01(\t\x12\x19\n\x11service_namespace\x18\x03 \x01(\t\x12\x14\n\x0cservice_name\x18\x04 \x01(\t\x1aN\n\tMeshIstio\x12\x10\n\x08mesh_uid\x18\x01 \x01(\t\x12\x19\n\x11service_namespace\x18\x03 \x01(\t\x12\x14\n\x0cservice_name\x18\x04 \x01(\t\x1ai\n\x15IstioCanonicalService\x12\x10\n\x08mesh_uid\x18\x01 \x01(\t\x12#\n\x1bcanonical_service_namespace\x18\x03 \x01(\t\x12\x19\n\x11canonical_service\x18\x04 \x01(\t\x1a2\n\x08CloudRun\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x1ag\n\x0cGkeNamespace\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x14\n\x0ccluster_name\x18\x03 \x01(\t\x12\x16\n\x0enamespace_name\x18\x04 \x01(\t\x1a\xac\x01\n\x0bGkeWorkload\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x14\n\x0ccluster_name\x18\x03 \x01(\t\x12\x16\n\x0enamespace_name\x18\x04 \x01(\t\x12!\n\x19top_level_controller_type\x18\x05 \x01(\t\x12!\n\x19top_level_controller_name\x18\x06 \x01(\t\x1a{\n\nGkeService\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x14\n\x0ccluster_name\x18\x03 \x01(\t\x12\x16\n\x0enamespace_name\x18\x04 \x01(\t\x12\x14\n\x0cservice_name\x18\x05 \x01(\t\x1a\xb1\x01\n\x0cBasicService\x12\x14\n\x0cservice_type\x18\x01 \x01(\t\x12U\n\x0eservice_labels\x18\x02 \x03(\x0b2=.google.monitoring.v3.Service.BasicService.ServiceLabelsEntry\x1a4\n\x12ServiceLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a"\n\tTelemetry\x12\x15\n\rresource_name\x18\x01 \x01(\t\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xa7\x01\xeaA\xa3\x01\n!monitoring.googleapis.com/Service\x12%projects/{project}/services/{service}\x12/organizations/{organization}/services/{service}\x12#folders/{folder}/services/{service}\x12\x01*B\x0c\n\nidentifier"\x9b\x06\n\x15ServiceLevelObjective\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x0b \x01(\t\x12L\n\x17service_level_indicator\x18\x03 \x01(\x0b2+.google.monitoring.v3.ServiceLevelIndicator\x12\x0c\n\x04goal\x18\x04 \x01(\x01\x123\n\x0erolling_period\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x126\n\x0fcalendar_period\x18\x06 \x01(\x0e2\x1b.google.type.CalendarPeriodH\x00\x12P\n\x0buser_labels\x18\x0c \x03(\x0b2;.google.monitoring.v3.ServiceLevelObjective.UserLabelsEntry\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"4\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\x08\n\x04FULL\x10\x02\x12\x0c\n\x08EXPLICIT\x10\x01:\xca\x02\xeaA\xc6\x02\n/monitoring.googleapis.com/ServiceLevelObjective\x12Vprojects/{project}/services/{service}/serviceLevelObjectives/{service_level_objective}\x12`organizations/{organization}/services/{service}/serviceLevelObjectives/{service_level_objective}\x12Tfolders/{folder}/services/{service}/serviceLevelObjectives/{service_level_objective}\x12\x01* \x01B\x08\n\x06period"\xd4\x01\n\x15ServiceLevelIndicator\x123\n\tbasic_sli\x18\x04 \x01(\x0b2\x1e.google.monitoring.v3.BasicSliH\x00\x12>\n\rrequest_based\x18\x01 \x01(\x0b2%.google.monitoring.v3.RequestBasedSliH\x00\x12>\n\rwindows_based\x18\x02 \x01(\x0b2%.google.monitoring.v3.WindowsBasedSliH\x00B\x06\n\x04type"\xb6\x02\n\x08BasicSli\x12\x0e\n\x06method\x18\x07 \x03(\t\x12\x10\n\x08location\x18\x08 \x03(\t\x12\x0f\n\x07version\x18\t \x03(\t\x12K\n\x0cavailability\x18\x02 \x01(\x0b23.google.monitoring.v3.BasicSli.AvailabilityCriteriaH\x00\x12A\n\x07latency\x18\x03 \x01(\x0b2..google.monitoring.v3.BasicSli.LatencyCriteriaH\x00\x1a\x16\n\x14AvailabilityCriteria\x1a?\n\x0fLatencyCriteria\x12,\n\tthreshold\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x0e\n\x0csli_criteria"!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01"\xa1\x01\n\x0fRequestBasedSli\x12A\n\x10good_total_ratio\x18\x01 \x01(\x0b2%.google.monitoring.v3.TimeSeriesRatioH\x00\x12A\n\x10distribution_cut\x18\x03 \x01(\x0b2%.google.monitoring.v3.DistributionCutH\x00B\x08\n\x06method"h\n\x0fTimeSeriesRatio\x12\x1b\n\x13good_service_filter\x18\x04 \x01(\t\x12\x1a\n\x12bad_service_filter\x18\x05 \x01(\t\x12\x1c\n\x14total_service_filter\x18\x06 \x01(\t"Z\n\x0fDistributionCut\x12\x1b\n\x13distribution_filter\x18\x04 \x01(\t\x12*\n\x05range\x18\x05 \x01(\x0b2\x1b.google.monitoring.v3.Range"\x83\x05\n\x0fWindowsBasedSli\x12 \n\x16good_bad_metric_filter\x18\x05 \x01(\tH\x00\x12`\n\x1agood_total_ratio_threshold\x18\x02 \x01(\x0b2:.google.monitoring.v3.WindowsBasedSli.PerformanceThresholdH\x00\x12Q\n\x14metric_mean_in_range\x18\x06 \x01(\x0b21.google.monitoring.v3.WindowsBasedSli.MetricRangeH\x00\x12P\n\x13metric_sum_in_range\x18\x07 \x01(\x0b21.google.monitoring.v3.WindowsBasedSli.MetricRangeH\x00\x120\n\rwindow_period\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x1a\xb0\x01\n\x14PerformanceThreshold\x12<\n\x0bperformance\x18\x01 \x01(\x0b2%.google.monitoring.v3.RequestBasedSliH\x00\x12?\n\x15basic_sli_performance\x18\x03 \x01(\x0b2\x1e.google.monitoring.v3.BasicSliH\x00\x12\x11\n\tthreshold\x18\x02 \x01(\x01B\x06\n\x04type\x1aN\n\x0bMetricRange\x12\x13\n\x0btime_series\x18\x01 \x01(\t\x12*\n\x05range\x18\x04 \x01(\x0b2\x1b.google.monitoring.v3.RangeB\x12\n\x10window_criterionB\xd1\x01\n\x18com.google.monitoring.v3B\x16ServiceMonitoringProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x16ServiceMonitoringProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_SERVICE_GKENAMESPACE'].fields_by_name['project_id']._loaded_options = None
    _globals['_SERVICE_GKENAMESPACE'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICE_GKEWORKLOAD'].fields_by_name['project_id']._loaded_options = None
    _globals['_SERVICE_GKEWORKLOAD'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICE_GKESERVICE'].fields_by_name['project_id']._loaded_options = None
    _globals['_SERVICE_GKESERVICE'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICE_BASICSERVICE_SERVICELABELSENTRY']._loaded_options = None
    _globals['_SERVICE_BASICSERVICE_SERVICELABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICE_USERLABELSENTRY']._loaded_options = None
    _globals['_SERVICE_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICE'].fields_by_name['name']._loaded_options = None
    _globals['_SERVICE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SERVICE']._loaded_options = None
    _globals['_SERVICE']._serialized_options = b'\xeaA\xa3\x01\n!monitoring.googleapis.com/Service\x12%projects/{project}/services/{service}\x12/organizations/{organization}/services/{service}\x12#folders/{folder}/services/{service}\x12\x01*'
    _globals['_SERVICELEVELOBJECTIVE_USERLABELSENTRY']._loaded_options = None
    _globals['_SERVICELEVELOBJECTIVE_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICELEVELOBJECTIVE'].fields_by_name['name']._loaded_options = None
    _globals['_SERVICELEVELOBJECTIVE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SERVICELEVELOBJECTIVE']._loaded_options = None
    _globals['_SERVICELEVELOBJECTIVE']._serialized_options = b'\xeaA\xc6\x02\n/monitoring.googleapis.com/ServiceLevelObjective\x12Vprojects/{project}/services/{service}/serviceLevelObjectives/{service_level_objective}\x12`organizations/{organization}/services/{service}/serviceLevelObjectives/{service_level_objective}\x12Tfolders/{folder}/services/{service}/serviceLevelObjectives/{service_level_objective}\x12\x01* \x01'
    _globals['_SERVICE']._serialized_start = 188
    _globals['_SERVICE']._serialized_end = 2384
    _globals['_SERVICE_CUSTOM']._serialized_start = 1109
    _globals['_SERVICE_CUSTOM']._serialized_end = 1117
    _globals['_SERVICE_APPENGINE']._serialized_start = 1119
    _globals['_SERVICE_APPENGINE']._serialized_end = 1149
    _globals['_SERVICE_CLOUDENDPOINTS']._serialized_start = 1151
    _globals['_SERVICE_CLOUDENDPOINTS']._serialized_end = 1184
    _globals['_SERVICE_CLUSTERISTIO']._serialized_start = 1186
    _globals['_SERVICE_CLUSTERISTIO']._serialized_end = 1289
    _globals['_SERVICE_MESHISTIO']._serialized_start = 1291
    _globals['_SERVICE_MESHISTIO']._serialized_end = 1369
    _globals['_SERVICE_ISTIOCANONICALSERVICE']._serialized_start = 1371
    _globals['_SERVICE_ISTIOCANONICALSERVICE']._serialized_end = 1476
    _globals['_SERVICE_CLOUDRUN']._serialized_start = 1478
    _globals['_SERVICE_CLOUDRUN']._serialized_end = 1528
    _globals['_SERVICE_GKENAMESPACE']._serialized_start = 1530
    _globals['_SERVICE_GKENAMESPACE']._serialized_end = 1633
    _globals['_SERVICE_GKEWORKLOAD']._serialized_start = 1636
    _globals['_SERVICE_GKEWORKLOAD']._serialized_end = 1808
    _globals['_SERVICE_GKESERVICE']._serialized_start = 1810
    _globals['_SERVICE_GKESERVICE']._serialized_end = 1933
    _globals['_SERVICE_BASICSERVICE']._serialized_start = 1936
    _globals['_SERVICE_BASICSERVICE']._serialized_end = 2113
    _globals['_SERVICE_BASICSERVICE_SERVICELABELSENTRY']._serialized_start = 2061
    _globals['_SERVICE_BASICSERVICE_SERVICELABELSENTRY']._serialized_end = 2113
    _globals['_SERVICE_TELEMETRY']._serialized_start = 2115
    _globals['_SERVICE_TELEMETRY']._serialized_end = 2149
    _globals['_SERVICE_USERLABELSENTRY']._serialized_start = 2151
    _globals['_SERVICE_USERLABELSENTRY']._serialized_end = 2200
    _globals['_SERVICELEVELOBJECTIVE']._serialized_start = 2387
    _globals['_SERVICELEVELOBJECTIVE']._serialized_end = 3182
    _globals['_SERVICELEVELOBJECTIVE_USERLABELSENTRY']._serialized_start = 2151
    _globals['_SERVICELEVELOBJECTIVE_USERLABELSENTRY']._serialized_end = 2200
    _globals['_SERVICELEVELOBJECTIVE_VIEW']._serialized_start = 2787
    _globals['_SERVICELEVELOBJECTIVE_VIEW']._serialized_end = 2839
    _globals['_SERVICELEVELINDICATOR']._serialized_start = 3185
    _globals['_SERVICELEVELINDICATOR']._serialized_end = 3397
    _globals['_BASICSLI']._serialized_start = 3400
    _globals['_BASICSLI']._serialized_end = 3710
    _globals['_BASICSLI_AVAILABILITYCRITERIA']._serialized_start = 3607
    _globals['_BASICSLI_AVAILABILITYCRITERIA']._serialized_end = 3629
    _globals['_BASICSLI_LATENCYCRITERIA']._serialized_start = 3631
    _globals['_BASICSLI_LATENCYCRITERIA']._serialized_end = 3694
    _globals['_RANGE']._serialized_start = 3712
    _globals['_RANGE']._serialized_end = 3745
    _globals['_REQUESTBASEDSLI']._serialized_start = 3748
    _globals['_REQUESTBASEDSLI']._serialized_end = 3909
    _globals['_TIMESERIESRATIO']._serialized_start = 3911
    _globals['_TIMESERIESRATIO']._serialized_end = 4015
    _globals['_DISTRIBUTIONCUT']._serialized_start = 4017
    _globals['_DISTRIBUTIONCUT']._serialized_end = 4107
    _globals['_WINDOWSBASEDSLI']._serialized_start = 4110
    _globals['_WINDOWSBASEDSLI']._serialized_end = 4753
    _globals['_WINDOWSBASEDSLI_PERFORMANCETHRESHOLD']._serialized_start = 4477
    _globals['_WINDOWSBASEDSLI_PERFORMANCETHRESHOLD']._serialized_end = 4653
    _globals['_WINDOWSBASEDSLI_METRICRANGE']._serialized_start = 4655
    _globals['_WINDOWSBASEDSLI_METRICRANGE']._serialized_end = 4733