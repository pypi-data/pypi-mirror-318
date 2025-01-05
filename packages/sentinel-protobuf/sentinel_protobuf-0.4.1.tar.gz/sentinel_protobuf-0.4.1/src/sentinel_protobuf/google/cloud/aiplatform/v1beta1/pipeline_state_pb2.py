"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/pipeline_state.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1beta1/pipeline_state.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1*\x93\x02\n\rPipelineState\x12\x1e\n\x1aPIPELINE_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15PIPELINE_STATE_QUEUED\x10\x01\x12\x1a\n\x16PIPELINE_STATE_PENDING\x10\x02\x12\x1a\n\x16PIPELINE_STATE_RUNNING\x10\x03\x12\x1c\n\x18PIPELINE_STATE_SUCCEEDED\x10\x04\x12\x19\n\x15PIPELINE_STATE_FAILED\x10\x05\x12\x1d\n\x19PIPELINE_STATE_CANCELLING\x10\x06\x12\x1c\n\x18PIPELINE_STATE_CANCELLED\x10\x07\x12\x19\n\x15PIPELINE_STATE_PAUSED\x10\x08B\xe9\x01\n#com.google.cloud.aiplatform.v1beta1B\x12PipelineStateProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.pipeline_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x12PipelineStateProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_PIPELINESTATE']._serialized_start = 90
    _globals['_PIPELINESTATE']._serialized_end = 365