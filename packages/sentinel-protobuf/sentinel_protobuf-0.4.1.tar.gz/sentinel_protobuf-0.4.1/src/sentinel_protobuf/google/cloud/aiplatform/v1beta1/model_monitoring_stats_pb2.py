"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/model_monitoring_stats.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/aiplatform/v1beta1/model_monitoring_stats.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"v\n\x14ModelMonitoringStats\x12U\n\rtabular_stats\x18\x01 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.ModelMonitoringTabularStatsH\x00B\x07\n\x05stats"\x9c\x05\n\x1dModelMonitoringStatsDataPoint\x12`\n\rcurrent_stats\x18\x01 \x01(\x0b2I.google.cloud.aiplatform.v1beta1.ModelMonitoringStatsDataPoint.TypedValue\x12a\n\x0ebaseline_stats\x18\x02 \x01(\x0b2I.google.cloud.aiplatform.v1beta1.ModelMonitoringStatsDataPoint.TypedValue\x12\x17\n\x0fthreshold_value\x18\x03 \x01(\x01\x12\x13\n\x0bhas_anomaly\x18\x04 \x01(\x08\x12\x1c\n\x14model_monitoring_job\x18\x05 \x01(\t\x12\x10\n\x08schedule\x18\x06 \x01(\t\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\talgorithm\x18\x08 \x01(\t\x1a\x93\x02\n\nTypedValue\x12\x16\n\x0cdouble_value\x18\x01 \x01(\x01H\x00\x12}\n\x12distribution_value\x18\x02 \x01(\x0b2_.google.cloud.aiplatform.v1beta1.ModelMonitoringStatsDataPoint.TypedValue.DistributionDataValueH\x00\x1ae\n\x15DistributionDataValue\x12,\n\x0cdistribution\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x1e\n\x16distribution_deviation\x18\x02 \x01(\x01B\x07\n\x05value"\x9e\x01\n\x1bModelMonitoringTabularStats\x12\x12\n\nstats_name\x18\x01 \x01(\t\x12\x16\n\x0eobjective_type\x18\x02 \x01(\t\x12S\n\x0bdata_points\x18\x03 \x03(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringStatsDataPoint"\xb9\x02\n SearchModelMonitoringStatsFilter\x12t\n\x14tabular_stats_filter\x18\x01 \x01(\x0b2T.google.cloud.aiplatform.v1beta1.SearchModelMonitoringStatsFilter.TabularStatsFilterH\x00\x1a\x94\x01\n\x12TabularStatsFilter\x12\x12\n\nstats_name\x18\x01 \x01(\t\x12\x16\n\x0eobjective_type\x18\x02 \x01(\t\x12\x1c\n\x14model_monitoring_job\x18\x03 \x01(\t\x12!\n\x19model_monitoring_schedule\x18\x04 \x01(\t\x12\x11\n\talgorithm\x18\x05 \x01(\tB\x08\n\x06filterB\xf0\x01\n#com.google.cloud.aiplatform.v1beta1B\x19ModelMonitoringStatsProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_monitoring_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x19ModelMonitoringStatsProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELMONITORINGSTATS']._serialized_start = 160
    _globals['_MODELMONITORINGSTATS']._serialized_end = 278
    _globals['_MODELMONITORINGSTATSDATAPOINT']._serialized_start = 281
    _globals['_MODELMONITORINGSTATSDATAPOINT']._serialized_end = 949
    _globals['_MODELMONITORINGSTATSDATAPOINT_TYPEDVALUE']._serialized_start = 674
    _globals['_MODELMONITORINGSTATSDATAPOINT_TYPEDVALUE']._serialized_end = 949
    _globals['_MODELMONITORINGSTATSDATAPOINT_TYPEDVALUE_DISTRIBUTIONDATAVALUE']._serialized_start = 839
    _globals['_MODELMONITORINGSTATSDATAPOINT_TYPEDVALUE_DISTRIBUTIONDATAVALUE']._serialized_end = 940
    _globals['_MODELMONITORINGTABULARSTATS']._serialized_start = 952
    _globals['_MODELMONITORINGTABULARSTATS']._serialized_end = 1110
    _globals['_SEARCHMODELMONITORINGSTATSFILTER']._serialized_start = 1113
    _globals['_SEARCHMODELMONITORINGSTATSFILTER']._serialized_end = 1426
    _globals['_SEARCHMODELMONITORINGSTATSFILTER_TABULARSTATSFILTER']._serialized_start = 1268
    _globals['_SEARCHMODELMONITORINGSTATSFILTER_TABULARSTATSFILTER']._serialized_end = 1416