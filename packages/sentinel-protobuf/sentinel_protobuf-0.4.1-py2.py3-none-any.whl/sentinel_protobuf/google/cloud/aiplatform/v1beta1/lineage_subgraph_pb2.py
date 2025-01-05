"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/lineage_subgraph.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.aiplatform.v1beta1 import artifact_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_artifact__pb2
from .....google.cloud.aiplatform.v1beta1 import event_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_event__pb2
from .....google.cloud.aiplatform.v1beta1 import execution_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_execution__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/lineage_subgraph.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a.google/cloud/aiplatform/v1beta1/artifact.proto\x1a+google/cloud/aiplatform/v1beta1/event.proto\x1a/google/cloud/aiplatform/v1beta1/execution.proto"\xc7\x01\n\x0fLineageSubgraph\x12<\n\tartifacts\x18\x01 \x03(\x0b2).google.cloud.aiplatform.v1beta1.Artifact\x12>\n\nexecutions\x18\x02 \x03(\x0b2*.google.cloud.aiplatform.v1beta1.Execution\x126\n\x06events\x18\x03 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.EventB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14LineageSubgraphProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.lineage_subgraph_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14LineageSubgraphProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_LINEAGESUBGRAPH']._serialized_start = 234
    _globals['_LINEAGESUBGRAPH']._serialized_end = 433