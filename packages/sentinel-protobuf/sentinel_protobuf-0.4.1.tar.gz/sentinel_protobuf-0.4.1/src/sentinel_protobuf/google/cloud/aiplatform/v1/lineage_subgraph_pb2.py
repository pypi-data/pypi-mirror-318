"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/lineage_subgraph.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.aiplatform.v1 import artifact_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_artifact__pb2
from .....google.cloud.aiplatform.v1 import event_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_event__pb2
from .....google.cloud.aiplatform.v1 import execution_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_execution__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1/lineage_subgraph.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a)google/cloud/aiplatform/v1/artifact.proto\x1a&google/cloud/aiplatform/v1/event.proto\x1a*google/cloud/aiplatform/v1/execution.proto"\xb8\x01\n\x0fLineageSubgraph\x127\n\tartifacts\x18\x01 \x03(\x0b2$.google.cloud.aiplatform.v1.Artifact\x129\n\nexecutions\x18\x02 \x03(\x0b2%.google.cloud.aiplatform.v1.Execution\x121\n\x06events\x18\x03 \x03(\x0b2!.google.cloud.aiplatform.v1.EventB\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14LineageSubgraphProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.lineage_subgraph_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14LineageSubgraphProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_LINEAGESUBGRAPH']._serialized_start = 209
    _globals['_LINEAGESUBGRAPH']._serialized_end = 393