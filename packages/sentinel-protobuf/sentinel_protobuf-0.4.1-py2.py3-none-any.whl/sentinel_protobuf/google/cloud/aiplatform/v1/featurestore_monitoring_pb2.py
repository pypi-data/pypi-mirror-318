"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/featurestore_monitoring.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1/featurestore_monitoring.proto\x12\x1agoogle.cloud.aiplatform.v1"\xa9\x08\n\x1cFeaturestoreMonitoringConfig\x12d\n\x11snapshot_analysis\x18\x01 \x01(\x0b2I.google.cloud.aiplatform.v1.FeaturestoreMonitoringConfig.SnapshotAnalysis\x12q\n\x18import_features_analysis\x18\x02 \x01(\x0b2O.google.cloud.aiplatform.v1.FeaturestoreMonitoringConfig.ImportFeaturesAnalysis\x12l\n\x1anumerical_threshold_config\x18\x03 \x01(\x0b2H.google.cloud.aiplatform.v1.FeaturestoreMonitoringConfig.ThresholdConfig\x12n\n\x1ccategorical_threshold_config\x18\x04 \x01(\x0b2H.google.cloud.aiplatform.v1.FeaturestoreMonitoringConfig.ThresholdConfig\x1a^\n\x10SnapshotAnalysis\x12\x10\n\x08disabled\x18\x01 \x01(\x08\x12 \n\x18monitoring_interval_days\x18\x03 \x01(\x05\x12\x16\n\x0estaleness_days\x18\x04 \x01(\x05\x1a\xc0\x03\n\x16ImportFeaturesAnalysis\x12d\n\x05state\x18\x01 \x01(\x0e2U.google.cloud.aiplatform.v1.FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.State\x12|\n\x1aanomaly_detection_baseline\x18\x02 \x01(\x0e2X.google.cloud.aiplatform.v1.FeaturestoreMonitoringConfig.ImportFeaturesAnalysis.Baseline"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\x0b\n\x07ENABLED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03"z\n\x08Baseline\x12\x18\n\x14BASELINE_UNSPECIFIED\x10\x00\x12\x10\n\x0cLATEST_STATS\x10\x01\x12\x1e\n\x1aMOST_RECENT_SNAPSHOT_STATS\x10\x02\x12"\n\x1ePREVIOUS_IMPORT_FEATURES_STATS\x10\x03\x1a/\n\x0fThresholdConfig\x12\x0f\n\x05value\x18\x01 \x01(\x01H\x00B\x0b\n\tthresholdB\xd9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1bFeaturestoreMonitoringProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.featurestore_monitoring_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1bFeaturestoreMonitoringProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_FEATURESTOREMONITORINGCONFIG']._serialized_start = 89
    _globals['_FEATURESTOREMONITORINGCONFIG']._serialized_end = 1154
    _globals['_FEATURESTOREMONITORINGCONFIG_SNAPSHOTANALYSIS']._serialized_start = 560
    _globals['_FEATURESTOREMONITORINGCONFIG_SNAPSHOTANALYSIS']._serialized_end = 654
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS']._serialized_start = 657
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS']._serialized_end = 1105
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_STATE']._serialized_start = 911
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_STATE']._serialized_end = 981
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_BASELINE']._serialized_start = 983
    _globals['_FEATURESTOREMONITORINGCONFIG_IMPORTFEATURESANALYSIS_BASELINE']._serialized_end = 1105
    _globals['_FEATURESTOREMONITORINGCONFIG_THRESHOLDCONFIG']._serialized_start = 1107
    _globals['_FEATURESTOREMONITORINGCONFIG_THRESHOLDCONFIG']._serialized_end = 1154