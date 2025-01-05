"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/logging/reconciler_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dataproc/logging/reconciler_log.proto\x12\x1dgoogle.cloud.dataproc.logging\x1a\x1egoogle/protobuf/duration.proto"\xe0\x03\n\x11ReconciliationLog\x12G\n\x06inputs\x18\x01 \x01(\x0b27.google.cloud.dataproc.logging.ReconciliationLog.Inputs\x12I\n\x07outputs\x18\x02 \x01(\x0b28.google.cloud.dataproc.logging.ReconciliationLog.Outputs\x1a\xc4\x01\n\x06Inputs\x120\n\ridle_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12+\n\x08idle_ttl\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x123\n\x10session_lifetime\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12&\n\x03ttl\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x1ap\n\x07Outputs\x12K\n\x08decision\x18\x01 \x01(\x0e29.google.cloud.dataproc.logging.ReconciliationDecisionType\x12\x18\n\x10decision_details\x18\x02 \x01(\t"\xb6\x01\n\x1cReconciliationClusterHealLog\x12T\n\x07outputs\x18\x01 \x01(\x0b2C.google.cloud.dataproc.logging.ReconciliationClusterHealLog.Outputs\x1a@\n\x07Outputs\x12\x1b\n\x13repair_operation_id\x18\x01 \x01(\t\x12\x18\n\x10decision_details\x18\x02 \x01(\t*p\n\x1aReconciliationDecisionType\x12,\n(RECONCILIATION_DECISION_TYPE_UNSPECIFIED\x10\x00\x12$\n RECONCILIATION_TERMINATE_SESSION\x10\x01B\x93\x01\n!com.google.cloud.dataproc.loggingB\x12ReconcilerLogProtoP\x01Z8cloud.google.com/go/dataproc/logging/loggingpb;loggingpb\xaa\x02\x1dGoogle.Cloud.Dataproc.Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.logging.reconciler_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dataproc.loggingB\x12ReconcilerLogProtoP\x01Z8cloud.google.com/go/dataproc/logging/loggingpb;loggingpb\xaa\x02\x1dGoogle.Cloud.Dataproc.Logging'
    _globals['_RECONCILIATIONDECISIONTYPE']._serialized_start = 785
    _globals['_RECONCILIATIONDECISIONTYPE']._serialized_end = 897
    _globals['_RECONCILIATIONLOG']._serialized_start = 118
    _globals['_RECONCILIATIONLOG']._serialized_end = 598
    _globals['_RECONCILIATIONLOG_INPUTS']._serialized_start = 288
    _globals['_RECONCILIATIONLOG_INPUTS']._serialized_end = 484
    _globals['_RECONCILIATIONLOG_OUTPUTS']._serialized_start = 486
    _globals['_RECONCILIATIONLOG_OUTPUTS']._serialized_end = 598
    _globals['_RECONCILIATIONCLUSTERHEALLOG']._serialized_start = 601
    _globals['_RECONCILIATIONCLUSTERHEALLOG']._serialized_end = 783
    _globals['_RECONCILIATIONCLUSTERHEALLOG_OUTPUTS']._serialized_start = 719
    _globals['_RECONCILIATIONCLUSTERHEALLOG_OUTPUTS']._serialized_end = 783