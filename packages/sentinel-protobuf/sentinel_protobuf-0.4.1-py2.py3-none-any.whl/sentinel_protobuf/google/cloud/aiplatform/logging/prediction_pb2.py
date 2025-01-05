"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/logging/prediction.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/aiplatform/logging/prediction.proto\x12\x1fgoogle.cloud.aiplatform.logging\x1a\x17google/rpc/status.proto"\x9c\x01\n\x18OnlinePredictionLogEntry\x12\x10\n\x08endpoint\x18\x01 \x01(\t\x12\x19\n\x11deployed_model_id\x18\x02 \x01(\t\x12\x16\n\x0einstance_count\x18\x03 \x01(\x03\x12\x18\n\x10prediction_count\x18\x04 \x01(\x03\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.StatusBt\n#com.google.cloud.aiplatform.loggingB\x0fPredictionProtoP\x01Z:cloud.google.com/go/aiplatform/logging/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.logging.prediction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.loggingB\x0fPredictionProtoP\x01Z:cloud.google.com/go/aiplatform/logging/loggingpb;loggingpb'
    _globals['_ONLINEPREDICTIONLOGENTRY']._serialized_start = 111
    _globals['_ONLINEPREDICTIONLOGENTRY']._serialized_end = 267