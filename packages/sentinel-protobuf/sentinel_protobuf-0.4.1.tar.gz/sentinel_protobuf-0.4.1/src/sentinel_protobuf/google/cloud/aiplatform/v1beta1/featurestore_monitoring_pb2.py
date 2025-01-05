"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/featurestore_monitoring.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/aiplatform/v1beta1/featurestore_monitoring.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1egoogle/protobuf/duration.proto"\x85\t\n\x1cFeaturestoreMonitoringConfig\x12i\n\x11snapshot_analysis\x18\x01 \x01(\x0b2N.google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfig.SnapshotAnalysis\x12v\n\x18import_features_analysis\x18\x02 \x01(\x0b2T.google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfig.ImportFeaturesAnalysis\x12q\n\x1anumerical_threshold_config\x18\x03 \x01(\x0b2M.google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfig.ThresholdConfig\x12s\n\x1ccategorical_threshold_config\x18\x04 \x01(\x0b2M.google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfig.ThresholdConfig\x1a\x9a\x01\n\x10SnapshotAnalysis\x12\x10\n\x08disabled\x18\x01 \x01(\x08\x12:\n\x13monitoring_interval\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x02\x18\x01\x12 \n\x18monitoring_interval_days\x18\x03 \x01(\x05\x12\x16\n\x0estaleness_days\x18\x04 \x01(\x05\x1a\xcb\x03\n\x16ImportFeaturesAnalysis\x12i\n\x05state\x18\x01 \x01(\x0e2Z.google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State\x12\x81\x01\n\x1aanomaly_detection_baseline\x18\x02 \x01(\x0e2].google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\x0b\n\x07ENABLED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03"z\n\x08Baseline\x12\x18\n\x14BASELINE_UNSPECIFIED\x10\x00\x12\x10\n\x0cLATEST_STATS\x10\x01\x12\x1e\n\x1aMOST_RECENT_SNAPSHOT_STATS\x10\x02\x12"\n\x1ePREVIOUS_IMPORT_FEATURES_STATS\x10\x03\x1a/\n\x0fThresholdConfig\x12\x0f\n\x05value\x18\x01 \x01(\x01H\x00B\x0b\n\tthresholdB\xf2\x01\n#com.google.cloud.aiplatform.v1beta1B\x1bFeaturestoreMonitoringProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.featurestore_monitoring_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1bFeaturestoreMonitoringProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FEATURESTOREMONITORINGCONFIG_SNAPSHOTANALYSIS'].fields_by_name['monitoring_interval']._loaded_options = None
    _globals['_FEATURESTOREMONITORINGCONFIG_SNAPSHOTANALYSIS'].fields_by_name['monitoring_interval']._serialized_options = b'\x18\x01'
    _globals['_FEATURESTOREMONITORINGCONFIG']._serialized_start = 131
    _globals['_FEATURESTOREMONITORINGCONFIG']._serialized_end = 1288
    _globals['_FEATURESTOREMONITORINGCONFIG_SNAPSHOTANALYSIS']._serialized_start = 623
    _globals['_FEATURESTOREMONITORINGCONFIG_SNAPSHOTANALYSIS']._serialized_end = 777
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS']._serialized_start = 780
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS']._serialized_end = 1239
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_STATE']._serialized_start = 1045
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_STATE']._serialized_end = 1115
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_BASELINE']._serialized_start = 1117
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_BASELINE']._serialized_end = 1239
    _globals['_FEATURESTOREMONITORINGCONFIG_THRESHOLDCONFIG']._serialized_start = 1241
    _globals['_FEATURESTOREMONITORINGCONFIG_THRESHOLDCONFIG']._serialized_end = 1288