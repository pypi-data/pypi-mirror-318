"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/surface_capabilities.proto')
_sym_db = _symbol_database.Default()
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/actions/sdk/v2/interactionmodel/prompt/surface_capabilities.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1a\x1fgoogle/api/field_behavior.proto"\x8b\x02\n\x13SurfaceCapabilities\x12h\n\x0ccapabilities\x18\x01 \x03(\x0e2M.google.actions.sdk.v2.interactionmodel.prompt.SurfaceCapabilities.CapabilityB\x03\xe0A\x02"\x89\x01\n\nCapability\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06SPEECH\x10\x01\x12\x11\n\rRICH_RESPONSE\x10\x02\x12\x13\n\x0fLONG_FORM_AUDIO\x10\x03\x12\x16\n\x12INTERACTIVE_CANVAS\x10\x04\x12\x0c\n\x08WEB_LINK\x10\x05\x12\x10\n\x0cHOME_STORAGE\x10\x06B\xa4\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x18SurfaceCapabilitiesProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.surface_capabilities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x18SurfaceCapabilitiesProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_SURFACECAPABILITIES'].fields_by_name['capabilities']._loaded_options = None
    _globals['_SURFACECAPABILITIES'].fields_by_name['capabilities']._serialized_options = b'\xe0A\x02'
    _globals['_SURFACECAPABILITIES']._serialized_start = 157
    _globals['_SURFACECAPABILITIES']._serialized_end = 424
    _globals['_SURFACECAPABILITIES_CAPABILITY']._serialized_start = 287
    _globals['_SURFACECAPABILITIES_CAPABILITY']._serialized_end = 424