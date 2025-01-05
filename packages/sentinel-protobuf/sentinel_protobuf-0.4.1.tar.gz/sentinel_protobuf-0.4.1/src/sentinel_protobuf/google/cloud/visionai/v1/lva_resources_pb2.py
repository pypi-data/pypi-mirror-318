"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/visionai/v1/lva_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.visionai.v1 import lva_pb2 as google_dot_cloud_dot_visionai_dot_v1_dot_lva__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/visionai/v1/lva_resources.proto\x12\x18google.cloud.visionai.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/cloud/visionai/v1/lva.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb9\x03\n\x08Operator\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12>\n\x06labels\x18\x04 \x03(\x0b2..google.cloud.visionai.v1.Operator.LabelsEntry\x12I\n\x13operator_definition\x18\x05 \x01(\x0b2,.google.cloud.visionai.v1.OperatorDefinition\x12\x14\n\x0cdocker_image\x18\x06 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:c\xeaA`\n visionai.googleapis.com/Operator\x12<projects/{project}/locations/{location}/operators/{operator}"\x85\x06\n\x08Analysis\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12>\n\x06labels\x18\x04 \x03(\x0b2..google.cloud.visionai.v1.Analysis.LabelsEntry\x12I\n\x13analysis_definition\x18\x05 \x01(\x0b2,.google.cloud.visionai.v1.AnalysisDefinition\x12Z\n\x15input_streams_mapping\x18\x06 \x03(\x0b2;.google.cloud.visionai.v1.Analysis.InputStreamsMappingEntry\x12\\\n\x16output_streams_mapping\x18\x07 \x03(\x0b2<.google.cloud.visionai.v1.Analysis.OutputStreamsMappingEntry\x12\x1b\n\x13disable_event_watch\x18\x08 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a:\n\x18InputStreamsMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a;\n\x19OutputStreamsMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:u\xeaAr\n visionai.googleapis.com/Analysis\x12Nprojects/{project}/locations/{location}/clusters/{cluster}/analyses/{analysis}"\x97\x04\n\x07Process\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x08analysis\x18\x04 \x01(\tB(\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis\x12 \n\x13attribute_overrides\x18\x05 \x03(\tB\x03\xe0A\x01\x12<\n\nrun_status\x18\x06 \x01(\x0b2#.google.cloud.visionai.v1.RunStatusB\x03\xe0A\x01\x128\n\x08run_mode\x18\x07 \x01(\x0e2!.google.cloud.visionai.v1.RunModeB\x03\xe0A\x01\x12\x15\n\x08event_id\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08batch_id\x18\t \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bretry_count\x18\n \x01(\x05B\x03\xe0A\x01:t\xeaAq\n\x1fvisionai.googleapis.com/Process\x12Nprojects/{project}/locations/{location}/clusters/{cluster}/processes/{process}B\xc1\x01\n\x1ccom.google.cloud.visionai.v1B\x11LvaResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.lva_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x11LvaResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_OPERATOR_LABELSENTRY']._loaded_options = None
    _globals['_OPERATOR_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_OPERATOR'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATOR'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_OPERATOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATOR']._loaded_options = None
    _globals['_OPERATOR']._serialized_options = b'\xeaA`\n visionai.googleapis.com/Operator\x12<projects/{project}/locations/{location}/operators/{operator}'
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
    _globals['_PROCESS'].fields_by_name['create_time']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESS'].fields_by_name['update_time']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESS'].fields_by_name['analysis']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['analysis']._serialized_options = b'\xe0A\x02\xfaA"\n visionai.googleapis.com/Analysis'
    _globals['_PROCESS'].fields_by_name['attribute_overrides']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['attribute_overrides']._serialized_options = b'\xe0A\x01'
    _globals['_PROCESS'].fields_by_name['run_status']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['run_status']._serialized_options = b'\xe0A\x01'
    _globals['_PROCESS'].fields_by_name['run_mode']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['run_mode']._serialized_options = b'\xe0A\x01'
    _globals['_PROCESS'].fields_by_name['event_id']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['event_id']._serialized_options = b'\xe0A\x01'
    _globals['_PROCESS'].fields_by_name['batch_id']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['batch_id']._serialized_options = b'\xe0A\x01'
    _globals['_PROCESS'].fields_by_name['retry_count']._loaded_options = None
    _globals['_PROCESS'].fields_by_name['retry_count']._serialized_options = b'\xe0A\x01'
    _globals['_PROCESS']._loaded_options = None
    _globals['_PROCESS']._serialized_options = b'\xeaAq\n\x1fvisionai.googleapis.com/Process\x12Nprojects/{project}/locations/{location}/clusters/{cluster}/processes/{process}'
    _globals['_OPERATOR']._serialized_start = 204
    _globals['_OPERATOR']._serialized_end = 645
    _globals['_OPERATOR_LABELSENTRY']._serialized_start = 499
    _globals['_OPERATOR_LABELSENTRY']._serialized_end = 544
    _globals['_ANALYSIS']._serialized_start = 648
    _globals['_ANALYSIS']._serialized_end = 1421
    _globals['_ANALYSIS_LABELSENTRY']._serialized_start = 499
    _globals['_ANALYSIS_LABELSENTRY']._serialized_end = 544
    _globals['_ANALYSIS_INPUTSTREAMSMAPPINGENTRY']._serialized_start = 1183
    _globals['_ANALYSIS_INPUTSTREAMSMAPPINGENTRY']._serialized_end = 1241
    _globals['_ANALYSIS_OUTPUTSTREAMSMAPPINGENTRY']._serialized_start = 1243
    _globals['_ANALYSIS_OUTPUTSTREAMSMAPPINGENTRY']._serialized_end = 1302
    _globals['_PROCESS']._serialized_start = 1424
    _globals['_PROCESS']._serialized_end = 1959