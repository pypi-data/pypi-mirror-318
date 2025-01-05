"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/model_deployment_monitoring_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_monitoring_stats_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__monitoring__stats__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/aiplatform/v1beta1/model_deployment_monitoring_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a>google/cloud/aiplatform/v1beta1/feature_monitoring_stats.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a6google/cloud/aiplatform/v1beta1/model_monitoring.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x9d\x11\n\x1cModelDeploymentMonitoringJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12<\n\x08endpoint\x18\x03 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12=\n\x05state\x18\x04 \x01(\x0e2).google.cloud.aiplatform.v1beta1.JobStateB\x03\xe0A\x03\x12r\n\x0eschedule_state\x18\x05 \x01(\x0e2U.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob.MonitoringScheduleStateB\x03\xe0A\x03\x12\x90\x01\n#latest_monitoring_pipeline_metadata\x18\x19 \x01(\x0b2^.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob.LatestMonitoringPipelineMetadataB\x03\xe0A\x03\x12\x85\x01\n-model_deployment_monitoring_objective_configs\x18\x06 \x03(\x0b2I.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringObjectiveConfigB\x03\xe0A\x02\x12\x82\x01\n+model_deployment_monitoring_schedule_config\x18\x07 \x01(\x0b2H.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringScheduleConfigB\x03\xe0A\x02\x12Y\n\x19logging_sampling_strategy\x18\x08 \x01(\x0b21.google.cloud.aiplatform.v1beta1.SamplingStrategyB\x03\xe0A\x02\x12b\n\x1dmodel_monitoring_alert_config\x18\x0f \x01(\x0b2;.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertConfig\x12#\n\x1bpredict_instance_schema_uri\x18\t \x01(\t\x127\n\x17sample_predict_instance\x18\x13 \x01(\x0b2\x16.google.protobuf.Value\x12$\n\x1canalysis_instance_schema_uri\x18\x10 \x01(\t\x12e\n\x0fbigquery_tables\x18\n \x03(\x0b2G.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringBigQueryTableB\x03\xe0A\x03\x12*\n\x07log_ttl\x18\x11 \x01(\x0b2\x19.google.protobuf.Duration\x12Y\n\x06labels\x18\x0b \x03(\x0b2I.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob.LabelsEntry\x124\n\x0bcreate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x12next_schedule_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12W\n\x1estats_anomalies_base_directory\x18\x14 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestination\x12H\n\x0fencryption_spec\x18\x15 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12\'\n\x1fenable_monitoring_pipeline_logs\x18\x16 \x01(\x08\x12&\n\x05error\x18\x17 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x1a \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x1b \x01(\x08B\x03\xe0A\x03\x1at\n LatestMonitoringPipelineMetadata\x12,\n\x08run_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"k\n\x17MonitoringScheduleState\x12)\n%MONITORING_SCHEDULE_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07OFFLINE\x10\x02\x12\x0b\n\x07RUNNING\x10\x03:\xa5\x01\xeaA\xa1\x01\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob\x12gprojects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}"\xc8\x03\n&ModelDeploymentMonitoringBigQueryTable\x12e\n\nlog_source\x18\x01 \x01(\x0e2Q.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringBigQueryTable.LogSource\x12a\n\x08log_type\x18\x02 \x01(\x0e2O.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringBigQueryTable.LogType\x12\x1b\n\x13bigquery_table_path\x18\x03 \x01(\t\x124\n\'request_response_logging_schema_version\x18\x04 \x01(\tB\x03\xe0A\x03"B\n\tLogSource\x12\x1a\n\x16LOG_SOURCE_UNSPECIFIED\x10\x00\x12\x0c\n\x08TRAINING\x10\x01\x12\x0b\n\x07SERVING\x10\x02"=\n\x07LogType\x12\x18\n\x14LOG_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PREDICT\x10\x01\x12\x0b\n\x07EXPLAIN\x10\x02"\xa0\x01\n(ModelDeploymentMonitoringObjectiveConfig\x12\x19\n\x11deployed_model_id\x18\x01 \x01(\t\x12Y\n\x10objective_config\x18\x02 \x01(\x0b2?.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveConfig"\x96\x01\n\'ModelDeploymentMonitoringScheduleConfig\x128\n\x10monitor_interval\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x121\n\x0emonitor_window\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xc5\x04\n\x1dModelMonitoringStatsAnomalies\x12Z\n\tobjective\x18\x01 \x01(\x0e2G.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringObjectiveType\x12\x19\n\x11deployed_model_id\x18\x02 \x01(\t\x12\x15\n\ranomaly_count\x18\x03 \x01(\x05\x12s\n\rfeature_stats\x18\x04 \x03(\x0b2\\.google.cloud.aiplatform.v1beta1.ModelMonitoringStatsAnomalies.FeatureHistoricStatsAnomalies\x1a\xa0\x02\n\x1dFeatureHistoricStatsAnomalies\x12\x1c\n\x14feature_display_name\x18\x01 \x01(\t\x12C\n\tthreshold\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ThresholdConfig\x12L\n\x0etraining_stats\x18\x04 \x01(\x0b24.google.cloud.aiplatform.v1beta1.FeatureStatsAnomaly\x12N\n\x10prediction_stats\x18\x05 \x03(\x0b24.google.cloud.aiplatform.v1beta1.FeatureStatsAnomaly*\xce\x01\n&ModelDeploymentMonitoringObjectiveType\x12:\n6MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10RAW_FEATURE_SKEW\x10\x01\x12\x15\n\x11RAW_FEATURE_DRIFT\x10\x02\x12\x1c\n\x18FEATURE_ATTRIBUTION_SKEW\x10\x03\x12\x1d\n\x19FEATURE_ATTRIBUTION_DRIFT\x10\x04B\xf8\x01\n#com.google.cloud.aiplatform.v1beta1B!ModelDeploymentMonitoringJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_deployment_monitoring_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B!ModelDeploymentMonitoringJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELDEPLOYMENTMONITORINGJOB_LABELSENTRY']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['name']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['display_name']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['endpoint']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['state']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['schedule_state']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['schedule_state']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['latest_monitoring_pipeline_metadata']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['latest_monitoring_pipeline_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['model_deployment_monitoring_objective_configs']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['model_deployment_monitoring_objective_configs']._serialized_options = b'\xe0A\x02'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['model_deployment_monitoring_schedule_config']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['model_deployment_monitoring_schedule_config']._serialized_options = b'\xe0A\x02'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['logging_sampling_strategy']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['logging_sampling_strategy']._serialized_options = b'\xe0A\x02'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['bigquery_tables']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['bigquery_tables']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['next_schedule_time']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['next_schedule_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['error']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGJOB']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGJOB']._serialized_options = b'\xeaA\xa1\x01\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob\x12gprojects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}'
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE'].fields_by_name['request_response_logging_schema_version']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE'].fields_by_name['request_response_logging_schema_version']._serialized_options = b'\xe0A\x03'
    _globals['_MODELDEPLOYMENTMONITORINGSCHEDULECONFIG'].fields_by_name['monitor_interval']._loaded_options = None
    _globals['_MODELDEPLOYMENTMONITORINGSCHEDULECONFIG'].fields_by_name['monitor_interval']._serialized_options = b'\xe0A\x02'
    _globals['_MODELDEPLOYMENTMONITORINGOBJECTIVETYPE']._serialized_start = 4120
    _globals['_MODELDEPLOYMENTMONITORINGOBJECTIVETYPE']._serialized_end = 4326
    _globals['_MODELDEPLOYMENTMONITORINGJOB']._serialized_start = 553
    _globals['_MODELDEPLOYMENTMONITORINGJOB']._serialized_end = 2758
    _globals['_MODELDEPLOYMENTMONITORINGJOB_LATESTMONITORINGPIPELINEMETADATA']._serialized_start = 2318
    _globals['_MODELDEPLOYMENTMONITORINGJOB_LATESTMONITORINGPIPELINEMETADATA']._serialized_end = 2434
    _globals['_MODELDEPLOYMENTMONITORINGJOB_LABELSENTRY']._serialized_start = 2436
    _globals['_MODELDEPLOYMENTMONITORINGJOB_LABELSENTRY']._serialized_end = 2481
    _globals['_MODELDEPLOYMENTMONITORINGJOB_MONITORINGSCHEDULESTATE']._serialized_start = 2483
    _globals['_MODELDEPLOYMENTMONITORINGJOB_MONITORINGSCHEDULESTATE']._serialized_end = 2590
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE']._serialized_start = 2761
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE']._serialized_end = 3217
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE_LOGSOURCE']._serialized_start = 3088
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE_LOGSOURCE']._serialized_end = 3154
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE_LOGTYPE']._serialized_start = 3156
    _globals['_MODELDEPLOYMENTMONITORINGBIGQUERYTABLE_LOGTYPE']._serialized_end = 3217
    _globals['_MODELDEPLOYMENTMONITORINGOBJECTIVECONFIG']._serialized_start = 3220
    _globals['_MODELDEPLOYMENTMONITORINGOBJECTIVECONFIG']._serialized_end = 3380
    _globals['_MODELDEPLOYMENTMONITORINGSCHEDULECONFIG']._serialized_start = 3383
    _globals['_MODELDEPLOYMENTMONITORINGSCHEDULECONFIG']._serialized_end = 3533
    _globals['_MODELMONITORINGSTATSANOMALIES']._serialized_start = 3536
    _globals['_MODELMONITORINGSTATSANOMALIES']._serialized_end = 4117
    _globals['_MODELMONITORINGSTATSANOMALIES_FEATUREHISTORICSTATSANOMALIES']._serialized_start = 3829
    _globals['_MODELMONITORINGSTATSANOMALIES_FEATUREHISTORICSTATSANOMALIES']._serialized_end = 4117