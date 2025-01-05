"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1alpha1/lva_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.visionai.v1alpha1 import lva_resources_pb2 as google_dot_cloud_dot_visionai_dot_v1alpha1_dot_lva__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/visionai/v1alpha1/lva_service.proto\x12\x1egoogle.cloud.visionai.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/visionai/v1alpha1/lva_resources.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto"\x97\x01\n\x13ListAnalysesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x80\x01\n\x14ListAnalysesResponse\x12:\n\x08analyses\x18\x01 \x03(\x0b2(.google.cloud.visionai.v1alpha1.Analysis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x12GetAnalysisRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis"\xc4\x01\n\x15CreateAnalysisRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fvisionai.googleapis.com/Cluster\x12\x18\n\x0banalysis_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\x08analysis\x18\x03 \x01(\x0b2(.google.cloud.visionai.v1alpha1.AnalysisB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa7\x01\n\x15UpdateAnalysisRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12?\n\x08analysis\x18\x02 \x01(\x0b2(.google.cloud.visionai.v1alpha1.AnalysisB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"h\n\x15DeleteAnalysisRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x012\xc1\t\n\x12LiveVideoAnalytics\x12\xc9\x01\n\x0cListAnalyses\x123.google.cloud.visionai.v1alpha1.ListAnalysesRequest\x1a4.google.cloud.visionai.v1alpha1.ListAnalysesResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1alpha1/{parent=projects/*/locations/*/clusters/*}/analyses\x12\xb9\x01\n\x0bGetAnalysis\x122.google.cloud.visionai.v1alpha1.GetAnalysisRequest\x1a(.google.cloud.visionai.v1alpha1.Analysis"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1alpha1/{name=projects/*/locations/*/clusters/*/analyses/*}\x12\xf6\x01\n\x0eCreateAnalysis\x125.google.cloud.visionai.v1alpha1.CreateAnalysisRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x1bparent,analysis,analysis_id\x82\xd3\xe4\x93\x02I"=/v1alpha1/{parent=projects/*/locations/*/clusters/*}/analyses:\x08analysis\x12\xf8\x01\n\x0eUpdateAnalysis\x125.google.cloud.visionai.v1alpha1.UpdateAnalysisRequest\x1a\x1d.google.longrunning.Operation"\x8f\x01\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x14analysis,update_mask\x82\xd3\xe4\x93\x02R2F/v1alpha1/{analysis.name=projects/*/locations/*/clusters/*/analyses/*}:\x08analysis\x12\xe1\x01\n\x0eDeleteAnalysis\x125.google.cloud.visionai.v1alpha1.DeleteAnalysisRequest\x1a\x1d.google.longrunning.Operation"y\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1alpha1/{name=projects/*/locations/*/clusters/*/analyses/*}\x1aK\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdd\x01\n"com.google.cloud.visionai.v1alpha1B\x0fLvaServiceProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.lva_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x0fLvaServiceProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
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
    _globals['_LIVEVIDEOANALYTICS']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS']._serialized_options = b'\xcaA\x17visionai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListAnalyses']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['ListAnalyses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1alpha1/{parent=projects/*/locations/*/clusters/*}/analyses'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['GetAnalysis']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1alpha1/{name=projects/*/locations/*/clusters/*/analyses/*}'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['CreateAnalysis']._serialized_options = b'\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x1bparent,analysis,analysis_id\x82\xd3\xe4\x93\x02I"=/v1alpha1/{parent=projects/*/locations/*/clusters/*}/analyses:\x08analysis'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['UpdateAnalysis']._serialized_options = b'\xcaA\x1d\n\x08Analysis\x12\x11OperationMetadata\xdaA\x14analysis,update_mask\x82\xd3\xe4\x93\x02R2F/v1alpha1/{analysis.name=projects/*/locations/*/clusters/*/analyses/*}:\x08analysis'
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteAnalysis']._loaded_options = None
    _globals['_LIVEVIDEOANALYTICS'].methods_by_name['DeleteAnalysis']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1alpha1/{name=projects/*/locations/*/clusters/*/analyses/*}'
    _globals['_LISTANALYSESREQUEST']._serialized_start = 323
    _globals['_LISTANALYSESREQUEST']._serialized_end = 474
    _globals['_LISTANALYSESRESPONSE']._serialized_start = 477
    _globals['_LISTANALYSESRESPONSE']._serialized_end = 605
    _globals['_GETANALYSISREQUEST']._serialized_start = 607
    _globals['_GETANALYSISREQUEST']._serialized_end = 683
    _globals['_CREATEANALYSISREQUEST']._serialized_start = 686
    _globals['_CREATEANALYSISREQUEST']._serialized_end = 882
    _globals['_UPDATEANALYSISREQUEST']._serialized_start = 885
    _globals['_UPDATEANALYSISREQUEST']._serialized_end = 1052
    _globals['_DELETEANALYSISREQUEST']._serialized_start = 1054
    _globals['_DELETEANALYSISREQUEST']._serialized_end = 1158
    _globals['_LIVEVIDEOANALYTICS']._serialized_start = 1161
    _globals['_LIVEVIDEOANALYTICS']._serialized_end = 2378