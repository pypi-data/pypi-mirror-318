"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1/processor_type.proto')
_sym_db = _symbol_database.Default()
from .....google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/documentai/v1/processor_type.proto\x12\x1agoogle.cloud.documentai.v1\x1a\x1dgoogle/api/launch_stage.proto\x1a\x19google/api/resource.proto"\x93\x03\n\rProcessorType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08category\x18\x03 \x01(\t\x12S\n\x13available_locations\x18\x04 \x03(\x0b26.google.cloud.documentai.v1.ProcessorType.LocationInfo\x12\x16\n\x0eallow_creation\x18\x06 \x01(\x08\x12-\n\x0claunch_stage\x18\x08 \x01(\x0e2\x17.google.api.LaunchStage\x12\x1c\n\x14sample_document_uris\x18\t \x03(\t\x1a#\n\x0cLocationInfo\x12\x13\n\x0blocation_id\x18\x01 \x01(\t:u\xeaAr\n\'documentai.googleapis.com/ProcessorType\x12Gprojects/{project}/locations/{location}/processorTypes/{processor_type}B\xd5\x01\n\x1ecom.google.cloud.documentai.v1B\x17DocumentAiProcessorTypeP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1.processor_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.documentai.v1B\x17DocumentAiProcessorTypeP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1'
    _globals['_PROCESSORTYPE']._loaded_options = None
    _globals['_PROCESSORTYPE']._serialized_options = b"\xeaAr\n'documentai.googleapis.com/ProcessorType\x12Gprojects/{project}/locations/{location}/processorTypes/{processor_type}"
    _globals['_PROCESSORTYPE']._serialized_start = 138
    _globals['_PROCESSORTYPE']._serialized_end = 541
    _globals['_PROCESSORTYPE_LOCATIONINFO']._serialized_start = 387
    _globals['_PROCESSORTYPE_LOCATIONINFO']._serialized_end = 422