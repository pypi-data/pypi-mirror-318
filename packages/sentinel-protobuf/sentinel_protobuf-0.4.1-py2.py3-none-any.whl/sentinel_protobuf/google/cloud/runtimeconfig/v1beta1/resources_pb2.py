"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/runtimeconfig/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/runtimeconfig/v1beta1/resources.proto\x12"google.cloud.runtimeconfig.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"2\n\rRuntimeConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t"\xb8\x01\n\x08Variable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x05value\x18\x02 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x05 \x01(\tH\x00\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\x05state\x18\x04 \x01(\x0e21.google.cloud.runtimeconfig.v1beta1.VariableStateB\n\n\x08contents"\x9d\x01\n\x0cEndCondition\x12S\n\x0bcardinality\x18\x01 \x01(\x0b2<.google.cloud.runtimeconfig.v1beta1.EndCondition.CardinalityH\x00\x1a+\n\x0bCardinality\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05B\x0b\n\tcondition"\xaa\x02\n\x06Waiter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x07timeout\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12A\n\x07failure\x18\x03 \x01(\x0b20.google.cloud.runtimeconfig.v1beta1.EndCondition\x12A\n\x07success\x18\x04 \x01(\x0b20.google.cloud.runtimeconfig.v1beta1.EndCondition\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04done\x18\x06 \x01(\x08\x12!\n\x05error\x18\x07 \x01(\x0b2\x12.google.rpc.Status*I\n\rVariableState\x12\x1e\n\x1aVARIABLE_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07UPDATED\x10\x01\x12\x0b\n\x07DELETED\x10\x02B\xc2\x01\n&com.google.cloud.runtimeconfig.v1beta1P\x01ZLcloud.google.com/go/runtimeconfig/apiv1beta1/runtimeconfigpb;runtimeconfigpb\xaa\x02"Google.Cloud.RuntimeConfig.V1Beta1\xca\x02"Google\\Cloud\\RuntimeConfig\\V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.runtimeconfig.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.runtimeconfig.v1beta1P\x01ZLcloud.google.com/go/runtimeconfig/apiv1beta1/runtimeconfigpb;runtimeconfigpb\xaa\x02"Google.Cloud.RuntimeConfig.V1Beta1\xca\x02"Google\\Cloud\\RuntimeConfig\\V1beta1'
    _globals['_VARIABLESTATE']._serialized_start = 910
    _globals['_VARIABLESTATE']._serialized_end = 983
    _globals['_RUNTIMECONFIG']._serialized_start = 210
    _globals['_RUNTIMECONFIG']._serialized_end = 260
    _globals['_VARIABLE']._serialized_start = 263
    _globals['_VARIABLE']._serialized_end = 447
    _globals['_ENDCONDITION']._serialized_start = 450
    _globals['_ENDCONDITION']._serialized_end = 607
    _globals['_ENDCONDITION_CARDINALITY']._serialized_start = 551
    _globals['_ENDCONDITION_CARDINALITY']._serialized_end = 594
    _globals['_WAITER']._serialized_start = 610
    _globals['_WAITER']._serialized_end = 908