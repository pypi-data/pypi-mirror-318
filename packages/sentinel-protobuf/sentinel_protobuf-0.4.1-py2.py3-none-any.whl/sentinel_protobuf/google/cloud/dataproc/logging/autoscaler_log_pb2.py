"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/logging/autoscaler_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dataproc/logging/autoscaler_log.proto\x12\x1dgoogle.cloud.dataproc.logging\x1a\x1egoogle/protobuf/duration.proto"K\n\x0bClusterSize\x12\x1c\n\x14primary_worker_count\x18\x01 \x01(\x05\x12\x1e\n\x16secondary_worker_count\x18\x02 \x01(\x05"\xa1\x01\n\rAutoscalerLog\x12?\n\x06status\x18\x01 \x01(\x0b2/.google.cloud.dataproc.logging.AutoscalerStatus\x12O\n\x0erecommendation\x18\x02 \x01(\x0b27.google.cloud.dataproc.logging.AutoscalerRecommendation"\x96\x01\n\x10AutoscalerStatus\x12=\n\x05state\x18\x01 \x01(\x0e2..google.cloud.dataproc.logging.AutoscalerState\x12\x0f\n\x07details\x18\x02 \x01(\t\x12#\n\x1bupdate_cluster_operation_id\x18\x03 \x01(\t\x12\r\n\x05error\x18\x04 \x01(\t"\xff\x07\n\x18AutoscalerRecommendation\x12N\n\x06inputs\x18\x01 \x01(\x0b2>.google.cloud.dataproc.logging.AutoscalerRecommendation.Inputs\x12P\n\x07outputs\x18\x02 \x01(\x0b2?.google.cloud.dataproc.logging.AutoscalerRecommendation.Outputs\x1a\x84\x03\n\x06Inputs\x12k\n\x0fcluster_metrics\x18\x01 \x03(\x0b2R.google.cloud.dataproc.logging.AutoscalerRecommendation.Inputs.ClusterMetricsEntry\x12H\n\x14current_cluster_size\x18\x02 \x01(\x0b2*.google.cloud.dataproc.logging.ClusterSize\x12E\n\x11min_worker_counts\x18\x03 \x01(\x0b2*.google.cloud.dataproc.logging.ClusterSize\x12E\n\x11max_worker_counts\x18\x04 \x01(\x0b2*.google.cloud.dataproc.logging.ClusterSize\x1a5\n\x13ClusterMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\xb9\x03\n\x07Outputs\x12D\n\x08decision\x18\x01 \x01(\x0e22.google.cloud.dataproc.logging.ScalingDecisionType\x12L\n\x18recommended_cluster_size\x18\x02 \x01(\x0b2*.google.cloud.dataproc.logging.ClusterSize\x12@\n\x1dgraceful_decommission_timeout\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12N\n\x13constraints_reached\x18\x04 \x03(\x0e21.google.cloud.dataproc.logging.ConstrainingFactor\x12)\n!additional_recommendation_details\x18\x05 \x03(\t\x12\x19\n\x11recommendation_id\x18\x06 \x01(\t\x12B\n\x0fdecision_metric\x18\x07 \x01(\x0e2).google.cloud.dataproc.logging.MetricType*\x8b\x01\n\x0fAutoscalerState\x12 \n\x1cAUTOSCALER_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08COOLDOWN\x10\x01\x12\x10\n\x0cRECOMMENDING\x10\x06\x12\x0b\n\x07SCALING\x10\x02\x12\x0b\n\x07STOPPED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x10\n\x0cINITIALIZING\x10\x05*\x92\x01\n\x13ScalingDecisionType\x12%\n!SCALING_DECISION_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08SCALE_UP\x10\x01\x12\x0e\n\nSCALE_DOWN\x10\x02\x12\x0c\n\x08NO_SCALE\x10\x03\x12\t\n\x05MIXED\x10\x04\x12\n\n\x06CANCEL\x10\x05\x12\x11\n\rDO_NOT_CANCEL\x10\x06*\xdc\x01\n\x12ConstrainingFactor\x12#\n\x1fCONSTRAINING_FACTOR_UNSPECIFIED\x10\x00\x12\'\n#SCALING_CAPPED_DUE_TO_LACK_OF_QUOTA\x10\x01\x12 \n\x1cREACHED_MAXIMUM_CLUSTER_SIZE\x10\x02\x12 \n\x1cREACHED_MINIMUM_CLUSTER_SIZE\x10\x03\x124\n0SECONDARY_SCALEDOWN_SINGLE_REQUEST_LIMIT_REACHED\x10\x04*_\n\nMetricType\x12\x1b\n\x17METRIC_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bYARN_MEMORY\x10\x01\x12\x0e\n\nYARN_CORES\x10\x02\x12\x13\n\x0fSPARK_EXECUTORS\x10\x03B\x7f\n!com.google.cloud.dataproc.loggingP\x01Z8cloud.google.com/go/dataproc/logging/loggingpb;loggingpb\xaa\x02\x1dGoogle.Cloud.Dataproc.Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.logging.autoscaler_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dataproc.loggingP\x01Z8cloud.google.com/go/dataproc/logging/loggingpb;loggingpb\xaa\x02\x1dGoogle.Cloud.Dataproc.Logging'
    _globals['_AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY']._loaded_options = None
    _globals['_AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY']._serialized_options = b'8\x01'
    _globals['_AUTOSCALERSTATE']._serialized_start = 1538
    _globals['_AUTOSCALERSTATE']._serialized_end = 1677
    _globals['_SCALINGDECISIONTYPE']._serialized_start = 1680
    _globals['_SCALINGDECISIONTYPE']._serialized_end = 1826
    _globals['_CONSTRAININGFACTOR']._serialized_start = 1829
    _globals['_CONSTRAININGFACTOR']._serialized_end = 2049
    _globals['_METRICTYPE']._serialized_start = 2051
    _globals['_METRICTYPE']._serialized_end = 2146
    _globals['_CLUSTERSIZE']._serialized_start = 117
    _globals['_CLUSTERSIZE']._serialized_end = 192
    _globals['_AUTOSCALERLOG']._serialized_start = 195
    _globals['_AUTOSCALERLOG']._serialized_end = 356
    _globals['_AUTOSCALERSTATUS']._serialized_start = 359
    _globals['_AUTOSCALERSTATUS']._serialized_end = 509
    _globals['_AUTOSCALERRECOMMENDATION']._serialized_start = 512
    _globals['_AUTOSCALERRECOMMENDATION']._serialized_end = 1535
    _globals['_AUTOSCALERRECOMMENDATION_INPUTS']._serialized_start = 703
    _globals['_AUTOSCALERRECOMMENDATION_INPUTS']._serialized_end = 1091
    _globals['_AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY']._serialized_start = 1038
    _globals['_AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY']._serialized_end = 1091
    _globals['_AUTOSCALERRECOMMENDATION_OUTPUTS']._serialized_start = 1094
    _globals['_AUTOSCALERRECOMMENDATION_OUTPUTS']._serialized_end = 1535