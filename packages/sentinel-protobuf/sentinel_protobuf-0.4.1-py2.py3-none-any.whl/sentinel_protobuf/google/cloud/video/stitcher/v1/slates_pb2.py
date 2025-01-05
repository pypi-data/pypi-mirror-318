"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/slates.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/video/stitcher/v1/slates.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8d\x02\n\x05Slate\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12A\n\tgam_slate\x18\x03 \x01(\x0b2..google.cloud.video.stitcher.v1.Slate.GamSlate\x1a@\n\x08GamSlate\x12\x19\n\x0cnetwork_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cgam_slate_id\x18\x02 \x01(\x03B\x03\xe0A\x03:_\xeaA\\\n"videostitcher.googleapis.com/Slate\x126projects/{project}/locations/{location}/slates/{slate}Bs\n"com.google.cloud.video.stitcher.v1B\x0bSlatesProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.slates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x0bSlatesProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_SLATE_GAMSLATE'].fields_by_name['network_code']._loaded_options = None
    _globals['_SLATE_GAMSLATE'].fields_by_name['network_code']._serialized_options = b'\xe0A\x02'
    _globals['_SLATE_GAMSLATE'].fields_by_name['gam_slate_id']._loaded_options = None
    _globals['_SLATE_GAMSLATE'].fields_by_name['gam_slate_id']._serialized_options = b'\xe0A\x03'
    _globals['_SLATE'].fields_by_name['name']._loaded_options = None
    _globals['_SLATE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SLATE']._loaded_options = None
    _globals['_SLATE']._serialized_options = b'\xeaA\\\n"videostitcher.googleapis.com/Slate\x126projects/{project}/locations/{location}/slates/{slate}'
    _globals['_SLATE']._serialized_start = 140
    _globals['_SLATE']._serialized_end = 409
    _globals['_SLATE_GAMSLATE']._serialized_start = 248
    _globals['_SLATE_GAMSLATE']._serialized_end = 312