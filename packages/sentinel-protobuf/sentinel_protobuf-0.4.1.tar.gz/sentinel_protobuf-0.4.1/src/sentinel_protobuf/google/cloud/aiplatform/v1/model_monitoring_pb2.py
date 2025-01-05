"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/model_monitoring.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_io__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1/model_monitoring.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x19google/api/resource.proto\x1a#google/cloud/aiplatform/v1/io.proto"\xbf\x15\n\x1eModelMonitoringObjectiveConfig\x12d\n\x10training_dataset\x18\x01 \x01(\x0b2J.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.TrainingDataset\x12\x93\x01\n)training_prediction_skew_detection_config\x18\x02 \x01(\x0b2`.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.TrainingPredictionSkewDetectionConfig\x12\x84\x01\n!prediction_drift_detection_config\x18\x03 \x01(\x0b2Y.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.PredictionDriftDetectionConfig\x12h\n\x12explanation_config\x18\x05 \x01(\x0b2L.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.ExplanationConfig\x1a\xdb\x02\n\x0fTrainingDataset\x129\n\x07dataset\x18\x03 \x01(\tB&\xfaA#\n!aiplatform.googleapis.com/DatasetH\x00\x12;\n\ngcs_source\x18\x04 \x01(\x0b2%.google.cloud.aiplatform.v1.GcsSourceH\x00\x12E\n\x0fbigquery_source\x18\x05 \x01(\x0b2*.google.cloud.aiplatform.v1.BigQuerySourceH\x00\x12\x13\n\x0bdata_format\x18\x02 \x01(\t\x12\x14\n\x0ctarget_field\x18\x06 \x01(\t\x12O\n\x19logging_sampling_strategy\x18\x07 \x01(\x0b2,.google.cloud.aiplatform.v1.SamplingStrategyB\r\n\x0bdata_source\x1a\x8f\x05\n%TrainingPredictionSkewDetectionConfig\x12\x8d\x01\n\x0fskew_thresholds\x18\x01 \x03(\x0b2t.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.TrainingPredictionSkewDetectionConfig.SkewThresholdsEntry\x12\xb0\x01\n!attribution_score_skew_thresholds\x18\x02 \x03(\x0b2\x84\x01.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.TrainingPredictionSkewDetectionConfig.AttributionScoreSkewThresholdsEntry\x12K\n\x16default_skew_threshold\x18\x06 \x01(\x0b2+.google.cloud.aiplatform.v1.ThresholdConfig\x1ab\n\x13SkewThresholdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ThresholdConfig:\x028\x01\x1ar\n#AttributionScoreSkewThresholdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ThresholdConfig:\x028\x01\x1a\x80\x05\n\x1ePredictionDriftDetectionConfig\x12\x88\x01\n\x10drift_thresholds\x18\x01 \x03(\x0b2n.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.PredictionDriftDetectionConfig.DriftThresholdsEntry\x12\xaa\x01\n"attribution_score_drift_thresholds\x18\x02 \x03(\x0b2~.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.PredictionDriftDetectionConfig.AttributionScoreDriftThresholdsEntry\x12L\n\x17default_drift_threshold\x18\x05 \x01(\x0b2+.google.cloud.aiplatform.v1.ThresholdConfig\x1ac\n\x14DriftThresholdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ThresholdConfig:\x028\x01\x1as\n$AttributionScoreDriftThresholdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ThresholdConfig:\x028\x01\x1a\xbc\x04\n\x11ExplanationConfig\x12!\n\x19enable_feature_attributes\x18\x01 \x01(\x08\x12~\n\x14explanation_baseline\x18\x02 \x01(\x0b2`.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline\x1a\x83\x03\n\x13ExplanationBaseline\x129\n\x03gcs\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1.GcsDestinationH\x00\x12C\n\x08bigquery\x18\x03 \x01(\x0b2/.google.cloud.aiplatform.v1.BigQueryDestinationH\x00\x12\x8c\x01\n\x11prediction_format\x18\x01 \x01(\x0e2q.google.cloud.aiplatform.v1.ModelMonitoringObjectiveConfig.ExplanationConfig.ExplanationBaseline.PredictionFormat"N\n\x10PredictionFormat\x12!\n\x1dPREDICTION_FORMAT_UNSPECIFIED\x10\x00\x12\t\n\x05JSONL\x10\x02\x12\x0c\n\x08BIGQUERY\x10\x03B\r\n\x0bdestination"\xa0\x02\n\x1aModelMonitoringAlertConfig\x12e\n\x12email_alert_config\x18\x01 \x01(\x0b2G.google.cloud.aiplatform.v1.ModelMonitoringAlertConfig.EmailAlertConfigH\x00\x12\x16\n\x0eenable_logging\x18\x02 \x01(\x08\x12Q\n\x15notification_channels\x18\x03 \x03(\tB2\xfaA/\n-monitoring.googleapis.com/NotificationChannel\x1a\'\n\x10EmailAlertConfig\x12\x13\n\x0buser_emails\x18\x01 \x03(\tB\x07\n\x05alert"/\n\x0fThresholdConfig\x12\x0f\n\x05value\x18\x01 \x01(\x01H\x00B\x0b\n\tthreshold"\x9c\x01\n\x10SamplingStrategy\x12]\n\x14random_sample_config\x18\x01 \x01(\x0b2?.google.cloud.aiplatform.v1.SamplingStrategy.RandomSampleConfig\x1a)\n\x12RandomSampleConfig\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x01B\xc4\x02\n\x1ecom.google.cloud.aiplatform.v1B\x14ModelMonitoringProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAo\n-monitoring.googleapis.com/NotificationChannel\x12>projects/{project}/notificationChannels/{notification_channel}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.model_monitoring_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14ModelMonitoringProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAo\n-monitoring.googleapis.com/NotificationChannel\x12>projects/{project}/notificationChannels/{notification_channel}'
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGDATASET'].fields_by_name['dataset']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGDATASET'].fields_by_name['dataset']._serialized_options = b'\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_SKEWTHRESHOLDSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_SKEWTHRESHOLDSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_ATTRIBUTIONSCORESKEWTHRESHOLDSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_ATTRIBUTIONSCORESKEWTHRESHOLDSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_DRIFTTHRESHOLDSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_DRIFTTHRESHOLDSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_ATTRIBUTIONSCOREDRIFTTHRESHOLDSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_ATTRIBUTIONSCOREDRIFTTHRESHOLDSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGALERTCONFIG'].fields_by_name['notification_channels']._loaded_options = None
    _globals['_MODELMONITORINGALERTCONFIG'].fields_by_name['notification_channels']._serialized_options = b'\xfaA/\n-monitoring.googleapis.com/NotificationChannel'
    _globals['_MODELMONITORINGOBJECTIVECONFIG']._serialized_start = 146
    _globals['_MODELMONITORINGOBJECTIVECONFIG']._serialized_end = 2897
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGDATASET']._serialized_start = 674
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGDATASET']._serialized_end = 1021
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG']._serialized_start = 1024
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG']._serialized_end = 1679
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_SKEWTHRESHOLDSENTRY']._serialized_start = 1465
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_SKEWTHRESHOLDSENTRY']._serialized_end = 1563
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_ATTRIBUTIONSCORESKEWTHRESHOLDSENTRY']._serialized_start = 1565
    _globals['_MODELMONITORINGOBJECTIVECONFIG_TRAININGPREDICTIONSKEWDETECTIONCONFIG_ATTRIBUTIONSCORESKEWTHRESHOLDSENTRY']._serialized_end = 1679
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG']._serialized_start = 1682
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG']._serialized_end = 2322
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_DRIFTTHRESHOLDSENTRY']._serialized_start = 2106
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_DRIFTTHRESHOLDSENTRY']._serialized_end = 2205
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_ATTRIBUTIONSCOREDRIFTTHRESHOLDSENTRY']._serialized_start = 2207
    _globals['_MODELMONITORINGOBJECTIVECONFIG_PREDICTIONDRIFTDETECTIONCONFIG_ATTRIBUTIONSCOREDRIFTTHRESHOLDSENTRY']._serialized_end = 2322
    _globals['_MODELMONITORINGOBJECTIVECONFIG_EXPLANATIONCONFIG']._serialized_start = 2325
    _globals['_MODELMONITORINGOBJECTIVECONFIG_EXPLANATIONCONFIG']._serialized_end = 2897
    _globals['_MODELMONITORINGOBJECTIVECONFIG_EXPLANATIONCONFIG_EXPLANATIONBASELINE']._serialized_start = 2510
    _globals['_MODELMONITORINGOBJECTIVECONFIG_EXPLANATIONCONFIG_EXPLANATIONBASELINE']._serialized_end = 2897
    _globals['_MODELMONITORINGOBJECTIVECONFIG_EXPLANATIONCONFIG_EXPLANATIONBASELINE_PREDICTIONFORMAT']._serialized_start = 2804
    _globals['_MODELMONITORINGOBJECTIVECONFIG_EXPLANATIONCONFIG_EXPLANATIONBASELINE_PREDICTIONFORMAT']._serialized_end = 2882
    _globals['_MODELMONITORINGALERTCONFIG']._serialized_start = 2900
    _globals['_MODELMONITORINGALERTCONFIG']._serialized_end = 3188
    _globals['_MODELMONITORINGALERTCONFIG_EMAILALERTCONFIG']._serialized_start = 3140
    _globals['_MODELMONITORINGALERTCONFIG_EMAILALERTCONFIG']._serialized_end = 3179
    _globals['_THRESHOLDCONFIG']._serialized_start = 3190
    _globals['_THRESHOLDCONFIG']._serialized_end = 3237
    _globals['_SAMPLINGSTRATEGY']._serialized_start = 3240
    _globals['_SAMPLINGSTRATEGY']._serialized_end = 3396
    _globals['_SAMPLINGSTRATEGY_RANDOMSAMPLECONFIG']._serialized_start = 3355
    _globals['_SAMPLINGSTRATEGY_RANDOMSAMPLECONFIG']._serialized_end = 3396