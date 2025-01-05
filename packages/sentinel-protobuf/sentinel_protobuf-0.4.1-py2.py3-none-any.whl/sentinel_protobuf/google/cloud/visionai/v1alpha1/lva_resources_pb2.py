"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1alpha1/lva_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.visionai.v1alpha1 import lva_pb2 as google_dot_cloud_dot_visionai_dot_v1alpha1_dot_lva__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/visionai/v1alpha1/lva_resources.proto\x12\x1egoogle.cloud.visionai.v1alpha1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/visionai/v1alpha1/lva.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x80\x06\n\x08Analysis\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\x06labels\x18\x04 \x03(\x0b24.google.cloud.visionai.v1alpha1.Analysis.LabelsEntry\x12O\n\x13analysis_definition\x18\x05 \x01(\x0b22.google.cloud.visionai.v1alpha1.AnalysisDefinition\x12`\n\x15input_streams_mapping\x18\x06 \x03(\x0b2A.google.cloud.visionai.v1alpha1.Analysis.InputStreamsMappingEntry\x12b\n\x16output_streams_mapping\x18\x07 \x03(\x0b2B.google.cloud.visionai.v1alpha1.Analysis.OutputStreamsMappingEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a:\n\x18InputStreamsMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a;\n\x19OutputStreamsMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:u\xeaAr\n visionai.googleapis.com/Analysis\x12Nprojects/{project}/locations/{location}/clusters/{cluster}/analyses/{analysis}B\xdf\x01\n"com.google.cloud.visionai.v1alpha1B\x11LvaResourcesProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.lva_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x11LvaResourcesProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
    _globals['_ANALYSIS_LABELSENTRY']._loaded_options = None
    _globals['_ANALYSIS_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ANALYSIS_INPUTSTREAMSMAPPINGENTRY']._loaded_options = None
    _globals['_ANALYSIS_INPUTSTREAMSMAPPINGENTRY']._serialized_options = b'8\x01'
    _globals['_ANALYSIS_OUTPUTSTREAMSMAPPINGENTRY']._loaded_options = None
    _globals['_ANALYSIS_OUTPUTSTREAMSMAPPINGENTRY']._serialized_options = b'8\x01'
    _globals['_ANALYSIS'].fields_by_name['create_time']._loaded_options = None
    _globals['_ANALYSIS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANALYSIS'].fields_by_name['update_time']._loaded_options = None
    _globals['_ANALYSIS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANALYSIS']._loaded_options = None
    _globals['_ANALYSIS']._serialized_options = b'\xeaAr\n visionai.googleapis.com/Analysis\x12Nprojects/{project}/locations/{location}/clusters/{cluster}/analyses/{analysis}'
    _globals['_ANALYSIS']._serialized_start = 222
    _globals['_ANALYSIS']._serialized_end = 990
    _globals['_ANALYSIS_LABELSENTRY']._serialized_start = 705
    _globals['_ANALYSIS_LABELSENTRY']._serialized_end = 750
    _globals['_ANALYSIS_INPUTSTREAMSMAPPINGENTRY']._serialized_start = 752
    _globals['_ANALYSIS_INPUTSTREAMSMAPPINGENTRY']._serialized_end = 810
    _globals['_ANALYSIS_OUTPUTSTREAMSMAPPINGENTRY']._serialized_start = 812
    _globals['_ANALYSIS_OUTPUTSTREAMSMAPPINGENTRY']._serialized_end = 871