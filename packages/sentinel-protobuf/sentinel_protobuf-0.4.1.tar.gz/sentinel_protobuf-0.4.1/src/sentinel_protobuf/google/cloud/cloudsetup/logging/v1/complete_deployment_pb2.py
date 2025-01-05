"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudsetup/logging/v1/complete_deployment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/cloudsetup/logging/v1/complete_deployment.proto\x12"google.cloud.cloudsetup.logging.v1\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xba\x02\n\x17CompleteDeploymentEvent\x12M\n\x05value\x18\x01 \x01(\x0b2<.google.cloud.cloudsetup.logging.v1.CompleteDeploymentResultH\x00\x12#\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00\x12P\n\x05state\x18\x03 \x01(\x0e2A.google.cloud.cloudsetup.logging.v1.CompleteDeploymentEvent.State\x12\x14\n\x0cpreview_only\x18\x04 \x01(\x08"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02B\x08\n\x06result"\x9b\x01\n\x18CompleteDeploymentResult\x129\n\ndeployment\x18\x01 \x01(\tB%\xfaA"\n config.googleapis.com/Deployment\x123\n\x07preview\x18\x03 \x01(\tB"\xfaA\x1f\n\x1dconfig.googleapis.com/Preview\x12\x0f\n\x07message\x18\x02 \x01(\tB\xf8\x01\n&com.google.cloud.cloudsetup.logging.v1B\x17CompleteDeploymentProtoP\x01Z@cloud.google.com/go/cloudsetup/logging/apiv1/loggingpb;loggingpb\xaa\x02"Google.Cloud.CloudSetup.Logging.V1\xca\x02"Google\\Cloud\\CloudSetup\\Logging\\V1\xea\x02&Google::Cloud::CloudSetup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudsetup.logging.v1.complete_deployment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.cloudsetup.logging.v1B\x17CompleteDeploymentProtoP\x01Z@cloud.google.com/go/cloudsetup/logging/apiv1/loggingpb;loggingpb\xaa\x02"Google.Cloud.CloudSetup.Logging.V1\xca\x02"Google\\Cloud\\CloudSetup\\Logging\\V1\xea\x02&Google::Cloud::CloudSetup::Logging::V1'
    _globals['_COMPLETEDEPLOYMENTRESULT'].fields_by_name['deployment']._loaded_options = None
    _globals['_COMPLETEDEPLOYMENTRESULT'].fields_by_name['deployment']._serialized_options = b'\xfaA"\n config.googleapis.com/Deployment'
    _globals['_COMPLETEDEPLOYMENTRESULT'].fields_by_name['preview']._loaded_options = None
    _globals['_COMPLETEDEPLOYMENTRESULT'].fields_by_name['preview']._serialized_options = b'\xfaA\x1f\n\x1dconfig.googleapis.com/Preview'
    _globals['_COMPLETEDEPLOYMENTEVENT']._serialized_start = 153
    _globals['_COMPLETEDEPLOYMENTEVENT']._serialized_end = 467
    _globals['_COMPLETEDEPLOYMENTEVENT_STATE']._serialized_start = 400
    _globals['_COMPLETEDEPLOYMENTEVENT_STATE']._serialized_end = 457
    _globals['_COMPLETEDEPLOYMENTRESULT']._serialized_start = 470
    _globals['_COMPLETEDEPLOYMENTRESULT']._serialized_end = 625