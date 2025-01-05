"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/deployed_index_ref.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1beta1/deployed_index_ref.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x96\x01\n\x10DeployedIndexRef\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x05\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x1e\n\x11deployed_index_id\x18\x02 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x03B\xec\x01\n#com.google.cloud.aiplatform.v1beta1B\x15DeployedIndexRefProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.deployed_index_ref_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x15DeployedIndexRefProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_DEPLOYEDINDEXREF'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_DEPLOYEDINDEXREF'].fields_by_name['index_endpoint']._serialized_options = b"\xe0A\x05\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_DEPLOYEDINDEXREF'].fields_by_name['deployed_index_id']._loaded_options = None
    _globals['_DEPLOYEDINDEXREF'].fields_by_name['deployed_index_id']._serialized_options = b'\xe0A\x05'
    _globals['_DEPLOYEDINDEXREF'].fields_by_name['display_name']._loaded_options = None
    _globals['_DEPLOYEDINDEXREF'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDINDEXREF']._serialized_start = 154
    _globals['_DEPLOYEDINDEXREF']._serialized_end = 304