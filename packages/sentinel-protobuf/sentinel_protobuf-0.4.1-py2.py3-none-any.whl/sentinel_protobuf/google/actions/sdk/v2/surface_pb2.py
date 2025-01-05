"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/surface.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/actions/sdk/v2/surface.proto\x12\x15google.actions.sdk.v2"a\n\x13SurfaceRequirements\x12J\n\x14minimum_requirements\x18\x01 \x03(\x0b2,.google.actions.sdk.v2.CapabilityRequirement"\xb4\x02\n\x15CapabilityRequirement\x12R\n\ncapability\x18\x01 \x01(\x0e2>.google.actions.sdk.v2.CapabilityRequirement.SurfaceCapability"\xc6\x01\n\x11SurfaceCapability\x12"\n\x1eSURFACE_CAPABILITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cAUDIO_OUTPUT\x10\x01\x12\x11\n\rSCREEN_OUTPUT\x10\x02\x12\x18\n\x14MEDIA_RESPONSE_AUDIO\x10\x03\x12\x0f\n\x0bWEB_BROWSER\x10\x04\x12\x13\n\x0fACCOUNT_LINKING\x10\x07\x12\x16\n\x12INTERACTIVE_CANVAS\x10\x08\x12\x10\n\x0cHOME_STORAGE\x10\tBe\n\x19com.google.actions.sdk.v2B\x0cSurfaceProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.surface_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x0cSurfaceProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_SURFACEREQUIREMENTS']._serialized_start = 62
    _globals['_SURFACEREQUIREMENTS']._serialized_end = 159
    _globals['_CAPABILITYREQUIREMENT']._serialized_start = 162
    _globals['_CAPABILITYREQUIREMENT']._serialized_end = 470
    _globals['_CAPABILITYREQUIREMENT_SURFACECAPABILITY']._serialized_start = 272
    _globals['_CAPABILITYREQUIREMENT_SURFACECAPABILITY']._serialized_end = 470