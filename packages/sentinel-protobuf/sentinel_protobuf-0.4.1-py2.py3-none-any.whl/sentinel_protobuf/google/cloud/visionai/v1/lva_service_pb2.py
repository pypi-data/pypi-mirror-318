"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1/lva_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.visionai.v1 import common_pb2 as google_dot_cloud_dot_visionai_dot_v1_dot_common__pb2
from .....google.cloud.visionai.v1 import lva_resources_pb2 as google_dot_cloud_dot_visionai_dot_v1_dot_lva__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/visionai/v1/lva_service.proto\x12\x18google.cloud.visionai.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a%google/cloud/visionai/v1/common.proto\x1a,google/cloud/visionai/v1/lva_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9a\x01\n\x14ListOperatorsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"|\n\x15ListOperatorsResponse\x125\n\toperators\x18\x01 \x03(\x0b2".google.cloud.visionai.v1.Operator\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x12GetOperatorRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Operator"\xc0\x01\n\x15CreateOperatorRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0boperator_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x08operator\x18\x03 \x01(\x0b2".google.cloud.visionai.v1.OperatorB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa1\x01\n\x15UpdateOperatorRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x129\n\x08operator\x18\x02 \x01(\x0b2".google.cloud.visionai.v1.OperatorB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"h\n\x15DeleteOperatorRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Operator\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x97\x01\n\x13ListAnalysesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"z\n\x14ListAnalysesResponse\x124\n\x08analyses\x18\x01 \x03(\x0b2".google.cloud.visionai.v1.Analysis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x12GetAnalysisRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis"\xbe\x01\n\x15CreateAnalysisRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x18\n\x0banalysis_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x08analysis\x18\x03 \x01(\x0b2".google.cloud.visionai.v1.AnalysisB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa1\x01\n\x15UpdateAnalysisRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x129\n\x08analysis\x18\x02 \x01(\x0b2".google.cloud.visionai.v1.AnalysisB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"h\n\x15DeleteAnalysisRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x98\x01\n\x14ListProcessesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"{\n\x15ListProcessesResponse\x124\n\tprocesses\x18\x01 \x03(\x0b2!.google.cloud.visionai.v1.Process\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"J\n\x11GetProcessRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Process"\xba\x01\n\x14CreateProcessRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x17\n\nprocess_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x07process\x18\x03 \x01(\x0b2!.google.cloud.visionai.v1.ProcessB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\x9e\x01\n\x14UpdateProcessRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x127\n\x07process\x18\x02 \x01(\x0b2!.google.cloud.visionai.v1.ProcessB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"f\n\x14DeleteProcessRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Process\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xd1\x02\n\x16BatchRunProcessRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12E\n\x08requests\x18\x02 \x03(\x0b2..google.cloud.visionai.v1.CreateProcessRequestB\x03\xe0A\x02\x12]\n\x07options\x18\x03 \x01(\x0b2G.google.cloud.visionai.v1.BatchRunProcessRequest.BatchRunProcessOptionsB\x03\xe0A\x01\x12\x15\n\x08batch_id\x18\x04 \x01(\tB\x03\xe0A\x03\x1aA\n\x16BatchRunProcessOptions\x12\x13\n\x0bretry_count\x18\x01 \x01(\x05\x12\x12\n\nbatch_size\x18\x02 \x01(\x05"a\n\x17BatchRunProcessResponse\x12\x10\n\x08batch_id\x18\x01 \x01(\t\x124\n\tprocesses\x18\x02 \x03(\x0b2!.google.cloud.visionai.v1.Process"\x96\x01\n\x1aResolveOperatorInfoRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12=\n\x07queries\x18\x02 \x03(\x0b2\'.google.cloud.visionai.v1.OperatorQueryB\x03\xe0A\x02"s\n\rOperatorQuery\x12\x15\n\x08operator\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03tag\x18\x02 \x01(\tB\x03\xe0A\x01\x129\n\x08registry\x18\x03 \x01(\x0e2".google.cloud.visionai.v1.RegistryB\x03\xe0A\x01"T\n\x1bResolveOperatorInfoResponse\x125\n\toperators\x18\x01 \x03(\x0b2".google.cloud.visionai.v1.Operator"\xa0\x01\n\x1aListPublicOperatorsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"m\n\x1bListPublicOperatorsResponse\x125\n\toperators\x18\x01 \x03(\x0b2".google.cloud.visionai.v1.Operator\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*=\n\x08Registry\x12\x18\n\x14REGISTRY_UNSPECIFIED\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x022\x8d\x1e\n\x12LiveVideoAnalytics\x12\xcc\x01\n\x13ListPublicOperators\x124.google.cloud.visionai.v1.ListPublicOperatorsRequest\x1a5.google.cloud.visionai.v1.ListPublicOperatorsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}:listPublicOperators\x12\xd7\x01\n\x13ResolveOperatorInfo\x124.google.cloud.visionai.v1.ResolveOperatorInfoRequest\x1a5.google.cloud.visionai.v1.ResolveOperatorInfoResponse"S\xdaA\x0eparent,queries\x82\xd3\xe4\x93\x02<"7/v1/{parent=projects/*/locations/*}:resolveOperatorInfo:\x01*\x12\xb0\x01\n\rListOperators\x12..google.cloud.visionai.v1.ListOperatorsRequest\x1a/.google.cloud.visionai.v1.ListOperatorsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/operators\x12\x9d\x01\n\x0bGetOperator\x12,.google.cloud.visionai.v1.GetOperatorRequest\x1a".google.cloud.visionai.v1.Operator"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/operators/*}\x12\xdf\x01\n\x0eCreateOperator\x12/.google.cloud.visionai.v1.CreateOperatorRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Operator\x12\x11OperationMetadata\xdaA\x1bparent,operator,operator_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/operators:\x08operator\x12\xe1\x01\n\x0eUpdateOperator\x12/.google.cloud.visionai.v1.UpdateOperatorRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1d\n\x08Operator\x12\x11OperationMetadata\xdaA\x14operator,update_mask\x82\xd3\xe4\x93\x02B26/v1/{operator.name=projects/*/locations/*/operators/*}:\x08operator\x12\xcb\x01\n\x0eDeleteOperator\x12/.google.cloud.visionai.v1.DeleteOperatorRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/operators/*}\x12\xb7\x01\n\x0cListAnalyses\x12-.google.cloud.visionai.v1.ListAnalysesRequest\x1a..google.cloud.visionai.v1.ListAnalysesResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*/clusters/*}/analyses\x12\xa7\x01\n\x0bGetAnalysis\x12,.google.cloud.visionai.v1.GetAnalysisRequest\x1a".google.cloud.visionai.v1.Analysis"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/clusters/*/analyses/*}\x12\xea\x01\n\x0eCreateAnalysis\x12/.google.cloud.visionai.v1.CreateAnalysisRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x1bparent,analysis,analysis_id\x82\xd3\xe4\x93\x02C"7/v1/{parent=projects/*/locations/*/clusters/*}/analyses:\x08analysis\x12\xec\x01\n\x0eUpdateAnalysis\x12/.google.cloud.visionai.v1.UpdateAnalysisRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x14analysis,update_mask\x82\xd3\xe4\x93\x02L2@/v1/{analysis.name=projects/*/locations/*/clusters/*/analyses/*}:\x08analysis\x12\xd5\x01\n\x0eDeleteAnalysis\x12/.google.cloud.visionai.v1.DeleteAnalysisRequest\x1a\x1d.google.longrunning.Operation"s\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/clusters/*/analyses/*}\x12\xbb\x01\n\rListProcesses\x12..google.cloud.visionai.v1.ListProcessesRequest\x1a/.google.cloud.visionai.v1.ListProcessesResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/clusters/*}/processes\x12\xa5\x01\n\nGetProcess\x12+.google.cloud.visionai.v1.GetProcessRequest\x1a!.google.cloud.visionai.v1.Process"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/clusters/*/processes/*}\x12\xe5\x01\n\rCreateProcess\x12..google.cloud.visionai.v1.CreateProcessRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA\x1c\n\x07Process\x12\x11OperationMetadata\xdaA\x19parent,process,process_id\x82\xd3\xe4\x93\x02C"8/v1/{parent=projects/*/locations/*/clusters/*}/processes:\x07process\x12\xe7\x01\n\rUpdateProcess\x12..google.cloud.visionai.v1.UpdateProcessRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA\x1c\n\x07Process\x12\x11OperationMetadata\xdaA\x13process,update_mask\x82\xd3\xe4\x93\x02K2@/v1/{process.name=projects/*/locations/*/clusters/*/processes/*}:\x07process\x12\xd4\x01\n\rDeleteProcess\x12..google.cloud.visionai.v1.DeleteProcessRequest\x1a\x1d.google.longrunning.Operation"t\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/clusters/*/processes/*}\x12\xf2\x01\n\x0fBatchRunProcess\x120.google.cloud.visionai.v1.BatchRunProcessRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA,\n\x17BatchRunProcessResponse\x12\x11OperationMetadata\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02F"A/v1/{parent=projects/*/locations/*/clusters/*}/processes:batchRun:\x01*\x1aK\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbf\x01\n\x1ccom.google.cloud.visionai.v1B\x0fLvaServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.lva_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x0fLvaServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_LISTOPERATORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOPERATORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETOPERATORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETOPERATORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n visionai.googleapis.com/Operator'
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['operator_id']._loaded_options = None
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['operator_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['operator']._loaded_options = None
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['operator']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEOPERATORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEOPERATORREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEOPERATORREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEOPERATORREQUEST'].fields_by_name['operator']._loaded_options = None
    _globals['_UPDATEOPERATORREQUEST'].fields_by_name['operator']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEOPERATORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEOPERATORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEOPERATORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEOPERATORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n visionai.googleapis.com/Operator'
    _globals['_DELETEOPERATORREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEOPERATORREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTANALYSESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTANALYSESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_GETANALYSISREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETANALYSISREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis'
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['analysis_id']._loaded_options = None
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['analysis_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['analysis']._loaded_options = None
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['analysis']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEANALYSISREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEANALYSISREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEANALYSISREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEANALYSISREQUEST'].fields_by_name['analysis']._loaded_options = None
    _globals['_UPDATEANALYSISREQUEST'].fields_by_name['analysis']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEANALYSISREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEANALYSISREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEANALYSISREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEANALYSISREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis'
    _globals['_DELETEANALYSISREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEANALYSISREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPROCESSESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROCESSESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_GETPROCESSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROCESSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Process'
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['process_id']._loaded_options = None
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['process_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['process']._loaded_options = None
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['process']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEPROCESSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPROCESSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPROCESSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPROCESSREQUEST'].fields_by_name['process']._loaded_options = None
    _globals['_UPDATEPROCESSREQUEST'].fields_by_name['process']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPROCESSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEPROCESSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPROCESSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPROCESSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Process'
    _globals['_DELETEPROCESSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEPROCESSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster'
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['options']._loaded_options = None
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['options']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['batch_id']._loaded_options = None
    _globals['_BATCHRUNPROCESSREQUEST'].fields_by_name['batch_id']._serialized_options = b'\xe0A\x03'
    _globals['_RESOLVEOPERATORINFOREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RESOLVEOPERATORINFOREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_RESOLVEOPERATORINFOREQUEST'].fields_by_name['queries']._loaded_options = None
    _globals['_RESOLVEOPERATORINFOREQUEST'].fields_by_name['queries']._serialized_options = b'\xe0A\x02'
    _globals['_OPERATORQUERY'].fields_by_name['operator']._loaded_options = None
    _globals['_OPERATORQUERY'].fields_by_name['operator']._serialized_options = b'\xe0A\x02'
    _globals['_OPERATORQUERY'].fields_by_name['tag']._loaded_options = None
    _globals['_OPERATORQUERY'].fields_by_name['tag']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATORQUERY'].fields_by_name['registry']._loaded_options = None
    _globals['_OPERATORQUERY'].fields_by_name['registry']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPUBLICOPERATORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPUBLICOPERATORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LIVEVIDEOANALYTICS']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS']._serialized_options = b'\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListPublicOperators']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListPublicOperators']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}:listPublicOperators'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ResolveOperatorInfo']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ResolveOperatorInfo']._serialized_options = b'\xdaA\x0eparent,queries\x82\xd3\xe4\x93\x02<"7/v1/{parent=projects/*/locations/*}:resolveOperatorInfo:\x01*'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListOperators']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListOperators']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/operators'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetOperator']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetOperator']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/operators/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateOperator']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateOperator']._serialized_options = b'\xcaA\x1d\n\x08Operator\x12\x11OperationMetadata\xdaA\x1bparent,operator,operator_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/operators:\x08operator'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateOperator']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateOperator']._serialized_options = b'\xcaA\x1d\n\x08Operator\x12\x11OperationMetadata\xdaA\x14operator,update_mask\x82\xd3\xe4\x93\x02B26/v1/{operator.name=projects/*/locations/*/operators/*}:\x08operator'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteOperator']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteOperator']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/operators/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListAnalyses']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListAnalyses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*/clusters/*}/analyses'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetAnalysis']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/clusters/*/analyses/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateAnalysis']._serialized_options = b'\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x1bparent,analysis,analysis_id\x82\xd3\xe4\x93\x02C"7/v1/{parent=projects/*/locations/*/clusters/*}/analyses:\x08analysis'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateAnalysis']._serialized_options = b'\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x14analysis,update_mask\x82\xd3\xe4\x93\x02L2@/v1/{analysis.name=projects/*/locations/*/clusters/*/analyses/*}:\x08analysis'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteAnalysis']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/clusters/*/analyses/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListProcesses']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListProcesses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/clusters/*}/processes'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetProcess']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetProcess']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/clusters/*/processes/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateProcess']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateProcess']._serialized_options = b'\xcaA\x1c\n\x07Process\x12\x11OperationMetadata\xdaA\x19parent,process,process_id\x82\xd3\xe4\x93\x02C"8/v1/{parent=projects/*/locations/*/clusters/*}/processes:\x07process'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateProcess']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateProcess']._serialized_options = b'\xcaA\x1c\n\x07Process\x12\x11OperationMetadata\xdaA\x13process,update_mask\x82\xd3\xe4\x93\x02K2@/v1/{process.name=projects/*/locations/*/clusters/*/processes/*}:\x07process'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteProcess']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteProcess']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/clusters/*/processes/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['BatchRunProcess']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['BatchRunProcess']._serialized_options = b'\xcaA,\n\x17BatchRunProcessResponse\x12\x11OperationMetadata\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02F"A/v1/{parent=projects/*/locations/*/clusters/*}/processes:batchRun:\x01*'
    _globals['_REGISTRY']._serialized_start = 3896
    _globals['_REGISTRY']._serialized_end = 3957
    _globals['_LISTOPERATORSREQUEST']._serialized_start = 373
    _globals['_LISTOPERATORSREQUEST']._serialized_end = 527
    _globals['_LISTOPERATORSRESPONSE']._serialized_start = 529
    _globals['_LISTOPERATORSRESPONSE']._serialized_end = 653
    _globals['_GETOPERATORREQUEST']._serialized_start = 655
    _globals['_GETOPERATORREQUEST']._serialized_end = 731
    _globals['_CREATEOPERATORREQUEST']._serialized_start = 734
    _globals['_CREATEOPERATORREQUEST']._serialized_end = 926
    _globals['_UPDATEOPERATORREQUEST']._serialized_start = 929
    _globals['_UPDATEOPERATORREQUEST']._serialized_end = 1090
    _globals['_DELETEOPERATORREQUEST']._serialized_start = 1092
    _globals['_DELETEOPERATORREQUEST']._serialized_end = 1196
    _globals['_LISTANALYSESREQUEST']._serialized_start = 1199
    _globals['_LISTANALYSESREQUEST']._serialized_end = 1350
    _globals['_LISTANALYSESRESPONSE']._serialized_start = 1352
    _globals['_LISTANALYSESRESPONSE']._serialized_end = 1474
    _globals['_GETANALYSISREQUEST']._serialized_start = 1476
    _globals['_GETANALYSISREQUEST']._serialized_end = 1552
    _globals['_CREATEANALYSISREQUEST']._serialized_start = 1555
    _globals['_CREATEANALYSISREQUEST']._serialized_end = 1745
    _globals['_UPDATEANALYSISREQUEST']._serialized_start = 1748
    _globals['_UPDATEANALYSISREQUEST']._serialized_end = 1909
    _globals['_DELETEANALYSISREQUEST']._serialized_start = 1911
    _globals['_DELETEANALYSISREQUEST']._serialized_end = 2015
    _globals['_LISTPROCESSESREQUEST']._serialized_start = 2018
    _globals['_LISTPROCESSESREQUEST']._serialized_end = 2170
    _globals['_LISTPROCESSESRESPONSE']._serialized_start = 2172
    _globals['_LISTPROCESSESRESPONSE']._serialized_end = 2295
    _globals['_GETPROCESSREQUEST']._serialized_start = 2297
    _globals['_GETPROCESSREQUEST']._serialized_end = 2371
    _globals['_CREATEPROCESSREQUEST']._serialized_start = 2374
    _globals['_CREATEPROCESSREQUEST']._serialized_end = 2560
    _globals['_UPDATEPROCESSREQUEST']._serialized_start = 2563
    _globals['_UPDATEPROCESSREQUEST']._serialized_end = 2721
    _globals['_DELETEPROCESSREQUEST']._serialized_start = 2723
    _globals['_DELETEPROCESSREQUEST']._serialized_end = 2825
    _globals['_BATCHRUNPROCESSREQUEST']._serialized_start = 2828
    _globals['_BATCHRUNPROCESSREQUEST']._serialized_end = 3165
    _globals['_BATCHRUNPROCESSREQUEST_BATCHRUNPROCESSOPTIONS']._serialized_start = 3100
    _globals['_BATCHRUNPROCESSREQUEST_BATCHRUNPROCESSOPTIONS']._serialized_end = 3165
    _globals['_BATCHRUNPROCESSRESPONSE']._serialized_start = 3167
    _globals['_BATCHRUNPROCESSRESPONSE']._serialized_end = 3264
    _globals['_RESOLVEOPERATORINFOREQUEST']._serialized_start = 3267
    _globals['_RESOLVEOPERATORINFOREQUEST']._serialized_end = 3417
    _globals['_OPERATORQUERY']._serialized_start = 3419
    _globals['_OPERATORQUERY']._serialized_end = 3534
    _globals['_RESOLVEOPERATORINFORESPONSE']._serialized_start = 3536
    _globals['_RESOLVEOPERATORINFORESPONSE']._serialized_end = 3620
    _globals['_LISTPUBLICOPERATORSREQUEST']._serialized_start = 3623
    _globals['_LISTPUBLICOPERATORSREQUEST']._serialized_end = 3783
    _globals['_LISTPUBLICOPERATORSRESPONSE']._serialized_start = 3785
    _globals['_LISTPUBLICOPERATORSRESPONSE']._serialized_end = 3894
    _globals['_LIVEVIDEOANALYTICS']._serialized_start = 3960
    _globals['_LIVEVIDEOANALYTICS']._serialized_end = 7813