"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/aerialview/v1/aerial_view.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/maps/aerialview/v1/aerial_view.proto\x12\x19google.maps.aerialview.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x16google/type/date.proto"\xca\x02\n\x05Video\x128\n\x04uris\x18\x01 \x03(\x0b2*.google.maps.aerialview.v1.Video.UrisEntry\x125\n\x05state\x18\x02 \x01(\x0e2&.google.maps.aerialview.v1.Video.State\x12:\n\x08metadata\x18\x03 \x01(\x0b2(.google.maps.aerialview.v1.VideoMetadata\x1aL\n\tUrisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b2\x1f.google.maps.aerialview.v1.Uris:\x028\x01"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\n\n\x06FAILED\x10\x03"3\n\x04Uris\x12\x15\n\rlandscape_uri\x18\x01 \x01(\t\x12\x14\n\x0cportrait_uri\x18\x02 \x01(\t"w\n\rVideoMetadata\x12\x10\n\x08video_id\x18\x01 \x01(\t\x12\'\n\x0ccapture_date\x18\x02 \x01(\x0b2\x11.google.type.Date\x12+\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration"*\n\x12RenderVideoRequest\x12\x14\n\x07address\x18\x01 \x01(\tB\x03\xe0A\x02"\x88\x01\n\x13RenderVideoResponse\x125\n\x05state\x18\x01 \x01(\x0e2&.google.maps.aerialview.v1.Video.State\x12:\n\x08metadata\x18\x02 \x01(\x0b2(.google.maps.aerialview.v1.VideoMetadata"B\n\x12LookupVideoRequest\x12\x12\n\x08video_id\x18\x01 \x01(\tH\x00\x12\x11\n\x07address\x18\x02 \x01(\tH\x00B\x05\n\x03key2\xf7\x02\n\nAerialView\x12\x99\x01\n\x0bRenderVideo\x12-.google.maps.aerialview.v1.RenderVideoRequest\x1a..google.maps.aerialview.v1.RenderVideoResponse"+\xdaA\x07address\x82\xd3\xe4\x93\x02\x1b"\x16/v1/videos:renderVideo:\x01*\x12~\n\x0bLookupVideo\x12-.google.maps.aerialview.v1.LookupVideoRequest\x1a .google.maps.aerialview.v1.Video"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/videos:lookupVideo\x1aM\xcaA\x19aerialview.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd8\x01\n\x1dcom.google.maps.aerialview.v1B\x0fAerialViewProtoP\x01ZCcloud.google.com/go/maps/aerialview/apiv1/aerialviewpb;aerialviewpb\xa2\x02\x07GGMPV1B\xaa\x02\x19Google.Maps.AerialView.V1\xca\x02\x19Google\\Maps\\AerialView\\V1\xea\x02\x1cGoogle::Maps::AerialView::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.aerialview.v1.aerial_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.maps.aerialview.v1B\x0fAerialViewProtoP\x01ZCcloud.google.com/go/maps/aerialview/apiv1/aerialviewpb;aerialviewpb\xa2\x02\x07GGMPV1B\xaa\x02\x19Google.Maps.AerialView.V1\xca\x02\x19Google\\Maps\\AerialView\\V1\xea\x02\x1cGoogle::Maps::AerialView::V1'
    _globals['_VIDEO_URISENTRY']._loaded_options = None
    _globals['_VIDEO_URISENTRY']._serialized_options = b'8\x01'
    _globals['_RENDERVIDEOREQUEST'].fields_by_name['address']._loaded_options = None
    _globals['_RENDERVIDEOREQUEST'].fields_by_name['address']._serialized_options = b'\xe0A\x02'
    _globals['_AERIALVIEW']._loaded_options = None
    _globals['_AERIALVIEW']._serialized_options = b'\xcaA\x19aerialview.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AERIALVIEW'].methods_by_name['RenderVideo']._loaded_options = None
    _globals['_AERIALVIEW'].methods_by_name['RenderVideo']._serialized_options = b'\xdaA\x07address\x82\xd3\xe4\x93\x02\x1b"\x16/v1/videos:renderVideo:\x01*'
    _globals['_AERIALVIEW'].methods_by_name['LookupVideo']._loaded_options = None
    _globals['_AERIALVIEW'].methods_by_name['LookupVideo']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/videos:lookupVideo'
    _globals['_VIDEO']._serialized_start = 219
    _globals['_VIDEO']._serialized_end = 549
    _globals['_VIDEO_URISENTRY']._serialized_start = 401
    _globals['_VIDEO_URISENTRY']._serialized_end = 477
    _globals['_VIDEO_STATE']._serialized_start = 479
    _globals['_VIDEO_STATE']._serialized_end = 549
    _globals['_URIS']._serialized_start = 551
    _globals['_URIS']._serialized_end = 602
    _globals['_VIDEOMETADATA']._serialized_start = 604
    _globals['_VIDEOMETADATA']._serialized_end = 723
    _globals['_RENDERVIDEOREQUEST']._serialized_start = 725
    _globals['_RENDERVIDEOREQUEST']._serialized_end = 767
    _globals['_RENDERVIDEORESPONSE']._serialized_start = 770
    _globals['_RENDERVIDEORESPONSE']._serialized_end = 906
    _globals['_LOOKUPVIDEOREQUEST']._serialized_start = 908
    _globals['_LOOKUPVIDEOREQUEST']._serialized_end = 974
    _globals['_AERIALVIEW']._serialized_start = 977
    _globals['_AERIALVIEW']._serialized_end = 1352