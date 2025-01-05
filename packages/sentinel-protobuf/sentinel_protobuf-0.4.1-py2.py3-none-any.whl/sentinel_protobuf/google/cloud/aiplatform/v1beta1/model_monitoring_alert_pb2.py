"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/model_monitoring_alert.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/aiplatform/v1beta1/model_monitoring_alert.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"A\n\x1dModelMonitoringAlertCondition\x12\x13\n\tthreshold\x18\x01 \x01(\x01H\x00B\x0b\n\tcondition"\x9e\x03\n\x16ModelMonitoringAnomaly\x12a\n\x0ftabular_anomaly\x18\x01 \x01(\x0b2F.google.cloud.aiplatform.v1beta1.ModelMonitoringAnomaly.TabularAnomalyH\x00\x12\x1c\n\x14model_monitoring_job\x18\x02 \x01(\t\x12\x11\n\talgorithm\x18\x03 \x01(\t\x1a\xe4\x01\n\x0eTabularAnomaly\x12\x13\n\x0banomaly_uri\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\'\n\x07anomaly\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x120\n\x0ctrigger_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12Q\n\tcondition\x18\x05 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertConditionB\t\n\x07anomaly"\xbc\x01\n\x14ModelMonitoringAlert\x12\x12\n\nstats_name\x18\x01 \x01(\t\x12\x16\n\x0eobjective_type\x18\x02 \x01(\t\x12.\n\nalert_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12H\n\x07anomaly\x18\x04 \x01(\x0b27.google.cloud.aiplatform.v1beta1.ModelMonitoringAnomalyB\xf0\x01\n#com.google.cloud.aiplatform.v1beta1B\x19ModelMonitoringAlertProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_monitoring_alert_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x19ModelMonitoringAlertProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELMONITORINGALERTCONDITION']._serialized_start = 160
    _globals['_MODELMONITORINGALERTCONDITION']._serialized_end = 225
    _globals['_MODELMONITORINGANOMALY']._serialized_start = 228
    _globals['_MODELMONITORINGANOMALY']._serialized_end = 642
    _globals['_MODELMONITORINGANOMALY_TABULARANOMALY']._serialized_start = 403
    _globals['_MODELMONITORINGANOMALY_TABULARANOMALY']._serialized_end = 631
    _globals['_MODELMONITORINGALERT']._serialized_start = 645
    _globals['_MODELMONITORINGALERT']._serialized_end = 833