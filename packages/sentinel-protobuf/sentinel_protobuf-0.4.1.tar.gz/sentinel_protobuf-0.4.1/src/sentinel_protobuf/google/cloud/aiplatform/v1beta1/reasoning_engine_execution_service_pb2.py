"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/reasoning_engine_execution_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/cloud/aiplatform/v1beta1/reasoning_engine_execution_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa6\x01\n\x1bQueryReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12+\n\x05input\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x19\n\x0cclass_method\x18\x03 \x01(\tB\x03\xe0A\x01"F\n\x1cQueryReasoningEngineResponse\x12&\n\x06output\x18\x01 \x01(\x0b2\x16.google.protobuf.Value"\xac\x01\n!StreamQueryReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12+\n\x05input\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x19\n\x0cclass_method\x18\x03 \x01(\tB\x03\xe0A\x012\x9f\x04\n\x1fReasoningEngineExecutionService\x12\xdf\x01\n\x14QueryReasoningEngine\x12<.google.cloud.aiplatform.v1beta1.QueryReasoningEngineRequest\x1a=.google.cloud.aiplatform.v1beta1.QueryReasoningEngineResponse"J\x82\xd3\xe4\x93\x02D"?/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}:query:\x01*\x12\xca\x01\n\x1aStreamQueryReasoningEngine\x12B.google.cloud.aiplatform.v1beta1.StreamQueryReasoningEngineRequest\x1a\x14.google.api.HttpBody"P\x82\xd3\xe4\x93\x02J"E/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}:streamQuery:\x01*0\x01\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfb\x01\n#com.google.cloud.aiplatform.v1beta1B$ReasoningEngineExecutionServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.reasoning_engine_execution_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B$ReasoningEngineExecutionServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._loaded_options = None
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._loaded_options = None
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._loaded_options = None
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['QueryReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['QueryReasoningEngine']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}:query:\x01*'
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['StreamQueryReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['StreamQueryReasoningEngine']._serialized_options = b'\x82\xd3\xe4\x93\x02J"E/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}:streamQuery:\x01*'
    _globals['_QUERYREASONINGENGINEREQUEST']._serialized_start = 282
    _globals['_QUERYREASONINGENGINEREQUEST']._serialized_end = 448
    _globals['_QUERYREASONINGENGINERESPONSE']._serialized_start = 450
    _globals['_QUERYREASONINGENGINERESPONSE']._serialized_end = 520
    _globals['_STREAMQUERYREASONINGENGINEREQUEST']._serialized_start = 523
    _globals['_STREAMQUERYREASONINGENGINEREQUEST']._serialized_end = 695
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._serialized_start = 698
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._serialized_end = 1241