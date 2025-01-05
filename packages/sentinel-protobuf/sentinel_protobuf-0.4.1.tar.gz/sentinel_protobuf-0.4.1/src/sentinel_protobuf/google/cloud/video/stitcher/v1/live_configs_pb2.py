"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/live_configs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.video.stitcher.v1 import fetch_options_pb2 as google_dot_cloud_dot_video_dot_stitcher_dot_v1_dot_fetch__options__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/video/stitcher/v1/live_configs.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/video/stitcher/v1/fetch_options.proto\x1a\x1egoogle/protobuf/duration.proto"\xda\x06\n\nLiveConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nsource_uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\nad_tag_uri\x18\x03 \x01(\t\x12F\n\x0fgam_live_config\x18\x04 \x01(\x0b2-.google.cloud.video.stitcher.v1.GamLiveConfig\x12D\n\x05state\x18\x05 \x01(\x0e20.google.cloud.video.stitcher.v1.LiveConfig.StateB\x03\xe0A\x03\x12D\n\x0bad_tracking\x18\x06 \x01(\x0e2*.google.cloud.video.stitcher.v1.AdTrackingB\x03\xe0A\x02\x12>\n\rdefault_slate\x18\x07 \x01(\tB\'\xfaA$\n"videostitcher.googleapis.com/Slate\x12T\n\x10stitching_policy\x18\x08 \x01(\x0e2:.google.cloud.video.stitcher.v1.LiveConfig.StitchingPolicy\x12G\n\x0fprefetch_config\x18\n \x01(\x0b2..google.cloud.video.stitcher.v1.PrefetchConfig\x12J\n\x14source_fetch_options\x18\x10 \x01(\x0b2,.google.cloud.video.stitcher.v1.FetchOptions"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03"U\n\x0fStitchingPolicy\x12 \n\x1cSTITCHING_POLICY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bCUT_CURRENT\x10\x01\x12\x0f\n\x0bCOMPLETE_AD\x10\x02:o\xeaAl\n\'videostitcher.googleapis.com/LiveConfig\x12Aprojects/{project}/locations/{location}/liveConfigs/{live_config}"f\n\x0ePrefetchConfig\x12\x14\n\x07enabled\x18\x01 \x01(\x08B\x03\xe0A\x02\x12>\n\x1binitial_ad_request_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"a\n\rGamLiveConfig\x12\x19\n\x0cnetwork_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tasset_key\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10custom_asset_key\x18\x03 \x01(\tB\x03\xe0A\x03*A\n\nAdTracking\x12\x1b\n\x17AD_TRACKING_UNSPECIFIED\x10\x00\x12\n\n\x06CLIENT\x10\x01\x12\n\n\x06SERVER\x10\x02Bx\n"com.google.cloud.video.stitcher.v1B\x10LiveConfigsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.live_configs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x10LiveConfigsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_LIVECONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_LIVECONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LIVECONFIG'].fields_by_name['source_uri']._loaded_options = None
    _globals['_LIVECONFIG'].fields_by_name['source_uri']._serialized_options = b'\xe0A\x02'
    _globals['_LIVECONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_LIVECONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_LIVECONFIG'].fields_by_name['ad_tracking']._loaded_options = None
    _globals['_LIVECONFIG'].fields_by_name['ad_tracking']._serialized_options = b'\xe0A\x02'
    _globals['_LIVECONFIG'].fields_by_name['default_slate']._loaded_options = None
    _globals['_LIVECONFIG'].fields_by_name['default_slate']._serialized_options = b'\xfaA$\n"videostitcher.googleapis.com/Slate'
    _globals['_LIVECONFIG']._loaded_options = None
    _globals['_LIVECONFIG']._serialized_options = b"\xeaAl\n'videostitcher.googleapis.com/LiveConfig\x12Aprojects/{project}/locations/{location}/liveConfigs/{live_config}"
    _globals['_PREFETCHCONFIG'].fields_by_name['enabled']._loaded_options = None
    _globals['_PREFETCHCONFIG'].fields_by_name['enabled']._serialized_options = b'\xe0A\x02'
    _globals['_GAMLIVECONFIG'].fields_by_name['network_code']._loaded_options = None
    _globals['_GAMLIVECONFIG'].fields_by_name['network_code']._serialized_options = b'\xe0A\x02'
    _globals['_GAMLIVECONFIG'].fields_by_name['asset_key']._loaded_options = None
    _globals['_GAMLIVECONFIG'].fields_by_name['asset_key']._serialized_options = b'\xe0A\x03'
    _globals['_GAMLIVECONFIG'].fields_by_name['custom_asset_key']._loaded_options = None
    _globals['_GAMLIVECONFIG'].fields_by_name['custom_asset_key']._serialized_options = b'\xe0A\x03'
    _globals['_ADTRACKING']._serialized_start = 1293
    _globals['_ADTRACKING']._serialized_end = 1358
    _globals['_LIVECONFIG']._serialized_start = 230
    _globals['_LIVECONFIG']._serialized_end = 1088
    _globals['_LIVECONFIG_STATE']._serialized_start = 819
    _globals['_LIVECONFIG_STATE']._serialized_end = 888
    _globals['_LIVECONFIG_STITCHINGPOLICY']._serialized_start = 890
    _globals['_LIVECONFIG_STITCHINGPOLICY']._serialized_end = 975
    _globals['_PREFETCHCONFIG']._serialized_start = 1090
    _globals['_PREFETCHCONFIG']._serialized_end = 1192
    _globals['_GAMLIVECONFIG']._serialized_start = 1194
    _globals['_GAMLIVECONFIG']._serialized_end = 1291