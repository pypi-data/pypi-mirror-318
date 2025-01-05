"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/dropped_labels.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/monitoring/v3/dropped_labels.proto\x12\x14google.monitoring.v3"|\n\rDroppedLabels\x12=\n\x05label\x18\x01 \x03(\x0b2..google.monitoring.v3.DroppedLabels.LabelEntry\x1a,\n\nLabelEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\xcd\x01\n\x18com.google.monitoring.v3B\x12DroppedLabelsProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.dropped_labels_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x12DroppedLabelsProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_DROPPEDLABELS_LABELENTRY']._loaded_options = None
    _globals['_DROPPEDLABELS_LABELENTRY']._serialized_options = b'8\x01'
    _globals['_DROPPEDLABELS']._serialized_start = 67
    _globals['_DROPPEDLABELS']._serialized_end = 191
    _globals['_DROPPEDLABELS_LABELENTRY']._serialized_start = 147
    _globals['_DROPPEDLABELS_LABELENTRY']._serialized_end = 191