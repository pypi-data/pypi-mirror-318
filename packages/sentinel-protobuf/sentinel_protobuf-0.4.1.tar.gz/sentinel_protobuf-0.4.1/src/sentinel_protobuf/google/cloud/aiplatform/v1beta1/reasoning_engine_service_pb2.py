"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/reasoning_engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import reasoning_engine_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_reasoning__engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/aiplatform/v1beta1/reasoning_engine_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a6google/cloud/aiplatform/v1beta1/reasoning_engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xaa\x01\n\x1cCreateReasoningEngineRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12O\n\x10reasoning_engine\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ReasoningEngineB\x03\xe0A\x02"}\n&CreateReasoningEngineOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\\\n\x19GetReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine"\xa5\x01\n\x1cUpdateReasoningEngineRequest\x12O\n\x10reasoning_engine\x18\x01 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ReasoningEngineB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"}\n&UpdateReasoningEngineOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x9e\x01\n\x1bListReasoningEnginesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"\x84\x01\n\x1cListReasoningEnginesResponse\x12K\n\x11reasoning_engines\x18\x01 \x03(\x0b20.google.cloud.aiplatform.v1beta1.ReasoningEngine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"_\n\x1cDeleteReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine2\xeb\n\n\x16ReasoningEngineService\x12\xa1\x02\n\x15CreateReasoningEngine\x12=.google.cloud.aiplatform.v1beta1.CreateReasoningEngineRequest\x1a\x1d.google.longrunning.Operation"\xa9\x01\xcaA9\n\x0fReasoningEngine\x12&CreateReasoningEngineOperationMetadata\xdaA\x17parent,reasoning_engine\x82\xd3\xe4\x93\x02M"9/v1beta1/{parent=projects/*/locations/*}/reasoningEngines:\x10reasoning_engine\x12\xcc\x01\n\x12GetReasoningEngine\x12:.google.cloud.aiplatform.v1beta1.GetReasoningEngineRequest\x1a0.google.cloud.aiplatform.v1beta1.ReasoningEngine"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}\x12\xdf\x01\n\x14ListReasoningEngines\x12<.google.cloud.aiplatform.v1beta1.ListReasoningEnginesRequest\x1a=.google.cloud.aiplatform.v1beta1.ListReasoningEnginesResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1beta1/{parent=projects/*/locations/*}/reasoningEngines\x12\xb7\x02\n\x15UpdateReasoningEngine\x12=.google.cloud.aiplatform.v1beta1.UpdateReasoningEngineRequest\x1a\x1d.google.longrunning.Operation"\xbf\x01\xcaA9\n\x0fReasoningEngine\x12&UpdateReasoningEngineOperationMetadata\xdaA\x1creasoning_engine,update_mask\x82\xd3\xe4\x93\x02^2J/v1beta1/{reasoning_engine.name=projects/*/locations/*/reasoningEngines/*}:\x10reasoning_engine\x12\xf2\x01\n\x15DeleteReasoningEngine\x12=.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRequest\x1a\x1d.google.longrunning.Operation"{\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf2\x01\n#com.google.cloud.aiplatform.v1beta1B\x1bReasoningEngineServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.reasoning_engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1bReasoningEngineServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._loaded_options = None
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._serialized_options = b'\xe0A\x02'
    _globals['_GETREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._loaded_options = None
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_REASONINGENGINESERVICE']._loaded_options = None
    _globals['_REASONINGENGINESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['CreateReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['CreateReasoningEngine']._serialized_options = b'\xcaA9\n\x0fReasoningEngine\x12&CreateReasoningEngineOperationMetadata\xdaA\x17parent,reasoning_engine\x82\xd3\xe4\x93\x02M"9/v1beta1/{parent=projects/*/locations/*}/reasoningEngines:\x10reasoning_engine'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['GetReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['GetReasoningEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['ListReasoningEngines']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['ListReasoningEngines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1beta1/{parent=projects/*/locations/*}/reasoningEngines'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['UpdateReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['UpdateReasoningEngine']._serialized_options = b'\xcaA9\n\x0fReasoningEngine\x12&UpdateReasoningEngineOperationMetadata\xdaA\x1creasoning_engine,update_mask\x82\xd3\xe4\x93\x02^2J/v1beta1/{reasoning_engine.name=projects/*/locations/*/reasoningEngines/*}:\x10reasoning_engine'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['DeleteReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['DeleteReasoningEngine']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}'
    _globals['_CREATEREASONINGENGINEREQUEST']._serialized_start = 420
    _globals['_CREATEREASONINGENGINEREQUEST']._serialized_end = 590
    _globals['_CREATEREASONINGENGINEOPERATIONMETADATA']._serialized_start = 592
    _globals['_CREATEREASONINGENGINEOPERATIONMETADATA']._serialized_end = 717
    _globals['_GETREASONINGENGINEREQUEST']._serialized_start = 719
    _globals['_GETREASONINGENGINEREQUEST']._serialized_end = 811
    _globals['_UPDATEREASONINGENGINEREQUEST']._serialized_start = 814
    _globals['_UPDATEREASONINGENGINEREQUEST']._serialized_end = 979
    _globals['_UPDATEREASONINGENGINEOPERATIONMETADATA']._serialized_start = 981
    _globals['_UPDATEREASONINGENGINEOPERATIONMETADATA']._serialized_end = 1106
    _globals['_LISTREASONINGENGINESREQUEST']._serialized_start = 1109
    _globals['_LISTREASONINGENGINESREQUEST']._serialized_end = 1267
    _globals['_LISTREASONINGENGINESRESPONSE']._serialized_start = 1270
    _globals['_LISTREASONINGENGINESRESPONSE']._serialized_end = 1402
    _globals['_DELETEREASONINGENGINEREQUEST']._serialized_start = 1404
    _globals['_DELETEREASONINGENGINEREQUEST']._serialized_end = 1499
    _globals['_REASONINGENGINESERVICE']._serialized_start = 1502
    _globals['_REASONINGENGINESERVICE']._serialized_end = 2889